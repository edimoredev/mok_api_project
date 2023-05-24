from flask import Flask
# _importa el adaptador de la base de datos en este caso es "db"_
from app.adapters.database import db
# _importar controladores
from app.controllers.user_controller import user_controller
from app.controllers.supplier_controller import supplier_controller
from app.controllers.product_controller import product_controller
from app.controllers.customer_controller import customer_controller

# _Inicializamos el metodo flask_
app = Flask(__name__)

# _Traer los datos suministrados desde el config, donde se encuentra la base de datos_
app.config.from_pyfile('config.py')

# _inicializamos la app
db.init_app(app)

# _realizar registro blueprint de los controladores
app.register_blueprint(user_controller)
app.register_blueprint(supplier_controller)
app.register_blueprint(product_controller)
app.register_blueprint(customer_controller)


if __name__ == '__main__':
    with app.app_context():
        # _creamos todos los modelos alchemy_
        db.create_all()
    # _arranque de la aplicación_
    app.run()
