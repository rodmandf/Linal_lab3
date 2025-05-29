import numpy as np

H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])

def hadamard_2():
    return np.kron(H, H)

def oracle(state):
    state = state.copy()
    state[3] *= -1
    return state

def diffusion(state):
    mean = np.mean(state)
    return 2 * mean - state

def print_state(state, label):
    print(f"\n{label}:")
    for i, amp in enumerate(state):
        if abs(amp) > 1e-6:
            bits = format(i, '02b')
            prob = abs(amp)**2
            print(f"{amp.real:.3f} |{bits}>   p={prob:.2f}")

