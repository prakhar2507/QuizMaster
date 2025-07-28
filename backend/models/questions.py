from app import db
from datetime import datetime, timezone
from app.models.chapters import Chapter

class Question(db.Model):
    __tablename__ = 'questions'
    
    question_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(600), nullable=False, unique=True)
    difficulty_level = db.Column(db.Integer, nullable=False)
    weightage = db.Column(db.Integer, nullable=False, default=5)
    correct_answer = db.Column(db.String(300), nullable=False)
    
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.chapter_id', ondelete='CASCADE'), nullable=False)
    
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    chapter = db.relationship(
        'Chapter',
        back_populates='questions',
        passive_deletes=True
    )
    options = db.relationship(
        'Option',
        back_populates='question',
        cascade='all, delete-orphan',
        passive_deletes=True
    )
    
    def __repr__(self):
        return f"<Question {self.question_text[:30]}...>"