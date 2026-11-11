from conexionDB import conexion, cursor

class Empleados:
    def __init__(self, nombre, puesto, idEmpleado = None):
        self._idEmpleado = idEmpleado
        self._nombre = nombre
        self._puesto = puesto

#-------------------- Getters / Setters --------------------

    @property
    def idEmpleado(self):
        return self._idEmpleado

    @idEmpleado.setter
    def idEmpleado(self, idEmpleado):
        self._idEmpleado = idEmpleado

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def puesto(self):
        return self._puesto

    @puesto.setter
    def puesto(self, puesto):
        self._puesto = puesto

#-------------------- CRUD --------------------

    def agregar(self):
        try:
            cursor.execute("Insert into empleado values(NULL, %s, %s)", (self._nombre, self._puesto))
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def mostrar():
        try:
            cursor.execute("select * from empleado")
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def buscar(self):
        pass

    def eliminar(self):
        pass

    def modificar(self):
        pass
