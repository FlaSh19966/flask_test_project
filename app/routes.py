import os

from flask_login import current_user, login_user, logout_user, login_required
from flask import jsonify, request, make_response, Blueprint
from flask_restful import Resource
from .utils import aes_encrypt, aes_decrypt
from app import api
from . import db
from .models import User
from .tasks import process_csv_task

master_blueprint = Blueprint('master_blueprint', __name__)


class Register(Resource):
    def post(self):
        print('register user api')
        form_data = request.form
        username = form_data.get('username')
        email = form_data.get('email')
        password = form_data.get('password')
        password = password.encode('utf-8')
        encrypted_password = aes_encrypt(password)
        encrypted_password = encrypted_password.decode('utf-8')

        STORE_RESPONSE = User(
            username=username,
            email = email,
            password=encrypted_password
        )
        db.session.add(STORE_RESPONSE)
        db.session.commit()
        
        return make_response(jsonify({'Success': True}))


class Login(Resource):
    def post(self):
        print('register user api')
        form_data = request.form
        email = form_data.get('email')
        password = form_data.get('password')

        user = User.query.filter_by(email=email).first()
        encrypted_password = user.password
        decrypted_password = aes_decrypt(encrypted_password)
        if decrypted_password == password:
            login_user(user)
            return make_response(jsonify({'Success': True}))
        else:
            return make_response(jsonify({'Success': False, 'msg': "Invalid password or email"}))


class Logout(Resource):
    @login_required
    def post(self):
        print('logout user api')
        logout_user()
        return make_response(jsonify({'Success': True}))


class Upload(Resource):
    def post(self):
        if 'file' not in request.files:
            return make_response(jsonify({'Success': False, "error": "No file found"}))
        
        file = request.files['file']
        
        filepath = os.path.join('./uploads', 'companies_sorted.csv')
        file.save(filepath)
        
        process_csv_task.delay(filepath)

        return make_response(jsonify({'Upload': True,
                                    'Service': 'Flask Test'}))


class HealthCheck(Resource):
    def get(self):
        print('health-check hit portal')
        return make_response(jsonify({'Health-check': True,
                                      'Service': 'Flask Test'}))


api.add_resource(HealthCheck, '/')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Upload, '/upload')