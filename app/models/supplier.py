# importar db del adaptador
from app.adapters.database import db


class Supplier(db.Model):
    """ Clase Supplier

    Args:
        id:  llave primaria Integer, contiene el numero identificador de la proveedora 
        name:  nombre de la proveedora, de tipo string 
        email:  correo de la proveedora, de tipo string 

    Returns:
        dic: retorna un diccionario serializado de los campos id, name, address y telephone de la proveedora
    """
    __tablename__ = 'suppliers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)

    def __init__(self, name, address, telephone):
        """ Funcion inicializador de variables que recibe por parametro name, address y telephone de pa proveedora_

        Args:
            name (string): Nombre de la proveedora
            address (string): Direccion de la proveedora
            telephone (string): Telefono de la proveedora
        """
        self.name = name
        self.address = address
        self.telephone = telephone

    def serialize(self):
        """Funcion que serializa los datos de la proveedora

        Returns:
            dic: datos del la proveedora
        """
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'telephone': self.telephone
        }
