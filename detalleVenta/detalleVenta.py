class DetVenta:
    def __init__(self, idVenta, idProducto, precioUnitario, cantidad, idDetalle = None):
        self._idDetalle = idDetalle
        self._idVenta = idVenta
        self._idProducto = idProducto
        self._precioUnitario = precioUnitario
        self._cantidad = cantidad

#-------------------- Getters / Setters --------------------

    @property
    def idDetalle(self):
        return self._idDetalle

    @idDetalle.setter
    def idDetalle(self, idDetalle):
        self._idDetalle = idDetalle

    @property
    def idVenta(self):
        return self._idVenta

    @idVenta.setter
    def idVenta(self, idVenta):
        self._idVenta = idVenta

    @property
    def idProducto(self):
        return self._idProducto

    @idProducto.setter
    def idProducto(self, idProducto):
        self._idProducto = idProducto

    @property
    def precioUnitario(self):
        return self._precioUnitario

    @precioUnitario.setter
    def precioUnitario(self, precioUnitario):
        self._precioUnitario = precioUnitario

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

#-------------------- CRUD --------------------

    def agregar(self):
        pass

    def mostrar(self):
        pass

    def eliminar(self):
        pass

    def modificar(self):
        pass

    def calcularSubtotal(self):
        pass
