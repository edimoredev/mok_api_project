from app.adapters.database import db


class Supplier(db.Model):
    """_Clase Proveedoras_

    Args:
        id: _llave primaria Integer, contiene el numero identificador de la proveedora_
        name: _nombre del usuario, de tipo string_
        email: _correo del usuario, de tipo string_

    Returns:
        _dic_: _retorna un diccionario serializado de los campos id, name, address y telephone de la proveedora_
    """
    __tablename__ = 'suppliers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)

    def __init__(self, name, address, telephone):
        """_Funcion inicializador de variables que recibe por parametro name, address y telephone de pa proveedora_

        Args:
            name (string): _Nombre de la proveedora_
            address (string): _Direccion de la proveedora_
            telephone (string): _Telefono de la proveedora_
        """
        self.name = name
        self.address = address
        self.telephone = telephone

    def serialize(self):
        """_Funcion que serializa los datos de la proveedora_

        Returns:
            _dic_: _datos del la proveedora_
        """
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'telephone': self.telephone
        }
