def transicion(estado, simbolo):
    tabla = {
        'q0': {'0': {'q0', 'q3'}, '1': {'q0', 'q1'}},
        'q1': {'0': set(), '1': {'q2'}},
        'q2': {'0': {'q2'}, '1': {'q2'}},
        'q3': {'0': {'q4'}, '1': set()},
        'q4': {'0': {'q4'}, '1': {'q4'}}
    }
    return tabla[estado][simbolo]

# Conjunto de estados finales
estados_finales = {'q2', 'q4'}

# Función para verificar si una cadena es aceptada
def cadena_aceptada(cadena):
    estado_actual = 'q0'  # Empezamos en el estado inicial
    for simbolo in cadena:
        estado_actual = transicion(estado_actual, simbolo)
    
    return estado_actual in estados_finales

# Cadena a evaluar
cadena = "10001"

if cadena_aceptada(cadena):
    print(f"La cadena '{cadena}' es aceptada por el AFND.")
else:
    print(f"La cadena '{cadena}' no es aceptada por el AFND.")
