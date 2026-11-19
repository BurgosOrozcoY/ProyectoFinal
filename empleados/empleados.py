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

    @staticmethod
    def buscar(nombre):
        try:
            cursor.execute("select * from empleado where nombre = %s", (nombre,))
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete from empleado where id = %s", (id,))
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def modificar(self):
        try:
            cursor.execute("update empleado set nombre = %s, puesto = %s where id = %s", (self._nombre, self._puesto, self._idEmpleado))
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False
