from backend import db
from datetime import datetime, timezone
from .users import User
from .quiz import Quiz
from .responses import Response

class Attempt(db.Model):
    __tablename__ = 'attempts'
    
    attempt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.quiz_id', ondelete='CASCADE'), nullable=False, index=True)
    
    started_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    ended_at = db.Column(db.DateTime, nullable=True)
    
    score = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(20), default='in_progress')

    user = db.relationship(
        'User',
        backref='attempts',
        passive_deletes=True
    )
    quiz = db.relationship(
        'Quiz',
        backref='attempts',
        passive_deletes=True
    )
    responses = db.relationship(
        'Response',
        back_populates='attempt',
        cascade='all, delete',
        passive_deletes=True
    )
    
    def __repr__(self):
        return f"<Attempt id={self.attempt_id} user={self.user_id} quiz={self.quiz_id} status={self.status}>"