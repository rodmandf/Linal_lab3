from Qubit import *
from math import sqrt
import numpy as np

def print_divider(title):
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)

def main():
    # Однокубитные гейты
    print_divider("Однокубитные гейты")
    q = Qubit()  # |0⟩
    print("Начальное состояние:", q)
    q.apply_gate(X_GATE)
    print("После X-гейта:", q)
    q.apply_gate(Y_GATE)
    print("После Y-гейта:", q)
    q.apply_gate(Z_GATE)
    print("После Z-гейта:", q)

    print_divider("CNOT на |1⟩|0⟩")
    q1 = Qubit(0, 1)
    q2 = Qubit(1, 0)
    system = TwoQubit(q1, q2)
    print("До CNOT:", system)
    system.apply_gate(CNOT_GATE)
    print("После CNOT:", system)

    print_divider("Запутывание |+⟩|0⟩")
    q3 = Qubit(1/sqrt(2), 1/sqrt(2))
    q4 = Qubit(1, 0)
    entangled = TwoQubit(q3, q4)
    print("До CNOT:", entangled)
    entangled.apply_gate(CNOT_GATE)
    print("После CNOT:", entangled)

if __name__ == "__main__":
    main()