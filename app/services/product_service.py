# importamos el repositorio de los productos
from app.repositories.product_repository import ProductRepository


class ProductService:
    """ Clase prodcto Servicio
    """

    def __init__(self):
        """ Función inicial donde instanciamos el repositorio del producto
        """
        self.product_repository = ProductRepository()

    def create_product(self, name, price, supplier):
        """ Funcion que crea el producto y envia los datos al repositorio

        Args:
            name (string): Nombre del producto
            price (float): Precio del producto

        Returns:
            product: retorna los datos del producto
        """
        return self.product_repository.create_product(name, price, supplier)

    def get_product_by_id(self, product_id):
        """ Función que obtiene los datos de los productos y envia los datos al repositorio


        Args:
            product_id (integer): identificador unico para los productos

        Returns:
            product: Retorna los datos de los productos buscado
        """
        return self.product_repository.get_product_by_id(product_id)

    def get_all_products(self):
        """Funcion que obtiene todos los productos  y retorna los datos del repositorio

        Returns:
            product: Retorna todos los productos
            total_products: total de productos
        """
        return self.product_repository.get_all_products()

        # products = self.product_repository.get_all_products(page, per_page)
        # total_products = self.product_repository.get_total_products_count()
        # return products, total_products

    def update_product(self, product_id, name, price):
        """ Función que actualiza los productos por medio del product_id a buscar y envia los datos al repositorio

        Args:
            product_id (integer): id unico para los productos
            name (string): Nombre del producto
            price (float): Precio del producto


        Returns:
            product: Retorna los datos de los productos
        """
        return self.product_repository.update_product(product_id, name, price)

    def delete_product(self, product_id):
        """ Función que elimina el producto buscado por el "product_id" desde el repositorio

        Args:
            product_id (integer): id unico para el producto

        Returns:
            product: retornara el producto eliminado que esten disponibles
        """
        return self.product_repository.delete_product(product_id)
