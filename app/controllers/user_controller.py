from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()


@user_controller.route('/users', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    if not users:
        return jsonify({'message': 'No users found'}), 404
    return jsonify({'users': [user.serialize() for user in users]}), 200


@user_controller.route('/users', methods=['POST'])
def create_user():
    name = request.json.get('name')
    email = request.json.get('email')

    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400

    user = user_service.create_user(name, email)
    return jsonify({'user': user.serialize()}), 201


@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'user': user.serialize()}), 200


@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    name = request.json.get('name')
    email = request.json.get('email')

    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400

    user = user_service.update_user(user_id, name, email)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'user': user.serialize()}), 200


@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = user_service.delete_user(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'user': user.serialize()}), 200
