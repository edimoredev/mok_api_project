# importamos el repositorio de la proveedora
from app.repositories.supplier_repository import SupplierRepository


class SupplierService:
    """ Clase del servicio de la proveedora
    """

    def __init__(self):
        """ Función inicial donde instanciamos el repositorio de la proveedora
        """
        self.supplier_repository = SupplierRepository()

    def create_supplier(self, name, address, telephone):
        """ Funcion que crea la proveedora y envia los datos al repositorio

        Args:
            name (string): Nombre de la preoveedora
            address (string): Direccion de la preoveedora
            telephone (string): Telefono de la preoveedora

        Returns:
            supplier: retorna los datos de la proveedora
        """
        return self.supplier_repository.create_supplier(name, address, telephone)

    def get_supplier_by_id(self, supplier_id):
        """ Función que obtiene los datos de la proveedora dependiendo el id a buscar y envia los datos al repositorio

        Args:
            supplier_id (integer): identificador unico para la proveedora

        Returns:
            supplier: Retorna los datos de la proveedora buscado
        """
        return self.supplier_repository.get_supplier_by_id(supplier_id)

    def get_all_suppliers(self):
        """Funcion que obtiene todos las proveedoras y retorna los datos del repositorio

        Returns:
            supplier: Retorna todas las proveedoras
        """
        return self.supplier_repository.get_all_suppliers()

    def update_supplier(self, supplier_id, name, address, telephone):
        """ Función que actualiza la proveedora por medio del supplier_id a buscar y envia los datos al repositorio

        Args:
            supplier_id (integer): id unico para la proveedora
            name (string): nombre de la proveedora actualizado
            address (string): dirección de la proveedora actualizado
            telephone (string): telefono de la proveedora actualizado

        Returns:
            supplier: Retorna los datos de la proveedora actualizado
        """
        return self.supplier_repository.update_supplier(supplier_id, name, address, telephone)

    def delete_supplier(self, supplier_id):
        """ Función que elimina la proveedora buscado por el "supplier_id" desde el repositorio

        Args:
            supplier_id (integer): id unico para la proveedora

        Returns:
            supplier: retornara las proveedoras que esten disponibles
        """
        return self.supplier_repository.delete_supplier(supplier_id)
