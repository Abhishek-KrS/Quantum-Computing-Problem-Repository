# Python
import networkx as nx
# from qiskit import Aer, execute
from qiskit.aqua.algorithms import QAOA, NumPyMinimumEigensolver
# from qiskit.optimization.applications.ising import max_independent_set

# Defines the graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (1, 5)])

# Creates a QAOA instance
qaoa = QAOA(G)

# Solves the MIS problem using QAOA
result_qaoa = qaoa.compute_minimum_eigenvalue()

# Creates a Quantum adiabatic algorithm instance
qae = NumPyMinimumEigensolver(G)

# Solves the MIS problem using Quantum adiabatic algorithm
result_qae = qae.compute_minimum_eigenvalue()

# Prints the MIS solutions
print("MIS solution using QAOA:", result_qaoa)
print("MIS solution using Quantum adiabatic algorithm:", result_qae)

'''
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, transpile, assemble
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import QAOA
from qiskit.optimization.applications.ising import max_independent_set
import networkx as nx

def solve_mis_qaoa(graph):
    # Converts graph to Ising Hamiltonian
    qubit_op, offset = max_independent_set.get_operator(nx.Graph(graph))

    # Initializes QAOA algorithm
    qaoa = QAOA(qubit_op)

    # Sets up backend
    backend = Aer.get_backend('qasm_simulator')
    quantum_instance = QuantumInstance(backend)

    # Runs QAOA algorithm
    result = qaoa.run(quantum_instance)

    # Extracts solution
    mis = max_independent_set.sample_most_likely(result.eigenstate)

    return mis

# Example usage
graphs = [
    nx.complete_graph(3),
    nx.complete_graph(5),
    nx.complete_graph(6),
    nx.complete_graph(7)
]

for i, graph in enumerate(graphs, start=1):
    print(f"Graph {i}:")
    mis = solve_mis_qaoa(graph)
    print("Maximum Independent Set:", mis)
'''
