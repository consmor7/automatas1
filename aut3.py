def construir_tabla_transiciones(afn, alfabeto): #Para La tabla M' tomando de parametros
    tabla = {}                                     #el Aut Finito no determinista 
    for estado in afn[0]: #HASTA QUE NO SE PRESENTEN NUEVOS ESTADOS
        for simbolo in alfabeto:
            estados_destino = set()  #Va evaluando desde la tabla del afn
            for estado_origen in estado:
                if estado_origen in afn[1] and simbolo in afn[1][estado_origen]: 
                    estados_destino.update(afn[1][estado_origen][simbolo]) #Si se repite no lo agrega
            tabla[(estado, simbolo)] = tuple(estados_destino) #Si aun no se agrega se agrega ala tupla
    return tabla #Crea una nueva tabla con nuevos valores 

def construir_nuevos_estados(tabla_transiciones, alfabeto):
    nuevos_estados = set()  #Se crea una nueva tabla para las r, renombrando los estados ant con nuevos
    nuevos_estados.add(tuple(afn[2]))  # Se comienza evaluar las tuplas anteriories.
    while True: 
        nuevos_estados_encontrados = set() 
        for estado in nuevos_estados:
            for simbolo in alfabeto:
                if (estado, simbolo) in tabla_transiciones:
                    nuevos_estados_encontrados.add(tabla_transiciones[(estado, simbolo)])
        if nuevos_estados_encontrados == nuevos_estados:
            break
        nuevos_estados.update(nuevos_estados_encontrados)
    return list(nuevos_estados)

def determinar_Q_prima(tabla_transiciones, nuevos_estados, afn):
    Q_prima = {tuple(afn[2])}  #Se determina Q' con los estados que pertenecen al conjunto de F.
    for estado in nuevos_estados:
        if any(q in estado for q in afn[3]):
            Q_prima.add(estado)
    return list(Q_prima)

# Definir el AFN de entrada 
afn = (
    {'q0', 'q1', 'q2'},
    {
        'q0': {'a': {'q2'}, 'b': {'q1'}},
        'q1': {'a': {'q0'}, 'b': {'q2'}},
        'q2': {'a': {'q1', 'q2'}, 'b': {'q1'}}
    },
    {'q0'},
    {'q1', 'q2'}
)
alfabeto = {'a', 'b'}
print("Q' {r0,r1,r2,r3,r4}")
print("Estado inicial: r0")
print("F'={r1,r2,r3,r4,r5")
# Paso 2: Construir tabla de transiciones
tabla_transiciones = construir_tabla_transiciones(afn, alfabeto)
# Paso 3: Construir nuevos estados
nuevos_estados = construir_nuevos_estados(tabla_transiciones, alfabeto)
# Paso 4: Determinar Q'
Q_prima = determinar_Q_prima(tabla_transiciones, nuevos_estados, afn)
# Paso 5: Determinar F'
F_prima = {estado for estado in Q_prima if any(q in estado for q in afn[3])}

print("Q' =", Q_prima)
print("F' =", F_prima)












