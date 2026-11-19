from conexionDB import cursor, conexion

class Productos:
    def __init__(self, codigo, nombre, stock, minStock, precioCompra, precioVenta):
        self._codigo = codigo
        self._nombre = nombre
        self._stock = stock
        self._minStock = minStock
        self._precioCompra = precioCompra
        self._precioVenta = precioVenta

#-------------------- Getters / Setters --------------------

    @property
    def codigo(self):
        return self._codigo 

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        self._stock = stock

    @property
    def minStock(self):
        return self._minStock

    @minStock.setter
    def minStock(self, minStock):
        self._minStock = minStock

    @property
    def precioCompra(self):
        return self._precioCompra

    @precioCompra.setter
    def precioCompra(self, precioCompra):
        self._precioCompra = precioCompra

    @property
    def precioVenta(self):
        return self._precioVenta

    @precioVenta.setter
    def precioVenta(self, precioVenta):
        self._precioVenta = precioVenta

#-------------------- CRUD --------------------

    def agregar(self):
        try:
            cursor.execute("Insert into productos values(%s, %s, %s, %s, %s, %s)", (self._codigo, self._nombre, self._stock, self._minStock, self.precioCompra, self.precioVenta))
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False
    @staticmethod
    def mostrar():
        try:
            cursor.execute("select * from productos")
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def buscar(codigo):
        try:
            cursor.execute("select * from productos where id = %s", (codigo,))
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def eliminar(codigo):
        try:
            cursor.execute("delete from productos where id = %s", (codigo,))
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def modificar(self):
        try:
            cursor.execute("update productos set nombre = %s, stock = %s, stockMinimo = %s, precioCompra = %s, precioVenta = %s where id = %s", (self._nombre, self._stock, self._minStock, self._precioCompra, self._precioVenta, self._codigo))
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def verificarStock(self):
        pass