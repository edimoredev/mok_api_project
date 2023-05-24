# importamos las librerias necesarias para flask
from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.services.supplier_service import SupplierService

product_controller = Blueprint('product_controller', __name__)
product_service = ProductService()
supplier_service = SupplierService()


@product_controller.route('/products', methods=['GET'])
def get_all_products():
    products = product_service.get_all_products()
    if not products:
        return jsonify({'message': 'No products found'}), 404
    return jsonify({'products': [product.serialize() for product in products]}), 200
    # page = request.args.get('page', default=1, type=int)
    # per_page = request.args.get('per_page', default=3, type=int)

    # products, total_products = product_service.get_all_products(page, per_page)

    # if not products:
    #     return jsonify({'message': 'No users found'}), 404

    # response = {
    #     'page': page,
    #     'per_page': per_page,
    #     'total_pages': total_products // per_page + (1 if total_products % per_page != 0 else 0),
    #     'total_products': total_products,
    #     'products': [product.serialize() for product in products]
    # }

    # return jsonify(response), 200


@product_controller.route('/products', methods=['POST'])
def create_product():
    name = request.json.get('name')
    price = request.json.get('price')
    supplier_id = request.json.get('supplier_id')

    if not name or not price or not supplier_id:
        return jsonify({'message': 'Name, price, and supplier_id are required'}), 400

    # debería obtener el proveedor correspondiente según el supplier_id
    supplier_id = supplier_service.get_supplier_by_id(supplier_id)

    product = product_service.create_product(
        name, price, supplier_id)
    return jsonify({'product': product.serialize()}), 201


@product_controller.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product_by_id(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({'product': product.serialize()}), 200


@product_controller.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    name = request.json.get('name')
    price = request.json.get('price')

    if not name or not price:
        return jsonify({'message': 'Name and price are required'}), 400

    product = product_service.update_product(product_id, name, price)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({'product': product.serialize()}), 200


@product_controller.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = product_service.delete_product(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify({'product': product.serialize()}), 200
