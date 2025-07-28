from app import db
from datetime import datetime, timezone
from app.models.subjects import Subject

class Chapter(db.Model):
    __tablename__ = 'chapters'
    
    chapter_id = db.Column(db.Integer, primary_key=True)
    chapter_name = db.Column(db.String(150), nullable=False, unique=True)
    
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.subject_id', ondelete='CASCADE'), nullable=False)
    
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    
    subject = db.relationship(
        'Subject',
        back_populates='chapters'
    )
    
    questions = db.relationship(
        'Question',
        back_populates='chapter',
        cascade='all, delete-orphan',
        passive_deletes=True
    )
    