from backend.app import db
from datetime import datetime, timezone
# from backend.models.attempts import Attempt
# from backend.models.questions import Question

class Response(db.Model):
    __tablename__ = 'responses'
    
    response_id = db.Column(db.Integer, primary_key=True)
    attempt_id = db.Column(db.Integer, db.ForeignKey('attempts.attempt_id', ondelete='CASCADE'), nullable=False, index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id', ondelete='CASCADE'), nullable=False, index=True)
    selected_answer = db.Column(db.String(300), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    
    submitted_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    question = db.relationship(
        'Question',
        back_populates='responses',
        passive_deletes=True
    )
    attempt = db.relationship('Attempt', backref='responses', passive_deletes=True)
    
    def __repr__(self):
        return f'<Response {self.response_id}>'