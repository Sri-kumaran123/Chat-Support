from flask import jsonify, Blueprint, request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app import jwt, db
from flask_jwt_extended import create_access_token, create_refresh_token, set_refresh_cookies
from models.users import User

auth_bp = Blueprint("authentication", __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup_user():
    try:
        data = request.get_json() or {}

        # --- Input Validation ---
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')

        if not all([email, password, username]):
            return jsonify({
                "status": "failed",
                "message": "All fields (email, password, username) are required."
            }), 400

        # --- Check if User Exists ---
        if User.query.filter_by(email=email).first():
            return jsonify({
                "status": "failed",
                "message": "User already exists."
            }), 409

        # --- Create and Save User ---
        new_user = User(email=email, name=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        # --- Prepare Response Data ---
        user_data = {
            "id": new_user.id,
            "email": new_user.email,
            "username": new_user.name
        }
        return jsonify({
            "status": "success",
            "message": "User created successfully.",
            "user": user_data
        }), 201

    except IntegrityError as ie:
        db.session.rollback()
        return jsonify({
            "status": "error",
            "message": "Database integrity error. Possibly a duplicate entry.",
            "details": str(ie)
        }), 409

    except SQLAlchemyError as sqle:
        db.session.rollback()
        return jsonify({
            "status": "error",
            "message": "Database error occurred.",
            "details": str(sqle)
        }), 500

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred.",
            "details": str(e)
        }), 500


@auth_bp.route('/login', methods =  ['POST'])
def login_user():
    data = request.get_json() or {}
    email = data.get("email")
    password = data.get("password")

    user = User.filter_by_email(email)
    if not (user or user.check_password(password)):
        return jsonify({
            "status":"failed",
            "message":"Invalid Cretentials"
        }), 401
    
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))
    
    response = jsonify({
        "status": "success",
        "access_token": access_token,
        "user": {
            "id": user.id,
            "email": user.email
        }
    })

    # Set refresh token as HttpOnly cookie
    set_refresh_cookies(response, refresh_token, max_age=7*24*60*60)  # 7 days
    return response