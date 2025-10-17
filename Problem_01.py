# ==========================================
# Problem 1 – Quantum Communication Simulator
# Modern UI Version - FIXED
# ==========================================

import streamlit as st
import qiskit
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np

# Configure the page
st.set_page_config(
    page_title="Quantum Communication Simulator",
    page_icon="⚛️",
    layout="wide"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .section-header {
        font-size: 2rem;
        color: #2e86ab;
        border-bottom: 3px solid #2e86ab;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #2e86ab;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .info-box h4, .info-box li, .info-box p {
        color: #000000 !important;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-weight: bold;
    }
    .black-text {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">📡 Quantum Communication Simulator</div>', unsafe_allow_html=True)

# Initialize simulator
sim = AerSimulator()

# Initialize session state
if 'run_simulation' not in st.session_state:
    st.session_state.run_simulation = False
if 'results' not in st.session_state:
    st.session_state.results = None

# Sidebar for configuration
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    
    st.markdown("---")
    st.markdown("#### Alice's Operation")
    alice_op = st.selectbox(
        "Choose quantum gate:",
        ["h", "x", "z", "i"],
        format_func=lambda x: {
            "h": "🧬 Hadamard (H) Gate", 
            "x": "🔄 Pauli-X Gate", 
            "z": "🌀 Pauli-Z Gate", 
            "i": "⚪ Identity (No Operation)"
        }[x]
    )
    
    st.markdown("---")
    st.markdown("#### Simulation Settings")
    shots = st.slider("Number of Shots", 100, 5000, 1024, help="Number of times to run the simulation")
    
    st.markdown("---")
    st.markdown("#### Qiskit Info")
    st.write(f"🔬 Qiskit version: {qiskit.__version__}")
    
    st.markdown("---")
    if st.button("🚀 Run Quantum Simulation", use_container_width=True):
        st.session_state.run_simulation = True

# Main content area
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📋 Circuit Description")
    
    st.markdown("""
    <div class="info-box">
    <h4 style="color: #000000;">🧠 How Quantum Communication Works:</h4>
    <ol style="color: #000000;">
        <li style="color: #000000;"><b>Create Bell State</b>: Entangle two qubits using H and CNOT gates</li>
        <li style="color: #000000;"><b>Alice's Operation</b>: Apply selected quantum gate to first qubit</li>
        <li style="color: #000000;"><b>Measurement</b>: Measure both qubits to observe quantum correlations</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # Gate explanations
    st.markdown("### 🎯 Gate Effects")
    
    gate_info = {
        "h": "**Hadamard Gate**: Creates superposition |0⟩ → (|0⟩+|1⟩)/√2, |1⟩ → (|0⟩-|1⟩)/√2",
        "x": "**Pauli-X Gate**: Bit flip |0⟩ → |1⟩, |1⟩ → |0⟩",
        "z": "**Pauli-Z Gate**: Phase flip |0⟩ → |0⟩, |1⟩ → -|1⟩", 
        "i": "**Identity Gate**: No operation - preserves original state"
    }
    
    st.info(gate_info[alice_op])

with col2:
    if st.session_state.run_simulation:
        with st.spinner("🔄 Running quantum simulation..."):
            try:
                # Create quantum circuit
                qc1 = QuantumCircuit(2, 2)

                # Create Bell state
                qc1.h(0)
                qc1.cx(0, 1)

                # Alice applies an operation
                if alice_op == 'x':
                    qc1.x(0)
                elif alice_op == 'z':
                    qc1.z(0)
                elif alice_op == 'h':
                    qc1.h(0)
                # 'i' does nothing (identity)

                qc1.measure([0,1],[0,1])

                # Run simulation
                job1 = sim.run(qc1, shots=shots)
                result1 = job1.result()
                counts1 = result1.get_counts()
                
                # Store results
                st.session_state.results = {
                    'counts': counts1,
                    'circuit': qc1,
                    'alice_op': alice_op,
                    'shots': shots
                }
                
            except Exception as e:
                st.error(f"Error running simulation: {e}")

    if st.session_state.results is not None:
        results = st.session_state.results
        
        st.markdown(f"### 📊 Results (Alice's Operation: {results['alice_op'].upper()})")
        
        # Display circuit
        st.markdown("#### 🔧 Quantum Circuit")
        fig_circuit, ax_circuit = plt.subplots(figsize=(10, 4))
        results['circuit'].draw('mpl', ax=ax_circuit)
        ax_circuit.set_title(f"Quantum Communication Circuit\n(Alice applies {results['alice_op'].upper()} gate)", fontsize=14, fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig_circuit)
        
        # Display results in columns
        col_results1, col_results2 = st.columns(2)
        
        with col_results1:
            st.markdown("#### 📈 Measurement Results")
            fig_hist, ax_hist = plt.subplots(figsize=(8, 5))
            plot_histogram(results['counts'], ax=ax_hist, color=['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4'])
            ax_hist.set_title("Measurement Outcomes Distribution", fontweight='bold')
            ax_hist.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig_hist)
            
        with col_results2:
            st.markdown("#### 🔢 Detailed Statistics")
            total_shots = results['shots']
            
            # Create metrics for each state
            for state, count in sorted(results['counts'].items()):
                percentage = (count / total_shots) * 100
                st.metric(
                    label=f"State |{state}⟩",
                    value=f"{count} shots",
                    delta=f"{percentage:.1f}%"
                )
            
            st.markdown("#### 💡 Interpretation")
            total = sum(results['counts'].values())
            
            if len(results['counts']) == 1:
                state = list(results['counts'].keys())[0]
                st.success(f"✅ **Deterministic Outcome**: Always measured |{state}⟩")
                st.info("This shows perfect quantum correlation due to entanglement!")
            else:
                st.warning("🔍 **Probabilistic Outcomes**: Quantum superposition at work!")
                
            # Theoretical explanation
            st.markdown("#### 🧪 Theoretical Analysis")
            if results['alice_op'] == 'i':
                st.write("**Bell State |Φ⁺⟩ = (|00⟩ + |11⟩)/√2**")
                st.write("- Perfect correlation: both qubits same")
                st.write("- 50% |00⟩, 50% |11⟩")
                
            elif results['alice_op'] == 'x':
                st.write("**State after X gate: (|10⟩ + |01⟩)/√2**")
                st.write("- Anti-correlation: qubits always different") 
                st.write("- 50% |01⟩, 50% |10⟩")
                
            elif results['alice_op'] == 'z':
                st.write("**State after Z gate: (|00⟩ - |11⟩)/√2**")
                st.write("- Phase changed but same measurement probabilities")
                st.write("- 50% |00⟩, 50% |11⟩")
                
            elif results['alice_op'] == 'h':
                st.write("**State after H gate: Complex superposition**")
                st.write("- Creates equal superposition of all states")
                st.write("- More complex probability distribution")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Built with Qiskit ⚛️ | Quantum Communication Simulator"
    "</div>",
    unsafe_allow_html=True
)