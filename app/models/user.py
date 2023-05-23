from app.adapters.database import db


class User(db.Model):
    """_Clase Usuario_

    Args:
        id: _llave primaria Integer, contiene el numero identificador del usuario_
        name: _nombre del usuario, de tipo string_
        email: _correo del usuario, de tipo string_

    Returns:
        _dic_: _retorna un diccionario serializado de los campos id, name y email del usuario_
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email):
        """_Funcion inicializador de variables que recibe por parametro el name y email del usuario_

        Args:
            name (string): _Nombre del usuario_
            email (string): _Email del usuario_
        """
        self.name = name
        self.email = email

    def serialize(self):
        """_Funcion que serializa los datos del usuario_

        Returns:
            _dic_: _datos del usuario_
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
