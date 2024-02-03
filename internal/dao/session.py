import asyncio
from uuid import uuid4
from datetime import datetime

from app.models.session import Session
from db_connections import session as db_session


def create_session(telegram_id, token, data):
    """Create a session."""
    session = Session(telegram_id=telegram_id, token=token, data=data, id=uuid4())
    db_session.add(session)
    db_session.commit()
    return session


def get_session(token=None):
    """Get a session by telegram_id."""
    filter = Session.token == token
    session = (
        db_session.query(Session).filter(filter).filter_by(is_deleted=False).first()
    )
    return session


async def delete_session(token=None):
    """Delete a session by telegram_id."""
    filter = Session.token == token
    session = (
        db_session.query(Session).filter(filter).filter_by(is_deleted=False).first()
    )
    # actually delete session not just mark it as deleted
    db_session.delete(session)
    db_session.commit()
    return session


async def delete_expired_sessions():
    """Always run this function in background.
    It will delete all expired sessions
    """
    while True:
        await asyncio.sleep(60 * 60 * 24)
        sessions = (
            db_session.query(Session).filter(Session.expired_at < datetime.now()).all()
        )
        # actually delete sessions not just mark them as deleted
        for session in sessions:
            db_session.delete(session)
        db_session.commit()
