Quantum Hackathon Simulator Suite
A collection of three interactive quantum computing simulations built with Qiskit and Streamlit, featuring beautiful modern UIs for exploring quantum phenomena.

🚀 Features
Problem 1: Quantum Communication Simulator

Entanglement-based communication using Bell states
Interactive gate operations (H, X, Z, Identity)
Real-time circuit visualization and measurement results
Quantum state analysis with probability distributions

Problem 2: Quantum Coin Game

Quantum vs Classical strategy comparison
Interactive game simulation with referee moves
Win/loss tracking and statistics
Real-time performance analysis

Problem 3: Quantum Correlation Explorer

Advanced entanglement experiments with configurable gates
Correlation strength measurement and analysis
Multiple rotation gates (H, S, T, X, Y, Z)
Entanglement verification and quantum insights

🛠️ Installation

Prerequisites

Python 3.8 or higher
pip (Python package manager)

Quick Setup

Clone or download the project files to your local machine:
C:\Users\Desktop\hackathon-problems\Hackathon_problems

Install required packages:

cd C:\Users\DR\Desktop\hackathon_problems\Hackathon_Problems
pip install -r requirements.txt

Run individual simulations:

# Problem 1: Quantum Communication
streamlit run Problem_01.py

# Problem 2: Quantum Coin Game  
streamlit run Problem_02.py

# Problem 3: Quantum Correlation Explorer
streamlit run Problem_03.py

📁 Project Structure

Hackathon_Problems/
├── Problem_01.py          # Quantum Communication Simulator
├── Problem_02.py          # Quantum Coin Game
├── Problem_03.py          # Quantum Correlation Explorer
├── requirements.txt       # Python dependencies
└── README.md             # This file

🎯 Usage Guide

Problem 1: Quantum Communication

Select Alice's operation from the sidebar (H, X, Z, or Identity gate)
Adjust simulation shots for measurement precision
Click "Run Quantum Simulation" to execute

Analyze results:

View quantum circuit diagram
See measurement histogram
Check state probabilities
Read quantum correlation insights

Problem 2: Quantum Coin Game

Choose your strategy: Quantum (H gate) or Classical (no gate)
Set number of games to play (1-10)
Click "Play Quantum Coin Game" to start

Track your performance:
Individual game results
Win/loss statistics
Strategy recommendations
Circuit visualization

Problem 3: Quantum Correlation Explorer

Configure entanglement with H and CNOT gates
Add rotations to qubits 0 and 1
Set measurement shots for accuracy
Click "Explore Quantum Correlations"

Study the results:

Correlation strength metrics
Entanglement verification
State probability analysis
