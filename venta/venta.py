class Venta:
    def __init__(self, fecha, total, idVenta=None):
        self._idVenta = idVenta
        self._fecha = fecha
        self._total = total

#-------------------- Getters / Setters --------------------

    @property
    def idVenta(self):
        return self._idVenta

    @idVenta.setter
    def idVenta(self, idVenta):
        self._idVenta = idVenta
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

#-------------------- CRUD --------------------

    def registrar(self):
        pass

    def mostrar(self):
        pass

    def eliminar(self):
        pass

    def modificar(self):
        pass

    def calcularTotal(self):
        pass

    def generarTicket(self):
        pass
