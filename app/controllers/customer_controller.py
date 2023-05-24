# importamos las librerias necesarias para flask
from flask import Blueprint, request, jsonify

# importamos el CustomerService
from app.services.customer_service import CustomerService

# nombramos el controlador que es donde se vera en el main
customer_controller = Blueprint('customer_controller', __name__)
# nombramos el servicio a instanciar
customer_service = CustomerService()


@customer_controller.route('/customers', methods=['GET'])
def get_all_customers():
    """ Funcion que obtiene clientes por metodo GET

    Returns:
        customers: retorna los datos de clientes serializado por json
    """
    customers = customer_service.get_all_customers()
    if not customers:
        return jsonify({'message': 'No customers found'}), 404
    return jsonify({'customers': [customer.serialize() for customer in customers]}), 200


@customer_controller.route('/customers', methods=['POST'])
def create_customer():
    """ Funcion que crea clientes por metodo POST

    Returns:
        message: mensaje en caso de que no se complete algun campo requerido
        customer: retorna los datos de clientes serializado por json
    """
    name = request.json.get('name')
    email = request.json.get('email')

    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400

    customer = customer_service.create_customer(name, email)
    return jsonify({'customer': customer.serialize()}), 201


@customer_controller.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    """ funcion que obtiene la información del cliente buscado por customer_id

    Args:
        customer_id (integer): id unico para el cliente

    Returns:
        message: mensaje en caso de que no se encontro cliente
        customer: retorna los datos del cliente buscado
    """
    customer = customer_service.get_customer_by_id(customer_id)
    if not customer:
        return jsonify({'message': 'customer not found'}), 404
    return jsonify({'customer': customer.serialize()}), 200


@customer_controller.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """ Función que actualiza el cliente dependiendo del customer_id

    Args:
        customer_id (integer): id unico para el cliente

    Returns:
        message: mensaje en caso de que no se complete algun campo requerido
        customer: retorna los datos de el cliente actualizado
    """
    name = request.json.get('name')
    email = request.json.get('email')

    if not name or not email:
        return jsonify({'message': 'Name and email are required'}), 400

    customer = customer_service.update_customer(customer_id, name, email)
    if not customer:
        return jsonify({'message': 'customer not found'}), 404
    return jsonify({'customer': customer.serialize()}), 200


@customer_controller.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    """ Funcion que elimina el cliente depende del customer_id

    Args:
        customer_id (integer): id unico para el cliente

    Returns:
        message: mensaje del cliente no encontrada
        supplier: retorna los datos del cliente eliminado
    """
    customer = customer_service.delete_customer(customer_id)
    if not customer:
        return jsonify({'message': 'customer not found'}), 404
    return jsonify({'customer': customer.serialize()}), 200
