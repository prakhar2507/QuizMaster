from backend import db
from datetime import datetime, timezone
from .association_tables import grade_subject

class Grade(db.Model):
    __tablename__ = 'grade'

    grade_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    grade_name = db.Column(db.String(60), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    subjects = db.relationship(
        'Subject',
        secondary=grade_subject,
        back_populates='grades',
        passive_deletes=True
    )

    def __repr__(self):
        return f"<Grade {self.grade_name}>"
