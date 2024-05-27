from entrada_datos import obtener_datos
from generar_pdf import generar_factura_pdf

def main():
    nombre, apellido, direccion, productos = obtener_datos()
    generar_factura_pdf(nombre, apellido, direccion, productos)

if __name__ == "__main__":
    main()
