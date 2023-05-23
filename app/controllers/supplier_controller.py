# importamos las librerias necesarias para flask
from flask import Blueprint, request, jsonify

# importamos el SupplierService
from app.services.supplier_service import SupplierService

# nombramos el controlador que es donde se vera en el main
supplier_controller = Blueprint('supplier_controller', __name__)
# nombramos el servicio a instanciar
supplier_service = SupplierService()

# controlador GET donde se visualizan las proveedoras


@supplier_controller.route('/suppliers', methods=['GET'])
def get_all_suppliers():
    """ Funcion que obtiene las proveedoras por metodo GET

    Returns:
        message: mensaje en caso de que no se encontro proveedora
        suppliers: retorna los datos de las proveedoras serializado por json
    """
    suppliers = supplier_service.get_all_suppliers()
    if not suppliers:
        return jsonify({'message': 'No suppliers found'}), 404
    return jsonify({'suppliers': [supplier.serialize() for supplier in suppliers]}), 200


@supplier_controller.route('/suppliers', methods=['POST'])
def create_supplier():
    """ Funcion que crea la proveedora por metodo POST

    Returns:
        message: mensaje en caso de que no se complete algun campo requerido
        supplier: retorna los datos de las proveedoras serializado por json
    """
    name = request.json.get('name')
    address = request.json.get('address')
    telephone = request.json.get('telephone')

    if not name or not address or not telephone:
        return jsonify({'message': 'Name, address and telephone are required'}), 400

    supplier = supplier_service.create_supplier(name, address, telephone)
    return jsonify({'supplier': supplier.serialize()}), 201


@supplier_controller.route('/suppliers/<int:supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    """ funcion que obtiene la información de la proveedora buscado por supplier_id

    Args:
        supplier_id (integer): id unico para la proveedora

    Returns:
        message: mensaje en caso de que no se encontro proveedora
        supplier: retorna los datos de la proveedora buscada
    """
    supplier = supplier_service.get_supplier_by_id(supplier_id)
    if not supplier:
        return jsonify({'message': 'supplier not found'}), 404
    return jsonify({'supplier': supplier.serialize()}), 200


@supplier_controller.route('/suppliers/<int:supplier_id>', methods=['PUT'])
def update_supplier(supplier_id):
    """ Función que actualiza la proveedora dependiendo del supplier_id

    Args:
        supplier_id (integer): id unico para la proveedora

    Returns:
        message: mensaje en caso de que no se complete algun campo requerido
        supplier: retorna los datos de la proveedora actualizada
    """
    name = request.json.get('name')
    address = request.json.get('address')
    telephone = request.json.get('telephone')

    if not name or not address or not telephone:
        return jsonify({'message': 'Name, address and telephone are required'}), 400

    supplier = supplier_service.update_supplier(
        supplier_id,  name, address, telephone)
    if not supplier:
        return jsonify({'message': 'supplier not found'}), 404
    return jsonify({'supplier': supplier.serialize()}), 200


@supplier_controller.route('/suppliers/<int:supplier_id>', methods=['DELETE'])
def delete_supplier(supplier_id):
    """ Funcion que elimina la proveedora depende del supplier_id

    Args:
        supplier_id (integer): id unico para la proveedora

    Returns:
        message: mensaje de la proveedora no encontrada
        supplier: retorna los datos de la proveedora eliminada
    """
    supplier = supplier_service.delete_supplier(supplier_id)
    if not supplier:
        return jsonify({'message': 'Supplier not found'}), 404
    return jsonify({'supplier': supplier.serialize()}), 200
