# This file makes the backend directory a Python package. from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api

# Initialize SQLAlchemy (no app yet)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'quiz-master'
    db.init_app(app)
    migrate.init_app(app, db)
    # Most permissive CORS setup for debugging
    CORS(app, origins="*", supports_credentials=True)
    # from models import (
    #     User,
    #     Subject,
    #     Chapter,
    #     Quiz,
    #     Question,
    #     Option,
    #     Attempt,
    #     Response,
    #     Grade,
    #     grade_subject,
    #     quiz_chapter,
    #     quiz_subject,
    #     quiz_question
    # )

    # Register Flask-RESTful resources
    from .apis.auth import Register, Login
    api = Api(app)
    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')

    return app 