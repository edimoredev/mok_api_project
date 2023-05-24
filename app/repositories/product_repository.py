# importar db del adaptador
from app.adapters.database import db
# importar Product
from app.models.product import Product


class ProductRepository:
    """ Clase la product Repositorio
    """

    def create_product(self, name, price, supplier):
        """ Funcion que crea el producto

        Args:
            name (string): Nombre del producto
            price (float): Precio del producto

        Returns:
            product: retorna los datos del producto
        """
        product = Product(name, price, supplier)
        db.session.add(product)
        db.session.commit()
        return product

    def get_product_by_id(self, product_id):
        """ Función que obtiene los datos de los productos  dependiendo el id a buscar

        Args:
            product_id (integer): identificador unico para los productos

        Returns:
            product: Retorna los datos de los productos buscado
        """
        return Product.query.get(product_id)

    def get_all_products(self):
        """Funcion que obtiene todos los productos

        Returns:
            product: Retorna todos los productos
        """
        return Product.query.all()
        # return Product.query.paginate(page=page, per_page=per_page, error_out=False).items

    def get_total_products_count(self):
        """Funcion que cuenta cuantos productos tiene

        Returns:
            int: devuelte cuantos productos hay
        """
        return Product.query.count()

    def update_product(self, product_id, name, price):
        """ Función que actualiza los productos por medio del product_id a buscar

        Args:
            product_id (integer): id unico para los productos
            name (string): Nombre del producto
            price (float): Precio del producto


        Returns:
            product: Retorna los datos de los productos
        """
        product = self.get_product_by_id(product_id)
        if product:
            product.name = name
            product.price = price
            db.session.commit()
        return product

    def delete_product(self, product_id):
        """ Función que elimina el producto buscado por el "product_id"

        Args:
            product_id (integer): id unico para el producto

        Returns:
            product: retornara el producto eliminado que esten disponibles
        """
        product = self.get_product_by_id(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product

    def get_all_products_paginated(self, page, per_page):
        """Funcion donde pagina los datos

        Args:
            page (_type_): _description_
            per_page (_type_): _description_
        """
        Product.query.paginate(page=page, per_page=per_page)
