import mysql.connector
from tkinter import messagebox

try:
    conexion = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "",
        database = "minisuper"
    )
    cursor = conexion.cursor(buffered = True)
except:
    messagebox.showerror(title="Sin conexión", detail="¡Por el momento no es posible conectarse a la base de datos!\nIntentelo de nuevo mas tarde")