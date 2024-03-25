# Python
from qiskit import QuantumCircuit, Aer, execute

def oddToEven(n, num_list):
    # Calculates the number of qubits required based on n
    k = len(bin(n-1)[2:])
    
    # Creates a quantum circuit with k qubits
    circuit = QuantumCircuit(k, k)
    
    # Applies X-gate to flip the state of odd numbers
    for i in range(len(num_list)):
        if num_list[i] % 2 != 0:
            circuit.x(i)
    
    # Measures the qubits and stores the result in classical registers
    circuit.measure(range(k), range(k))
    
    # Simulates the circuit using the local simulator
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)
    result = job.result()
    counts = result.get_counts(circuit)
    
    # Converts the measurement result to a list of integers
    output_list = [int(key[::-1], 2) for key in counts.keys()]
    
    return output_list

# Example usage
n = 31
num_list = [1, 2, 2, 4, 5, 6, 7, 11, 17, 21, 22, 23]
B = oddToEven(n, num_list)
print(B)
