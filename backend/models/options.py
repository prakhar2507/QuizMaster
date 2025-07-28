from app import db
from datetime import datetime, timezone
from app.models.questions import Question

class Option(db.Model):
    __tablename__ = 'options'
    
    option_id = db.Column(db.Integer, primary_key=True)
    options_text = db.Column(db.String(300), nullable=False)
    
    question_id = db.Column(db.Integer, db.Foreignkey('questions.question_id', ondelete='CASCADE'), nullable=False)
    
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    question = db.relationship(
        'Question',
        back_populates='options',
        passive_deletes=True
    )
    
    def __repr__(self):
        return f"<Option {self.option_text[:30]}...>"