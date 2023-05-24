# importar db del adaptador
from app.adapters.database import db


class Customer(db.Model):
    """clase Customer

    Args:
        id: llave primaria Integer, contiene el numero identificador del customer
        name: nombre del customer, de tipo string
        email: precio del customer, de tipo string

    Returns:
        dic : _retorna un diccionario serializado de los campos id, name, email del customer
    """
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email):
        """_summary_

        Args:
            name (string): Nombre del customer
            email (string): Precio del customer
        """
        self.name = name
        self.email = email

    def serialize(self):
        """ Funcion que serializa los datos del customer

        Returns:
            _dic_: _datos del customer
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
