import base_de_datos
from colorama import Fore, Back, init
init()
while True:
    print(Back.BLACK + Fore.BLUE + "\nsistema de inventario")
    print(Back.BLACK +"1. Agregar producto")
    print(Back.BLACK +"2. Mostrar productos")
    print(Back.BLACK +"3. Actualizar precio de un producto")
    print(Back.BLACK +"4. Eliminar producto")
    print(Back.BLACK +"5. Salir")

    opcion = input("Seleccioná una opción: ")
    match opcion:
     case '1':
        try:
            nombre = input("Ingresá el nombre del producto: ").strip()
            cantidad = input("Ingresá la cantidad: ").strip()
            precio = input("Ingresá el precio del producto: ").strip()
            if not cantidad.isdigit() and not precio.isdigit():
                print( Fore.RED + "la cantidad y el precio deben ser un número válido.")
            else:
                base_de_datos.agregar_producto(nombre, int(cantidad), precio)
        except Exception as e:
            print( Fore.RED + f"Ocurrió un error inesperado: {e}")
     case "2":
        base_de_datos.mostrar_productos()
     case '3':
        id_producto = input("Ingresá el ID del producto a actualizar:").strip()
        nuevo_precio = input("Ingresá el nuevo precio: ").strip()
        if id_producto.isdigit():
            base_de_datos.actualizar_precio(int(id_producto), nuevo_precio)
        else:
            print( Fore.RED + "El ID debe ser un número válido.")
     case"4":
        id_producto = input("Ingresá el ID del producto a eliminar:").strip()
        if id_producto.isdigit():
            base_de_datos.eliminar_producto(int(id_producto))
        else:
            print( Fore.RED + "El ID debe ser un número válido.")
     case"5":
        print("Saliendo del sistema...")
        break
     case _:
        print( Fore.RED + "Opción inválida. Intentá nuevamente.")

base_de_datos.conexion.close()