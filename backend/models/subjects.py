from app import db
from datetime import datetime, timezone
from backend.models.association_tables import grade_subject, quiz_subject
from backend.models.grade import Grade

class Subject(db.Model):
    __tablename__ = 'subjects'

    subject_id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(60), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    grades = db.relationship(
        'Grade',
        secondary=grade_subject,
        back_populates='subjects',
        passive_deletes=True
    )
    chapters = db.relationship(
        'Chapter',
        back_populates='subject',
        cascade='all, delete',
        passive_deletes=True)
    quizzes = db.relationship(
        'Quiz',
        secondary=quiz_subject,
        back_populates='subjects',
        passive_deletes=True
    )


    def __repr__(self):
        return f"<Subject {self.subject_name}>"
