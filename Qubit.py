import numpy as np
import math

class Qubit:
    def __init__(self, alpha=1.0, beta=0.0):
        state = np.array([complex(alpha), complex(beta)])
        norm = np.linalg.norm(state)
        if norm == 0:
            raise ValueError("Нулевое состояние недопустимо")
        self.state = state / norm

    def apply_gate(self, gate):
        self.state = gate @ self.state
        
    def Zero():
        return Qubit(1, 0)
    def One():
        return Qubit(0, 1)
    
    def __str__(self):
        return f"Qubit state: {self.state[0]:.2f}|0⟩ + {self.state[1]:.2f}|1⟩"

X_GATE = np.array([[0, 1],
                   [1, 0]], dtype=complex)

Y_GATE = np.array([[0, -1j],
                   [1j, 0]], dtype=complex)

Z_GATE = np.array([[1, 0],
                   [0, -1]], dtype=complex)

class TwoQubit:
    def __init__(self, qubit1: Qubit, qubit2: Qubit):
        self.state = np.kron(qubit1.state, qubit2.state)

    def apply_gate(self, gate_4x4):
        self.state = gate_4x4 @ self.state

    def __str__(self):
        basis = ["|00⟩", "|01⟩", "|10⟩", "|11⟩"]
        result = []
        for amp, label in zip(self.state, basis):
            amp = complex(amp)
            if abs(amp) > 1e-6:
                result.append(f"{amp:.2f}{label}")
        return " + ".join(result)

CNOT_GATE = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], dtype=complex)
