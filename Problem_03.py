# ==========================================
# Problem 3 – Quantum Correlation Explorer (Entanglement)
# ==========================================

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np
import qiskit

print("\n=== Problem 3: Quantum Correlation Explorer ===")
sim = AerSimulator()

qc3 = QuantumCircuit(2,2)

# Create Bell state
qc3.h(0)
qc3.cx(0,1)

# Optional: apply rotations before measurement
# qc3.h(0)
# qc3.s(1)
# qc3.t(1)

qc3.measure([0,1],[0,1])

job3 = sim.run(qc3, shots=1024)
result3 = job3.result()
counts3 = result3.get_counts()

qc3.draw('mpl')
plt.show()

plot_histogram(counts3, title="Bell State Measurement Correlations")
plt.show()

# Bloch sphere (before measurement)
qc3_no_meas = QuantumCircuit(2)
qc3_no_meas.h(0)
qc3_no_meas.cx(0,1)
state3 = Statevector.from_instruction(qc3_no_meas)
plot_bloch_multivector(state3)
plt.show()
