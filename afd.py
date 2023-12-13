def automata_afd(Q, Sigma, q0, F, delta, w):
    q = q0  # Estado inicial
    i = 0  # Índice para recorrer la cadena

    while i < len(w):
        s = w[i]  # Símbolo actual de la cadena
        if q in Q and s in Sigma:
            q = delta[q][s]  # Transición de estado
            i += 1
        else:
            print("Cadena no aceptada")
            return

    if q in F:
        print("Cadena aceptada")
    else:
        print("Cadena no aceptada")

# Ejemplo de uso:
Q = {'q0', 'q1', 'q2'}  # Conjunto de estados
Sigma = {'0', '1'}      # Alfabeto
q0 = 'q0'               # Estado inicial
F = {'q2'}              # Conjunto de estados de aceptación

# Función de transición en forma de diccionario
delta = {
    'q0': {'0': 'q1', '1': 'q0'},
    'q1': {'0': 'q2', '1': 'q0'},
    'q2': {'0': 'q2', '1': 'q2'}
}

cadena_a_analizar = "0011"
automata_afd(Q, Sigma, q0, F, delta, cadena_a_analizar)
