import matplotlib.pyplot as plt
from qiskit import QuantumCircuit

qc = QuantumCircuit(4, 4)
qc.draw(output="mpl")
plt.show()