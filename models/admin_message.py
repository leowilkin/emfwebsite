from datetime import datetime

from sqlalchemy.sql.functions import func

from main import db
from . import BaseModel

INITIAL_TOPICS = {
    "heralds",
    "admin",
    "public",
}


class AdminMessage(BaseModel):
    __tablename__ = "admin_message"
    __versioned__: dict = {}

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    show = db.Column(db.Boolean, nullable=False, default=False)

    end = db.Column(db.DateTime)

    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modified = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow
    )

    creator = db.relationship("User", backref="admin_messages")

    @property
    def is_visible(self):
        return self.show and (self.end is None or self.end > datetime.utcnow())

    @classmethod
    def get_visible_messages(cls):
        return [m for m in cls.get_all_for_topic("public") if m.is_visible]

    @classmethod
    def get_all(cls):
        return AdminMessage.query.order_by(AdminMessage.created).all()

    @classmethod
    def get_by_id(cls, id):
        return AdminMessage.query.get_or_404(id)

    @classmethod
    def get_all_for_topic(cls, topic):
        return AdminMessage.query.filter(
            AdminMessage.topic == topic,
            AdminMessage.end > datetime.utcnow(),
        ).all()

    @classmethod
    def get_topic_counts(cls):
        res = {k: 0 for k in INITIAL_TOPICS}
        res.update(
            dict(
                AdminMessage.query.with_entities(
                    AdminMessage.topic,
                    func.count(AdminMessage.id).label("message_count"),
                )
                .group_by(AdminMessage.topic)
                .order_by(AdminMessage.topic)
                .all()
            )
        )
        return res
