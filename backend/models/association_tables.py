from backend.app import db

grade_subject = db.Table('grade_subject',
    db.Column('grade_id', db.Integer, db.ForeignKey('grade.grade_id', ondelete='CASCADE'), primary_key=True),
    db.Column('subject_id', db.Integer, db.ForeignKey('subjects.subject_id', ondelete='CASCADE'), primary_key=True)
)

quiz_chapter = db.Table('quiz_chapter',
    db.Column('quiz_id', db.Integer, db.ForeignKey('quizzes.quiz_id', ondelete='CASCADE'), primary_key=True),
    db.Column('chapter_id', db.Integer, db.ForeignKey('chapters.chapter_id', ondelete='CASCADE'), primary_key=True)
)

quiz_subject = db.Table('quiz_subject',
    db.Column('quiz_id', db.Integer, db.ForeignKey('quizzes.quiz_id', ondelete='CASCADE'), primary_key=True),
    db.Column('subject_id', db.Integer, db.ForeignKey('subjects.subject_id', ondelete='CASCADE'), primary_key=True)
)

quiz_question = db.Table(
    'quiz_question',
    db.Column('quiz_id', db.Integer, db.ForeignKey('quizzes.quiz_id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('questions.question_id', ondelete='CASCADE'), primary_key=True)
)