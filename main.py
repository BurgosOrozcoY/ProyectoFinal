from empleados import empleados
from productos import productos
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Pre-alpha 0.4.3")
        self.ventana.geometry("800x600")
        self.ventana.resizable(True,True)
        self.main()

    def clear(self):
        for witget in self.ventana.winfo_children():
            witget.destroy()

    def definir_puesto(self, puesto):
        self.puestoSeleccionado = puesto

    def menu_acciones(self, tipo):
        self.clear()
        Label(self.ventana, text = f"\n...::: Menú de {tipo} :::...").pack(pady=10)
        Button(self.ventana, text = "Agregar", command = lambda: self.insertar_view(tipo)).pack(pady=5)
        Button(self.ventana, text = "Mostrar", command = lambda: self.mostrar_view(tipo)).pack(pady=5)
        Button(self.ventana, text = "Buscar", command = lambda: self.buscar_view(tipo)).pack(pady=5)
        Button(self.ventana, text = "Eliminar", command = lambda: self.eliminar_view(tipo)).pack(pady=5)
        Button(self.ventana, text = "Modificar", command = lambda: self.modificar_view(tipo)).pack(pady=5)
        if tipo == "Productos":
            Button(self.ventana, text = "Verificar stock", command = "").pack(pady=5)
        elif tipo == "Ventas":
            Button(self.ventana, text = "Calcular total", command = "").pack(pady=5)
            Button(self.ventana, text = "Generar ticket", command = "").pack(pady=5)
        Button(self.ventana, text = "Regresar", command = self.main).pack(pady=30)

    def insertar_view(self, tipo):
        self.clear()
        if tipo == "Empleados":
            Label(self.ventana, text = "...Ingresar los datos del empleado...").pack(pady = 10)
            Label(self.ventana, text = "Nombre:").pack(pady = 5)
            self.nombre = Entry(self.ventana)
            self.nombre.focus()
            self.nombre.pack(pady = 5)
            self.puestoSeleccionado = ""
            Label(self.ventana, text = "Seleccionar puesto:").pack(pady=10)
            Button(self.ventana, text="Administrador", command= lambda: self.definir_puesto("Admin")).pack(pady=10)
            Button(self.ventana, text="Empleado", command= lambda: self.definir_puesto("Empleado")).pack(pady=10)
            Button(self.ventana, text = "Guardar", command = lambda: self.insertar_controller(tipo, self.puestoSeleccionado)).pack(pady = 10)
            Button(self.ventana, text = "Regresar", command = lambda: self.menu_acciones(tipo)).pack(pady = 10)
        elif tipo == "Productos":
            Label(self.ventana, text = "...Ingresar los datos del producto...").pack(pady = 10)
            Label(self.ventana, text= "Codigo:").pack(pady = 5)
            self.codigo = Entry(self.ventana)
            self.codigo.focus()
            self.codigo.pack(pady = 5)
            Label(self.ventana, text= "Nombre del producto:").pack(pady = 5)
            self.nombre = Entry(self.ventana)
            self.nombre.pack(pady = 5)
            Label(self.ventana, text= "Stock actual:").pack(pady = 5)
            self.stock = Entry(self.ventana)
            self.stock.pack(pady = 5)
            Label(self.ventana, text= "Stock minimo:").pack(pady = 5)
            self.minStock = Entry(self.ventana)
            self.minStock.pack(pady = 5)
            Label(self.ventana, text= "Precio de compra:").pack(pady = 5)
            self.precioCompra = Entry(self.ventana)
            self.precioCompra.pack(pady = 5)
            Label(self.ventana, text= "Precio de venta:").pack(pady = 5)
            self.precioVenta = Entry(self.ventana)
            self.precioVenta.pack(pady = 5)
            Button(self.ventana, text = "Guardar", command = lambda: self.insertar_controller(tipo)).pack(pady = 10)
            Button(self.ventana, text = "Regresar", command = lambda: self.menu_acciones(tipo)).pack(pady = 5)

    def mostrar_view(self, tipo):
        self.clear()
        Label(self.ventana, text=f"...Consultar {tipo}...").pack(pady=10)
        filas = ""
        filas = self.mostrar_controller(filas, tipo)
        Label(self.ventana, text=f"{filas}").pack(pady=5)
        Button(self.ventana, text= "Regresar", command= lambda: self.menu_acciones(tipo)).pack(pady=5)

    def buscar_view(self, tipo):
        self.clear()
        if tipo == "Empleados":
            Label(self.ventana, text = "...Buscar empleado...").pack(pady = 10)
            Label(self.ventana, text = "Nombre del empleado:").pack(pady = 5)
            self.nombre = Entry(self.ventana)
            self.nombre.focus()
            self.nombre.pack(pady = 5)
            self.BtnBuscar = Button(self.ventana, text = "Buscar", command = lambda: self.buscar_controller(tipo))
            self.BtnBuscar.pack(pady = 10)
            Button(self.ventana, text = "Regresar", command = lambda: self.menu_acciones(tipo)).pack(pady = 10)

    def eliminar_view(self, tipo):
        self.clear()
        if tipo == "Empleados":
            Label(self.ventana, text = "...Eliminar empleado...").pack(pady = 10)
            Label(self.ventana, text = "ID del empleado:").pack(pady = 5)
            self.idEmpleado = Entry(self.ventana)
            self.idEmpleado.focus()
            self.idEmpleado.pack(pady = 5)
            Button(self.ventana, text = "Eliminar", command = lambda: self.eliminar_controller(tipo)).pack(pady = 10)
            Button(self.ventana, text = "Regresar", command = lambda: self.menu_acciones(tipo)).pack(pady = 10)

    def modificar_view(self, tipo):
        self.clear()
        if tipo == "Empleados":
            Label(self.ventana, text = "...Modificar datos del empleado...").pack(pady = 10)
            Label(self.ventana, text = "ID del empleado:").pack(pady = 5)
            self.idEmpleado = Entry(self.ventana)
            self.idEmpleado.focus()
            self.idEmpleado.pack(pady = 5)
            Label(self.ventana, text = "Nuevo nombre:").pack(pady = 5)
            self.nombre = Entry(self.ventana)
            self.nombre.pack(pady = 5)
            Label(self.ventana, text = "Nuevo puesto:").pack(pady=10)
            self.puestoSeleccionado = ""
            Button(self.ventana, text="Administrador", command= lambda: self.definir_puesto("Admin")).pack(pady = 10)
            Button(self.ventana, text="Empleado", command= lambda: self.definir_puesto("Empleado")).pack(pady = 10)
            Button(self.ventana, text = "Guardar cambios", command = lambda: self.modificar_controller(tipo)).pack(pady = 10)
            Button(self.ventana, text = "Regresar", command = lambda: self.menu_acciones(tipo)).pack(pady = 10)

    #CONTROLADOR

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...", message="...Accion realizada con exito...")
        else:
            messagebox.showerror(title="... Verifica por favor ...", message="...Esta accion no puede realizarse...")

    def insertar_controller(self, tipo, cargo = None):
        if tipo == "Empleados":
            if self.puestoSeleccionado != "":
                if self.nombre.get() == "":
                    messagebox.showerror(title= "Error", message= "El nombre no puede estar vacío.")
                else:
                    if cargo == "Empleado":
                        confirmar = messagebox.askquestion(title= "Confirmar empleado", message= f"¿Desea registrar a {self.nombre.get()} como empleado?")
                    elif cargo == "Admin":
                        confirmar = messagebox.askquestion(title= "Confirmar empleado", message= f"¿Desea registrar a {self.nombre.get()} como administrador?")
                    if confirmar == "yes":
                        cargo = self.puestoSeleccionado
                        empleado = empleados.Empleados(self.nombre.get(), cargo)
                        respuesta = empleado.agregar()
                        self.respuesta_sql(respuesta)
                        del empleado
            else:
                messagebox.showerror(title="Error", message= "¡No se ha seleccionado un puesto!")
        elif tipo == "Productos":
            if self.codigo.get() != "" and self.nombre.get() != "" and self.stock.get() != "" and self.minStock.get() != "" and self.precioCompra.get() != "" and self.precioVenta.get() != "":
                producto = productos.Productos(self.codigo.get(), self.nombre.get(), self.stock.get(), self.minStock.get(), self.precioCompra.get(), self.precioVenta.get())
                respuesta = producto.agregar()
                self.respuesta_sql(respuesta)
                del producto
            else:
                messagebox.showerror(title="Error", message="Datos incompletos")

    def mostrar_controller(self, filas, tipo):
        if tipo == "Empleados":
            registros = empleados.Empleados.mostrar()
        elif tipo == "Productos":
            registros = productos.Productos.mostrar()
        if len(registros) > 0:
            num_categoria = 1
            for fila in registros:
                if tipo == "Empleados":
                    filas = filas + (f"Empleado # {num_categoria}\nID: {fila[0]}\nNombre: {fila[1]}\nPuesto: {fila[2]}")
                elif tipo == "Productos":
                    filas = filas + (f"Producto # {num_categoria}\nCódigo: {fila[0]}\nProducto: {fila[1]}\nStock: {fila[2]}")
                num_categoria += 1
        else:
            filas = ("\n\n\t NO existen datos que mostrar por el momento")
        return filas

    def eliminar_controller(self, tipo):
        if tipo == "Empleados":
            if self.idEmpleado.get() != "":
                id = self.idEmpleado.get()
                confirmar = messagebox.askquestion(title= "Confirmar eliminación", message= f"¿Desea eliminar al empleado con ID {id}?")
                if confirmar == "yes":
                    respuesta = empleados.Empleados.eliminar(id)
                    self.respuesta_sql(respuesta)
            else:
                messagebox.showerror(title="Error", message="¡No se ha ingresado un ID!")

    def buscar_controller(self, tipo):
        if tipo == "Empleados":
            if self.nombre.get() != "":
                nombre = self.nombre.get()
                registros = empleados.Empleados.buscar(nombre)
                filas = ""
                if len(registros) > 0:
                    for fila in registros:
                        filas = filas + (f"ID: {fila[0]}\nNombre: {fila[1]}\nPuesto: {fila[2]}")
                    self.clear()
                    Label(self.ventana, text = f"Resultado de la búsqueda:\n{filas}").pack(pady = 10)
                    Button(self.ventana, text = "Regresar", command = lambda: self.buscar_view(tipo)).pack(pady = 10)
                else:
                    messagebox.showerror(title="Error", message="¡No se encontraron resultados!")
            else:
                messagebox.showerror(title="Error", message="¡No se ha ingresado un nombre!")

    def modificar_controller(self, tipo):
        if tipo == "Empleados":
            if self.idEmpleado.get() != "" and self.nombre.get() != "" and self.puestoSeleccionado != "":
                id = self.idEmpleado.get()
                nombre = self.nombre.get()
                puesto = self.puestoSeleccionado
                confirmar = messagebox.askquestion(title= "Confirmar modificación", message= f"¿Desea modificar al empleado con ID {id}?")
                if confirmar == "yes":
                    empleado = empleados.Empleados(nombre, puesto, id)
                    respuesta = empleado.modificar()
                    self.respuesta_sql(respuesta)
                    del empleado
            elif self.puestoSeleccionado == "":
                messagebox.showerror(title="Error", message="¡No se ha seleccionado un puesto!")
            else:
                messagebox.showerror(title="Error", message="¡No se han ingresado todos los datos!")

    def main(self):
        self.clear()
        Label(self.ventana, text = "\n...::: M E N U  P R I N C I P A L :::...").pack(pady=10)
        Button(self.ventana, text = "Inventario", command = lambda: self.menu_acciones("Productos")).pack(pady=5)
        Button(self.ventana, text = "Empleados", command = lambda: self.menu_acciones("Empleados")).pack(pady=5)
        Button(self.ventana, text = "Ventas", command = lambda: self.menu_acciones("Ventas")).pack(pady=5)
        Button(self.ventana, text = "Salir", command = self.ventana.quit).pack(pady=5)

if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()