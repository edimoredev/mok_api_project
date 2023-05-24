# importar db del adaptador
from app.adapters.database import db


class Product(db.Model):
    """ Clase Producto

    Args:
        id: llave primaria Integer, contiene el numero identificador del producto
        name: nombre del producto, de tipo string
        price: precio del producto, de tipo float

    Returns:
        dic : _retorna un diccionario serializado de los campos id, name, address y telephone de la proveedora_
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    supplier_id = db.Column(db.Integer, db.ForeignKey(
        'suppliers.id'), nullable=False)
    supplier = db.relationship(
        'Supplier', backref=db.backref('products', lazy=True))

    def __init__(self, name, price, supplier):
        """_summary_

        Args:
            name (string): Nombre del producto
            price (float): Precio del producto
            supplier (integer): relacion entre supplier y product
        """

        self.name = name
        self.price = price
        self.supplier = supplier

    def serialize(self):
        """_Funcion que serializa los datos del product_

        Returns:
            _dic_: _datos del product_
        """
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'supplier': self.supplier.serialize()
        }
