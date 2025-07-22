from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to put qubit in superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)
result = job.result()
counts = result.get_counts()

# Plot the results
plot_histogram(counts)
plt.savefig('coin_flip_histogram.png')  # Save the plot
plt.show()

# Print the circuit
print(qc.draw())
