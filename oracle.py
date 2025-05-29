import numpy as np

def create_state(x0, x1, y):
    index = (x0 << 2) | (x1 << 1) | y
    state = np.zeros(8, dtype=complex)
    state[index] = 1.0
    return state

def print_state(state, label):
    print(f"\n{label}:")
    for i, amp in enumerate(state):
        if abs(amp) > 1e-6:
            bits = format(i, '03b') 
            print(f"{amp.real:.1f} |{bits}>")

def oracle_const1(state):
    new_state = state.copy()
    for i in range(8):
        if abs(state[i]) > 1e-6:
            bits = list(format(i, '03b'))
            bits[2] = '0' if bits[2] == '1' else '1'
            j = int(''.join(bits), 2)
            new_state[j] = state[i]
            new_state[i] = 0
    return new_state

def oracle_xor(state):
    new_state = state.copy()
    for control in [0, 1]:  # x0 и x1
        temp_state = np.zeros_like(state)
        for i in range(8):
            bits = list(format(i, '03b'))
            if bits[control] == '1':
                bits[2] = '0' if bits[2] == '1' else '1'
            j = int(''.join(bits), 2)
            temp_state[j] += new_state[i]
        new_state = temp_state
    return new_state
