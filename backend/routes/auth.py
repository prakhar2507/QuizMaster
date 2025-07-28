from flask import Flask, request,jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash

class Login(Resource):
    def post(self):
        
        # Get data from request body
        data=request.get_json()
        
        email=data.get('email')
        password=data.get('password')
        
        
        # Check if email exists, if npt exists return 400 error
        if not email or not password:
            return {'message': 'Missing email or Incorrect Password'},400
        
        user=User.query.filter_by(email=email).first()