from app.models.user import User, UserSchema
from db_connections import session
from uuid import uuid4

def create_user(user: UserSchema):
    """Create a user."""
    user = User(**user.model_dump(), id=uuid4())
    session.add(user)
    session.commit()
    return user


def get_user(telegram_id: str):
    """Get a user by telegram_id."""
    user = (
        session.query(User)
        .filter(User.telegram_id == telegram_id)
        .filter_by(is_deleted=False)
        .first()
    )
    return user


def get_users(page: int = 1, limit: int = 10):
    """Get all users."""
    users = (
        session.query(User)
        .filter_by(is_deleted=False)
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )
    return users


def update_user(telegram_id: str, user: UserSchema):
    """Update a user."""
    user = (
        session.query(User)
        .filter(User.telegram_id == telegram_id)
        .filter_by(is_deleted=False)
        .first()
    )
    for key, value in user.model_dump().items():
        if hasattr(user, key):
            setattr(user, key, value)
    session.commit()
    return user


def delete_user(telegram_id: str):
    """Delete a user."""
    user = (
        session.query(User)
        .filter(User.telegram_id == telegram_id)
        .filter_by(is_deleted=False)
        .first()
    )
    user.is_deleted = True
    session.commit()
    return user
