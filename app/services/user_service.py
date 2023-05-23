# importamos el repositorio del usuario
from app.repositories.user_repository import UserRepository


class UserService:
    """ Clase usuario Servicio
    """

    def __init__(self):
        """ Función inicial donde instanciamos el repositorio del usuario
        """
        self.user_repository = UserRepository()

    def create_user(self, name, email):
        """ Funcion que crea un usuario y envia los datos al repositorio

        Args:
            name (string): Nombre de la preoveedora
            email (string): Direccion de la preoveedora

        Returns:
            user: retorna los datos del usuario creado
        """
        return self.user_repository.create_user(name, email)

    def get_user_by_id(self, user_id):
        """ Función que obtiene los datos dl usuario dependiendo el user_id a buscar y envia los datos al repositorio

        Args:
            user_id (integer): identificador unico para el usuario

        Returns:
            user: Retorna los datos del usuario buscado
        """
        return self.user_repository.get_user_by_id(user_id)

    def get_all_users(self):
        """Funcion que obtiene todos los usuarios y retorna los datos del repositorio

        Returns:
            user: Retorna todos los usuarios
        """
        return self.user_repository.get_all_users()

    def update_user(self, user_id, name, email):
        """ Función que actualiza el usuario por medio del user_id a buscar y envia los datos al repositorio

        Args:
            user_id (integer): id unico para el usuario
            name (string): nombre del usuario actualizado
            email (string): email del usuario actualizado

        Returns:
            user: Retorna los datos del usuario actualizado
        """
        return self.user_repository.update_user(user_id, name, email)

    def delete_user(self, user_id):
        """ Función que elimina el usuario buscado por el "user_id" desde el repositorio

        Args:
            user_id (integer): id unico para el usuario

        Returns:
            usuario: retornara los usuarios que esten disponibles
        """
        return self.user_repository.delete_user(user_id)
