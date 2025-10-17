# 🌌 Quantum Hackathon Simulator Suite

A collection of three **interactive quantum computing simulations** built with **Qiskit** and **Streamlit**, featuring modern, visually engaging UIs to explore key quantum phenomena — **superposition, entanglement, and quantum communication**.

![Quantum Computing](https://img.shields.io/badge/Quantum-Computing-blue)
![Qiskit](https://img.shields.io/badge/Built%20with-Qiskit-purple)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)

---

## 🚀 Features

### 🔗 Problem 1: Quantum Communication Simulator
- **Entanglement-based communication** using Bell states  
- **Interactive gate operations** (H, X, Z, Identity)  
- **Real-time circuit visualization** and measurement results  
- **Quantum state analysis** with probability distributions  
- **Beautiful, modern Streamlit UI** with intuitive controls  

### 🪙 Problem 2: Quantum Coin Game
- **Quantum vs Classical strategy** comparison  
- **Interactive game simulation** with referee moves  
- **Win/loss tracking** and performance statistics  
- **Dynamic visualization of outcomes**  
- **Smart strategy insights** based on results  

### 🔬 Problem 3: Quantum Correlation Explorer
- **Advanced entanglement experiments** with configurable gates  
- **Correlation strength measurement** and visual analysis  
- **Multiple rotation gates** (H, S, T, X, Y, Z)  
- **Entanglement verification tools**  
- **Customizable circuit builder**  

---

## 🛠️ Installation

### Prerequisites
- 🐍 Python **3.8 or higher**  
- 📦 `pip` (Python package manager)  
- 💾 Minimum **4GB RAM** (8GB recommended)  
- ⚙️ **500MB** free disk space  

---

### ⚡ Quick Setup

1. **Navigate to the project directory:**
   ```bash
   cd C:\Users\DR\Desktop\hackathon_problems\Hackathon_Problems
  

2. **Installation:**
    ```bash
    pip install -r requirements.txt

3. **Run individual simulations:**
    ```bash
    # Problem 1: Quantum Communication
    streamlit run Problem_01.py

    # Problem 2: Quantum Coin Game  
    streamlit run Problem_02.py

    # Problem 3: Quantum Correlation Explorer
    streamlit run Problem_03.py

📁 Project Structure
  ```bash
      Hackathon_Problems/
    ├── Problem_01.py              # Quantum Communication Simulator
    ├── Problem_02.py              # Quantum Coin Game
    ├── Problem_03.py              # Quantum Correlation Explorer
    ├── requirements.txt           # Python dependencies
    └── README.md                  # Project documentation
```
🎯 Detailed Usage Guide
🔗 Problem 1: Quantum Communication Simulator

Step-by-Step Instructions:

Run:
  ```bash
  streamlit run Problem_01.py
```
###In the sidebar, select Alice's quantum operation:
- H Gate: Creates quantum superposition
- X Gate: Performs bit-flip operation
- Z Gate: Applies phase-flip

###Identity: No operation (control case)

- Adjust number of shots (100–5000) for precision.
- Click Run Quantum Simulation.

###You’ll See:
- 🧩 Quantum Circuit Diagram
- 📊 Measurement Histogram
- 🌀 State Probabilities
- 🧠 Quantum Insights

###Key Learning Points:

- Understand quantum entanglement for secure communication
- Observe instant correlation between Alice and Bob
- Learn quantum measurement and state collapse


