def contar_lineas_palabras_espacios_letras(archivo):
    try:
        with open(archivo, 'r') as f:
            contenido = f.read()
            lineas = contenido.split('\n')
            palabras = contenido.split()
            espacios = contenido.count(' ')
            letras = sum(c.isalpha() for c in contenido)

            num_lineas = len(lineas)
            num_palabras = len(palabras)
            num_espacios = espacios

            return num_lineas, num_palabras, num_espacios, letras
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return 0, 0, 0, 0

archivo = "C:/Users/Angel/Documents/automatas/texto.txt"  #
lineas, palabras, espacios, letras = contar_lineas_palabras_espacios_letras(archivo)

print(f"Número de líneas: {lineas}")
print(f"Número de palabras: {palabras}")
print(f"Número de espacios en blanco: {espacios}")
print(f"Número de letras: {letras}")