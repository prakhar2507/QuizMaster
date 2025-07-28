from app import db
from datetime import datetime, timezone
from app.models.association_tables import grade_subject
from app.models.subjects import Subject

class Grade(db.Model):
    __tablename__ = 'grade'

    grade_id = db.Column(db.Integer, primary_key=True)
    grade_name = db.Column(db.String(60), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    subjects = db.relationship(
        'Subjects',
        secondary=grade_subject,
        back_populates='grade',
        passive_deletes=True
    )

    def __repr__(self):
        return f"<Grade {self.grade_name}>"
