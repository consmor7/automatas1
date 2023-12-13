def convert_to_dfa(Q, Sigma, q0, F, delta):
    def epsilon_closure(state):
        epsilon_transitions = set()
        stack = list(state)
        while stack:
            current_state = stack.pop()
            epsilon_transitions.add(current_state)
            if ('', current_state) in delta:
                epsilon_transitions.update(delta[('', current_state)])
                stack.extend(delta[('', current_state)])
        return frozenset(epsilon_transitions)

    def move(states, symbol):
        next_states = set()
        for state in states:
            if (symbol, state) in delta:
                next_states.update(delta[(symbol, state)])
        return frozenset(next_states)

    dfa_states = set()
    dfa_delta = {}
    queue = [epsilon_closure({q0})]
    dfa_states.add(epsilon_closure({q0}))

    while queue:
        current_states = queue.pop(0)
        for symbol in Sigma:
            next_states = move(current_states, symbol)
            if not next_states in dfa_states:
                queue.append(next_states)
                dfa_states.add(next_states)
            dfa_delta[(current_states, symbol)] = next_states

    dfa_start = epsilon_closure({q0})
    dfa_final = [state for state in dfa_states if any(q in F for q in state)]

    return dfa_states, Sigma, dfa_start, dfa_final, dfa_delta

# Datos de entrada
Q = {'q0', 'q1', 'q2'}
Sigma = {'a', 'b'}
q0 = 'q0'
F = {'q1', 'q2'}
delta = {
    # Transiciones para el estado q0
    ('a', 'q0'): {'q2'},  # Transición para el símbolo 'a'
    ('b', 'q0'): {'q1'},  # Transición para el símbolo 'b'

    # Transiciones para el estado q1
    ('a', 'q1'): {'q0'},
    ('b', 'q1'): {'q2'},

    # Transiciones para el estado q2
    ('a', 'q2'): {'q1', 'q2'},
    ('b', 'q2'): {'q0', 'q2'},
}

# Conversión a AFD
dfa_states, dfa_sigma, dfa_start, dfa_final, dfa_delta = convert_to_dfa(Q, Sigma, q0, F, delta)

# Resultados
print("Estados del AFD:", dfa_states)
print("Alfabeto del AFD:", dfa_sigma)
print("Estado inicial del AFD:", dfa_start)
print("Estados finales del AFD:", dfa_final)
print("Función de transición del AFD:", dfa_delta)
