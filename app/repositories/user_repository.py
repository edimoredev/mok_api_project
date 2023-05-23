from app.adapters.database import db
from app.models.user import User


class UserRepository:
    """ Clase usuario Repositorio
    """

    def create_user(self, name, email):
        """ Funcion que crea un usuario

        Args:
            name (string): Nombre de la preoveedora
            email (string): Direccion de la preoveedora

        Returns:
            user: retorna los datos del usuario creado
        """
        user = User(name, email)
        db.session.add(user)
        db.session.commit()
        return user

    def get_user_by_id(self, user_id):
        """ Función que obtiene los datos dl usuario dependiendo el user_id a buscar

        Args:
            user_id (integer): identificador unico para el usuario

        Returns:
            user: Retorna los datos del usuario buscado
        """
        return User.query.get(user_id)

    def get_all_users(self):
        """Funcion que obtiene todos los usuarios

        Returns:
            user: Retorna todos los usuarios
        """
        return User.query.all()

    def update_user(self, user_id, name, email):
        """ Función que actualiza el usuario por medio del user_id a buscar

        Args:
            user_id (integer): id unico para el usuario
            name (string): nombre del usuario actualizado
            email (string): email del usuario actualizado

        Returns:
            user: Retorna los datos del usuario actualizado
        """
        user = self.get_user_by_id(user_id)
        if user:
            user.name = name
            user.email = email
            db.session.commit()
        return user

    def delete_user(self, user_id):
        """ Función que elimina el usuario buscado por el "user_id"

        Args:
            user_id (integer): id unico para el usuario

        Returns:
            usuario: retornara los usuarios que esten disponibles
        """
        user = self.get_user_by_id(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user
