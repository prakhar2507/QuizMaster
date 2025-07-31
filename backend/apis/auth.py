from flask_restful import Resource
from flask import request, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
from backend import db
from models import User
from datetime import datetime
from itsdangerous import URLSafeTimedSerializer

# --- Helper functions ---
def create_reset_token(user_id):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    return serializer.dumps(user_id, salt="password-reset-salt")

def decode_reset_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    try:
        user_id = serializer.loads(token, salt="password-reset-salt", max_age=expiration)
        return user_id
    except Exception:
        return None

# --- Resources ---
class Register(Resource):
    def post(self):
        data = request.get_json()
        full_name = data.get("full_name")
        email = data.get("email")
        dob = data.get("dob")
        qualification = data.get("qualification")
        role = data.get("role", "user")
        password = data.get("password")
        mobile_no = data.get("mobile_no")

        if not all([full_name, email, dob, qualification, password]):
            return {"message": "Missing required fields"}, 400

        if User.query.filter_by(email=email).first():
            return {"message": "User already exists"}, 409

        try:
            dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
        except Exception:
            return {"message": "Invalid date format for dob. Use YYYY-MM-DD."}, 400

        user = User(
            full_name=full_name,
            email=email,
            dob=dob_date,
            qualification=qualification,
            role=role,
            mobile_no=mobile_no
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return {"message": "User registered successfully!"}, 201

    def options(self):
        return {}, 200

class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        if not email or not password:
            return {"message": "Missing email or password"}, 400
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return {"message": "Invalid credentials"}, 401
        claims = {"role": user.role}
        access_token = create_access_token(identity=user.user_id, additional_claims=claims)
        refresh_token = create_refresh_token(identity=user.user_id, additional_claims=claims)
        user.last_login = datetime.utcnow()
        db.session.commit()
        return {
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": {
                "user_id": user.user_id,
                "email": user.email,
                "full_name": user.full_name,
                "role": user.role
            }
        }, 200

    def options(self):
        return {}, 200
