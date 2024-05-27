from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from datetime import datetime

def generar_factura_pdf(nombre, apellido, direccion, productos):
    nombre_archivo = f"Factura_{nombre}_{apellido}.pdf"
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
    ancho, alto = letter

    # Estilos
    estilos = getSampleStyleSheet()
    estilo_titulo = estilos['Title']
    estilo_normal = estilos['Normal']

    # Contenido de la factura
    contenido = []

    # Título
    titulo = Paragraph("Factura", estilo_titulo)
    contenido.append(titulo)
    contenido.append(Paragraph(f"Fecha: {datetime.now().strftime('%Y-%m-%d')}", estilo_normal))
    contenido.append(Paragraph(f"Nombre: {nombre} {apellido}", estilo_normal))
    contenido.append(Paragraph(f"Dirección: {direccion}", estilo_normal))

    # Espacio
    contenido.append(Paragraph("<br/><br/>", estilo_normal))

    # Tabla de productos
    datos = [["Producto", "Precio"]]
    total = 0
    for producto, precio in productos:
        datos.append([producto, f"${precio:.2f}"])
        total += precio

    datos.append(["Total", f"${total:.2f}"])

    tabla = Table(datos, colWidths=[4 * inch, 2 * inch])
    estilo_tabla = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    tabla.setStyle(estilo_tabla)
    contenido.append(tabla)

    # Construir PDF
    doc.build(contenido)
    print(f"Factura generada: {nombre_archivo}")