# Definir el diccionario de productos con sus precios
productos = {
    "Manzana": 1.0,
    "Banana": 0.75,
    "Naranja": 1.25,
    "Uva": 2.0,
    "Pera": 1.1
}

# Mostrar el menú al usuario
print("Bienvenido al menú de productos:")
for producto, precio in productos.items():
    print(f"{producto}: ${precio}")

# Crear un diccionario para almacenar las selecciones del usuario
selecciones = {}

# Pedir al usuario que seleccione productos y cantidades
while True:
    seleccion = input("\nSeleccione un producto de la lista (o escriba 'salir' para finalizar): ")
    if seleccion.lower() == 'salir':
        break

    if seleccion in productos:
        cantidad = int(input(f"Ingrese la cantidad de {seleccion} que desea comprar: "))
        if cantidad > 0:
            if seleccion in selecciones:
                selecciones[seleccion] += cantidad
            else:
                selecciones[seleccion] = cantidad
        else:
            print("La cantidad debe ser mayor que 0.")
    else:
        print("Producto no encontrado en la lista.")

# Calcular y mostrar el total de la compra
total = 0
print("\nResumen de la compra:")
for seleccion, cantidad in selecciones.items():
    precio_unitario = productos[seleccion]
    subtotal = precio_unitario * cantidad
    print(f"{seleccion}: {cantidad} x ${precio_unitario:.2f} = ${subtotal:.2f}")
    total += subtotal

print(f"Total a pagar: ${total:.2f}")


