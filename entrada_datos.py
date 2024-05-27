def obtener_datos():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Dirección: ")

    productos = []
    while True:
        producto = input("Nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == 'fin':
            break
        precio = float(input(f"Precio de {producto}: "))
        productos.append((producto, precio))

    return nombre, apellido, direccion, productos