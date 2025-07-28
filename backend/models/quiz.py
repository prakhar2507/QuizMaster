from app import db
from datetime import datetime, timezone
from app.models.association_tables import quiz_chapter, quiz_subject

class Quiz(db.Model):
    __tablename__ = 'quizzes'
    
    quiz_id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(200), nullable=False, unique=True)
    quiz_description = db.Column(db.String(1200))
    quiz_start_time = db.Column(db.DateTime, nullable=False)
    quiz_end_time = db.Column(db.DateTime, nullable=False)
    quiz_duration = db.Column(db.Integer, nullable=False)
    quiz_attempts = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    chapters = db.relationship(
        'Chapter',
        secondary=quiz_chapter,
        back_populates='quizzes',
        passive_deletes=True
    )
    subjects = db.relationship(
        'Subject',
        secondary=quiz_subject,
        back_populates='quizzes',
        passive_deletes=True
    )

    def __repr__(self):
        return f"<Quiz {self.quiz_name}>"