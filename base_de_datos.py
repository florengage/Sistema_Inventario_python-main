import sqlite3 as sql
from colorama import Fore, Back, init
init()
conexion = sql.connect("inventario.db")
cursor = conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL, cantidad INTEGER NOT NULL,
               precio REAL NOT NULL)
               ''')
conexion.commit()


def agregar_producto(nombre:str, cantidad:int, precio:float):
    """Inserta un nuevo producto en la base de datos
    se pide nombre de producto (string)
    cantidad de productos (integer)
    precio de los productos(float)
    se conecta con la db y guarda el objeto 
    """
    cursor.execute(
                    '''INSERT INTO productos (
                   nombre, cantidad, precio) VALUES (?, ?, ?)''', 
                   (nombre, cantidad, precio))
    conexion.commit()
    print(Fore.GREEN +"producto agregado con éxito.")


def mostrar_productos():
    """Muestra todos los productos en la base de datos"""
    cursor.execute('''SELECT * FROM productos''')
    productos = cursor.fetchall()
    print("\nLista de productos:")
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, cantidad: {producto[2]}, precio: {producto[3]}")
  

def actualizar_precio(id_producto:int, nuevo_precio:float):
    """Modifica el precio de un producto
    se pide el id del producto a modificar (integer)
    se pide el precio nuevo (float)
    y se modifica en la bd
    """
    cursor.execute('''UPDATE productos SET precio = ? WHERE id = ?''',
    (nuevo_precio, id_producto))
    conexion.commit()
    print(Fore.GREEN + "precio actualizado correctamente.")
  
def eliminar_producto(id_producto:int):
    """Elimina un producto de la base de datos
    se pide el id del producto(integer)
    se elimina de la bd
    """
    cursor.execute('''DELETE FROM productos WHERE id = ?''', (id_producto,))
    if cursor.rowcount > 0:
        print(Fore.GREEN + "Producto eliminado con éxito.")
    else:
        print(Fore.RED +f"Error: El producto con ID {id_producto} no existe.")
    conexion.commit()
  