# importamos las librerias necesarias para flask
from flask import Blueprint, request, jsonify

# importamos el UserService
from app.services.user_service import UserService

# nombramos el controlador que es donde se vera en el main
user_controller = Blueprint('user_controller', __name__)
# nombramos el servicio a instanciar
user_service = UserService()


@user_controller.route('/users', methods=['GET'])
def get_all_users():
    """ Funcion que obtiene los usuarios por metodo GET

    Returns:
        users: retorna los datos de los usuarios serializado por json
    """
    users = user_service.get_all_users()
    if not users:
        return jsonify({'message': 'No users found'}), 404
    return jsonify({'users': [user.serialize() for user in users]}), 200


@user_controller.route('/users', methods=['POST'])
def create_user():
    """ Funcion que crea los usuarios por metodo POST

    Returns:
        message: mensaje en caso de que no se complete algun campo requerido
        user: retorna los datos de los usuarios serializado por json
    """
    name = request.json.get('name')
    email = request.json.get('email')

    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400

    user = user_service.create_user(name, email)
    return jsonify({'user': user.serialize()}), 201


@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """ funcion que obtiene la información del usuario buscado por user_id

    Args:
        user_id (integer): id unico para el usuario

    Returns:
        message: mensaje en caso de que no se encontro usuario
        user: retorna los datos del usuario buscado
    """
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'user': user.serialize()}), 200


@user_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """ Función que actualiza el usuario dependiendo del user_id

    Args:
        user_id (integer): id unico para el usuario

    Returns:
        message: mensaje en caso de que no se complete algun campo requerido
        user: retorna los datos de el usuario actualizado
    """
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
    """ Funcion que elimina el usuario depende del user_id

    Args:
        user_id (integer): id unico para el usuario

    Returns:
        message: mensaje del usuario no encontrada
        supplier: retorna los datos del usuario eliminado
    """
    user = user_service.delete_user(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'user': user.serialize()}), 200
