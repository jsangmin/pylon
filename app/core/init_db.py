from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import get_password_hash
from app.core.database import SessionLocal
import logging

logger = logging.getLogger(__name__)

def init_db() -> None:
    """
    Initialize database with default users (user1 to user10).
    This function is called on application startup.
    """
    db: Session = SessionLocal()
    try:
        # Check if users already exist
        existing_users = db.query(User).filter(
            User.email.in_([f"user{i}@example.com" for i in range(1, 11)])
        ).count()
        
        if existing_users > 0:
            logger.info(f"Database already initialized with {existing_users} users. Skipping initialization.")
            return
        
        # Create user1 to user10
        users_to_create = []
        for i in range(1, 11):
            user = User(
                email=f"user{i}@example.com",
                hashed_password=get_password_hash(f"password{i}"),
                name=f"User {i}",
                is_active=True
            )
            users_to_create.append(user)
        
        # Add all users to the session
        db.add_all(users_to_create)
        db.commit()
        
        logger.info("Successfully created 10 initial users (user1 to user10)")
        
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()
