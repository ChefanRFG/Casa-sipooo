Inventario = {}
item="Tomate, Cebolla, Lechuga, Manzana, Pera, Sandia, Melon, Coco, Melocoton, Papaya, Aguacate, Pitaya"
print("Bienvenido al inventario de la fruteria Pozole")
while True:
    item=input("Ingresa el producto de tu lista que deseas manipular: ")
    if item == "fin":
        break
    else:
        Inventario.append(item)

print("Inventario")

while True:
    elim=input("Quieres eliminar algo de el inventario?: ")
    if elim == "no":
        break
    elif elim == "si":
        item_elim = input("que desea eliminar?: ")
        if item_elim == "fin":
            break

    else:
        print(Inventario)
        break