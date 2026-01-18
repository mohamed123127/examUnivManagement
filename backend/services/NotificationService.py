from sqlalchemy.orm import Session
from models.notification import Notification

# Insert notification
def create_notification(message: str, type: str | None, db: Session):
    notification = Notification(
        message=message,
        type=type
    )
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification


# Get all notifications
def get_all_notifications(db: Session):
    notifications = (
        db.query(Notification)
        .order_by(Notification.id.desc())
        .all()
    )

    return [
        {
            "id": n.id,
            "message": n.message,
            "type": n.type
        }
        for n in notifications
    ]
