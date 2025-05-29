from Qubit import *
from oracle import *
from Grover import *
from math import sqrt
import numpy as np


def print_divider(title):
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)

def main():
    q0 = Qubit.Zero()
    q1 = Qubit.One()
    print(q0)
    print(q1)
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

    #Oracles
    s1 = create_state(0, 1, 0)  # |010>
    print_state(s1, "До oracle_const1")
    s1 = oracle_const1(s1)
    print_state(s1, "После oracle_const1")

    s2 = create_state(1, 0, 1)  # |101>
    print_state(s2, "До oracle_xor")
    s2 = oracle_xor(s2)
    print_state(s2, "После oracle_xor")

    # 1. Начальное |00>
    state = np.zeros(4, dtype=complex)
    state[0] = 1.0

    # 2. Суперпозиция
    H2 = hadamard_2()
    state = H2 @ state
    print_state(state, "После H⊗H")

    # 3. Оракул
    state = oracle(state)
    print_state(state, "После оракула (знак у |11>)")

    # 4. Диффузия
    state = diffusion(state)
    print_state(state, "После диффузии")

    # 5. Какое состояние самое вероятное
    most_likely = np.argmax(np.abs(state)**2)
    print(f"\nНаибольшая вероятность у |{format(most_likely, '02b')}>")
if __name__ == "__main__":
    main()
