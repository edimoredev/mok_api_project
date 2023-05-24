# importar db del adaptador
from app.adapters.database import db
# importar Product
from app.models.customer import Customer


class CustomerRepository:
    """ Clase Customer Repositorio
    """

    def create_customer(self, name, email):
        """ Funcion que crea un cliente

        Args:
            name (string): Nombre del cliente
            email (string): Direccion del cliente

        Returns:
            customer: retorna los datos del cliente creado
        """
        customer = Customer(name, email)
        db.session.add(customer)
        db.session.commit()
        return customer

    def get_customer_by_id(self, customer_id):
        """ Función que obtiene los datos del cliente dependiendo el customer_id a buscar

        Args:
            customer_id (integer): identificador unico para el cliente

        Returns:
            customer: Retorna los datos del cliente buscado
        """
        return Customer.query.get(customer_id)

    def get_all_customers(self):
        """Funcion que obtiene todos los clientes

        Returns:
            customer: Retorna todos los clientes
        """
        return Customer.query.all()

    def update_customer(self, customer_id, name, email):
        """ Función que actualiza el cliente por medio del customer_id a buscar

        Args:
            customer_id (integer): id unico para el cliente
            name (string): nombre del cliente actualizado
            email (string): email del cliente actualizado

        Returns:
            customer: Retorna los datos del cliente actualizado
        """
        customer = self.get_customer_by_id(customer_id)
        if customer:
            customer.name = name
            customer.email = email
            db.session.commit()
        return customer

    def delete_customer(self, customer_id):
        """ Función que elimina el cliente buscado por el "customer_id"

        Args:
            customer_id (integer): id unico para el cliente

        Returns:
            customer: retornara el cliente eliminado
        """
        customer = self.get_customer_by_id(customer_id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
        return customer
