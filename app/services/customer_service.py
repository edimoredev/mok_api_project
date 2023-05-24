# importamos el repositorio del customer
from app.repositories.customer_repository import CustomerRepository


class CustomerService:
    """ Clase customer Servicio
    """

    def __init__(self):
        """ Función inicial donde instanciamos el repositorio del cliente
        """
        self.customer_repository = CustomerRepository()

    def create_customer(self, name, email):
        """ Funcion que crea un cliente y envia los datos al repositorio

        Args:
            name (string): Nombre del cliente
            email (string): Direccion del cliente

        Returns:
            customer: retorna los datos del cliente creado
        """
        return self.customer_repository.create_customer(name, email)

    def get_customer_by_id(self, customer_id):
        """ Función que obtiene los datos dl cliente dependiendo el customer_id a buscar y envia los datos al repositorio

        Args:
            customer_id (integer): identificador unico para el cliente

        Returns:
            customer: Retorna los datos del cliente buscado
        """
        return self.customer_repository.get_customer_by_id(customer_id)

    def get_all_customers(self):
        """Funcion que obtiene todos los clientes y retorna los datos del repositorio

        Returns:
            customer: Retorna todos los clientes
        """
        return self.customer_repository.get_all_customers()

    def update_customer(self, customer_id, name, email):
        """ Función que actualiza el cliente por medio del customer_id a buscar y envia los datos al repositorio

        Args:
            customer_id (integer): id unico para el cliente
            name (string): nombre del cliente actualizado
            email (string): email del cliente actualizado

        Returns:
            customer: Retorna los datos del cliente actualizado
        """
        return self.customer_repository.update_customer(customer_id, name, email)

    def delete_customer(self, customer_id):
        """ Función que elimina el cliente buscado por el "customer_id" desde el repositorio

        Args:
            customer_id (integer): id unico para el cliente

        Returns:
            customer: retornara los clientes que esten disponibles
        """
        return self.customer_repository.delete_customer(customer_id)
