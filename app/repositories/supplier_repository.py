from app.adapters.database import db
from app.models.supplier import Supplier


class SupplierRepository:
    """ Clase la proveedora Repositorio
    """

    def create_supplier(self, name, address, telephone):
        """ Funcion que crea la proveedora

        Args:
            name (string): Nombre de la preoveedora
            address (string): Direccion de la preoveedora
            telephone (string): Telefono de la preoveedora

        Returns:
            supplier: retorna los datos de la proveedora
        """
        supplier = Supplier(name, address, telephone)
        db.session.add(supplier)
        db.session.commit()
        return supplier

    def get_supplier_by_id(self, supplier_id):
        """ Función que obtiene los datos de la proveedora dependiendo el id a buscar

        Args:
            supplier_id (integer): identificador unico para la proveedora

        Returns:
            supplier: Retorna los datos de la proveedora buscado
        """
        return Supplier.query.get(supplier_id)

    def get_all_suppliers(self):
        """Funcion que obtiene todos las proveedoras

        Returns:
            supplier: Retorna todas las proveedoras
        """
        return Supplier.query.all()

    def update_supplier(self, supplier_id, name, address, telephone):
        """ Función que actualiza la proveedora por medio del supplier_id a buscar

        Args:
            supplier_id (integer): id unico para la proveedora
            name (string): nombre de la proveedora actualizado
            address (string): dirección de la proveedora actualizado
            telephone (string): telefono de la proveedora actualizado

        Returns:
            supplier: Retorna los datos de la proveedora actualizado
        """
        supplier = self.get_supplier_by_id(supplier_id)
        if supplier:
            supplier.name = name
            supplier.address = address
            supplier.telephone = telephone
            db.session.commit()
        return supplier

    def delete_supplier(self, supplier_id):
        """ Función que elimina la proveedora buscado por el "supplier_id"

        Args:
            supplier_id (integer): id unico para la proveedora

        Returns:
            supplier: retornara las proveedoras que esten disponibles
        """
        supplier = self.get_supplier_by_id(supplier_id)
        if supplier:
            db.session.delete(supplier)
            db.session.commit()

        return supplier
