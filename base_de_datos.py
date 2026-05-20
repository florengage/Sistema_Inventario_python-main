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


def agregar_producto(nombre, cantidad, precio):
    """Inserta un nuevo producto en la base de datos"""
    if not isinstance(cantidad(int)):
       raise TypeError('la cantidad debe ser un numero entero!')
    if not isinstance(precio(float)):
       raise TypeError('el precio debe ser un numero!')
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
  

def actualizar_precio(id_producto, nuevo_precio):
    """Modifica el precio de un producto"""
    if not isinstance(id_producto(int)):
       raise TypeError('el id del producto debe ser un numero entero!')
    if not isinstance(nuevo_precio(float)):
       raise TypeError('el precio debe ser un numero!') 
    cursor.execute('''UPDATE productos SET precio = ? WHERE id = ?''',
    (nuevo_precio, id_producto))
    conexion.commit()
    print(Fore.GREEN + "precio actualizado correctamente.")
  
def eliminar_producto(id_producto):
    """Elimina un producto de la base de datos"""
    if not isinstance(id_producto(int)):
       raise TypeError('el id del producto debe ser un numero entero!')
    cursor.execute('''DELETE FROM productos WHERE id = ?''', (id_producto,))
    if cursor.rowcount > 0:
        print(Fore.GREEN + "Producto eliminado con éxito.")
    else:
        print(Fore.RED +f"Error: El producto con ID {id_producto} no existe.")
    conexion.commit()
  