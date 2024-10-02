Lista = []

def mostrar_menu():
    print("Opciones")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver productos")
    print("4. Salir")

def agregar_producto():
    prod = input("Escriba los producto: ")
    total = input("Escriba el total de productos: ")
    Lista.append([prod, total])
    print(prod + "producto agregado")

def eliminar_producto():
    prod = input("Escriba el producto a eliminar: ")
    for elem in Lista:
        if elem[0] == prod:
            Lista.remove(elem)
            print(prod + "el producto fue eliminado.")
            return
    print(prod + "el producto no existe.")

def ver_lista():
    if len(Lista) > 0:
        print("Lista de productos")
        for elem in Lista:
            print("Producto: " + elem[0] + ", Total: " + elem[1])
    else:
        print("la lista esta vacía")

print("Bienvenido a la frutería Pozole")

while True:
    mostrar_menu()
    opcion = input("Elija la opcion que quiere ejecutar: ")
    
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        ver_lista()
    elif opcion == "4":
        print("Saliendo del progra,a")
        break
    else:
        print("la opción no es válida")
