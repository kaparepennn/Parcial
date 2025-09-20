from services.libros_service import UsersService
from flask import Blueprint, request, jsonify
# Importamos Blueprint para modularizar rutas, 
# request para acceder a datos enviados por el cliente (JSON, params, etc.) 
# y jsonify para devolver respuestas en formato JSON.

from config.database import get_db_session

service = UsersService(get_db_session())

user_bp = Blueprint('users', __name__)

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'El nombre de usuario y la contraseña son obligatorios'}), 400
    user = service.login_user(username, password)
    if user:
        return jsonify({'id': user.id, 'username': user.username}), 200
    return jsonify({'error': 'Credenciales inválidas'}), 401

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = service.get_all_users()
    return jsonify([{'id': u.id, 'username': u.username} for u in users]), 200

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = service.get_user_by_id(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

@user_bp.route('/registry', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'El nombre de usuario y la contraseña son obligatorios'}), 400
    user = service.create_user(username, password)
    return jsonify({'id': user.id, 'username': user.username}), 201

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = service.update_user(user_id, username, password)
    if user:
        return jsonify({'id': user.id, 'username': user.username}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = service.delete_user(user_id)
    if user:
        return jsonify({'message': 'Usuario eliminado correctamente'}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404