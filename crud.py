import asyncio
from sqlalchemy import Result, select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User, Profile, Post


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    print(user)
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)

    # result: Result = await session.execute(statement=stmt)
    # user: User | None = result.scalar_one_or_none()
    user: User | None = await session.scalar(statement=stmt)

    print(f"user = {user}" if user else "Not found")
    return user


async def create_user_profile(
    session: AsyncSession,
    user_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
) -> Profile:
    profile = Profile(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
    )
    session.add(profile)
    await session.commit()
    return profile


async def show_users_with_profiles(session: AsyncSession):
    stmt = select(User).options(joinedload(User.profile)).order_by(User.id)
    # result: Result = await session.execute(statement=stmt)
    # users = result.scalars()
    users = await session.scalars(stmt)
    for user in users:
        print(user)
        print(user.profile.first_name)


async def create_posts(
    session: AsyncSession,
    user_id: int,
    *post_titles: str,
) -> list[Post]:
    posts = [Post(title=title, user_id=user_id) for title in post_titles]
    session.add_all(posts)
    await session.commit()
    print(posts)
    return posts


async def get_user_with_posts(session: AsyncSession):
    stmt = (
        select(User)
        .options(
            # 2 способ
            # joinedload(User.posts)
            selectinload(User.posts)
        )
        .order_by(User.id)
    )
    # 1 - способ
    # users = await session.scalars(stmt)
    # for user in users.unique():
    result: Result = await session.execute(stmt)
    # 2 способ
    # users = result.unique().scalars()
    users = result.scalars()
    for user in users:  # type: User
        print("*" * 33)
        print(user)
        for post in user.posts:
            print(post)


async def get_user_with_posts_and_profiles(session: AsyncSession):
    stmt = (
        select(User)
        .options(joinedload(User.profile), selectinload(User.posts))
        .order_by(User.id)
    )

    users = await session.scalars(stmt)
    for user in users:  # type: User
        print("*" * 33)
        print(user, user.profile and user.profile.first_name)

        for post in user.posts:
            print(post)


async def get_posts_with_authors(session: AsyncSession):

    stmt = select(Post).options(joinedload(Post.user)).order_by(Post.id)
    posts = await session.scalars(stmt)
    for post in posts:  # type: Post
        print("*" * 50)
        print(f"Post: {post}")
        print(f"Author: {post.user}", "\n")


async def get_profiles_with_users_and_users_with_posts(session: AsyncSession):
    stmt = (
        select(Profile)
        .join(Profile.user)
        .options(joinedload(Profile.user).selectinload(User.posts))
        .order_by(Profile.id)
        .where(User.username == 'John')
    )
    profiles = await session.scalars(stmt)

    for profile in profiles:
        print('*'*50)
        print(profile.first_name, profile.user)
        print(profile.user.posts)
        


async def main():
    async with db_helper.session_factory() as session:
        # await create_user(session=session, username="John")
        # await create_user(session=session, username="Sam")
        # await create_user(session=session, username="Jack")

        # user_sam = await get_user_by_username(session=session, username="Sam")
        # user_john = await get_user_by_username(session=session, username="John")

        # await get_user_by_username(session=session, username="Bob")

        # await create_user_profile(
        #     session=session,
        #     user_id=user_john.id,
        #     first_name=user_john.username,
        # )
        # await create_user_profile(
        #     session=session,
        #     user_id=user_sam.id,
        #     first_name=user_sam.username,
        # )

        # await show_users_with_profiles(session=session)

        # await create_posts(
        #     session,
        #     user_john.id,
        #     "Post 1",
        #     "post2",
        # )

        # await create_posts(
        #     session,
        #     user_sam.id,
        #     "Post 1111",
        #     "post2222",
        #     "FastAPI"
        # )

        # await get_user_with_posts(session=session)

        # await get_posts_with_authors(session)

        # await get_user_with_posts_and_profiles(session)

        await get_profiles_with_users_and_users_with_posts(session)

if __name__ == "__main__":
    asyncio.run(main())
