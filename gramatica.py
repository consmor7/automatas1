# Función para cargar las reglas de producción desde un archivo
def cargar_gramatica_desde_archivo(nombre_archivo):
    # Abrir el archivo en modo de lectura
    with open(nombre_archivo, 'r') as archivo:
        # Leer todas las líneas del archivo
        lineas = archivo.readlines()

    # Inicializar un diccionario para almacenar las producciones por variable no terminal
    producciones = {}
    
    # Procesar cada línea del archivo
    for linea in lineas:
        # Dividir la línea en partes utilizando el tabulador como separador
        partes = linea.strip().split('\t')
        
        # La primera parte antes de la flecha (->) es la variable no terminal
        variable = partes[0]
        
        # Las partes restantes son las producciones asociadas con la variable
        producciones[variable] = partes[2:]

    # Devolver el diccionario con las reglas de producción
    return producciones

# Función para determinar si la gramática es vacía
def es_gramatica_vacia(producciones, V, T, S):
    # Conjuntos para almacenar las variables recién descubiertas en cada iteración
    Nuevo = set()
    # Conjunto para almacenar las variables descubiertas en la iteración anterior
    Anterior = set()

    # Algoritmo para determinar si la gramática es vacía
    while Nuevo != Anterior:
        # Actualizar el conjunto anterior con el conjunto actual
        Anterior = Nuevo.copy()

        # Iterar sobre cada variable no terminal en el conjunto de variables
        for A in V:
            # Verificar si la variable tiene reglas de producción asociadas
            if A in producciones:
                # Iterar sobre las producciones asociadas con la variable
                for produccion in producciones[A]:
                    # Verificar si todos los símbolos de la producción están en T U Anterior
                    if all(s in T.union(Anterior) for s in produccion):
                        Nuevo.add(A)
                    # Verificar si todos los símbolos de la producción están en Nuevo
                    elif all(s in Nuevo for s in produccion):
                        Nuevo.add(A)

    # Determinar si la variable inicial está en el conjunto Nuevo
    if S in Nuevo:
        print("La gramática NO es vacía.")
    else:
        print("La gramática es vacía.")

# Cargar las reglas de producción desde el archivo "gramatica.txt"
nombre_archivo = "gramatica.txt"
producciones = cargar_gramatica_desde_archivo(nombre_archivo)

# Solicitar al usuario el conjunto de variables, el conjunto de terminales y el símbolo inicial
V = set(input("Ingrese el conjunto de variables (separadas por comas): ").split(','))
T = set(input("Ingrese el conjunto de terminales (separados por comas): ").split(','))
S = input("Ingrese el símbolo inicial: ")

# Llamar a la función principal
es_gramatica_vacia(producciones, V, T, S)
