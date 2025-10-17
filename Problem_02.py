from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np
import qiskit


# ==========================================
# Problem 2 – Quantum Coin Game (Superposition)
# ==========================================
print("\n=== Problem 2: Quantum Coin Game ===")
sim = AerSimulator()

qc2 = QuantumCircuit(1,1)

# Fair coin (Hadamard)
qc2.h(0)

# Optional: biased coin
# theta = np.pi/4
# qc2.ry(theta, 0)

qc2.measure(0,0)

job2 = sim.run(qc2, shots=1000)
result2 = job2.result()
counts2 = result2.get_counts()

qc2.draw('mpl')
plt.show()

plot_histogram(counts2, title="Quantum Coin Toss Results")
plt.show()

# Bloch sphere
qc2_no_meas = QuantumCircuit(1)
qc2_no_meas.h(0)
state2 = Statevector.from_instruction(qc2_no_meas)
plot_bloch_multivector(state2)
plt.show()


