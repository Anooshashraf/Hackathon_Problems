# ==========================================
# Problem 3 – Quantum Correlation Explorer (Entanglement)
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
    page_title="Quantum Correlation Explorer",
    page_icon="🔗",
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
    .entanglement-card {
        background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .stButton button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-weight: bold;
    }
    .correlation-high {
        background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
        color: white;
        padding: 0.5rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.2rem 0;
    }
    .correlation-low {
        background: linear-gradient(135deg, #ff6b6b 0%, #c44d4d 100%);
        color: white;
        padding: 0.5rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🔗 Quantum Correlation Explorer</div>', unsafe_allow_html=True)

# Initialize simulator
sim = AerSimulator()

# Initialize session state
if 'entanglement_results' not in st.session_state:
    st.session_state.entanglement_results = None
if 'run_simulation' not in st.session_state:
    st.session_state.run_simulation = False

# Sidebar for configuration
with st.sidebar:
    st.markdown("### ⚙️ Entanglement Configuration")
    
    st.markdown("---")
    st.markdown("#### 🔧 Quantum Gates")
    
    apply_h0 = st.checkbox("Apply H gate to qubit 0", value=True, help="Hadamard gate creates superposition")
    apply_cx = st.checkbox("Apply CX gate (entanglement)", value=True, help="CNOT gate creates entanglement")
    
    st.markdown("---")
    st.markdown("#### 🎛️ Additional Rotations")
    
    rotation_qubit0 = st.selectbox(
        "Rotation on Qubit 0:",
        ["none", "h", "s", "t", "x", "y", "z"],
        format_func=lambda x: {
            "none": "No rotation",
            "h": "Hadamard (H)",
            "s": "Phase (S)",
            "t": "T gate",
            "x": "Pauli-X",
            "y": "Pauli-Y", 
            "z": "Pauli-Z"
        }[x]
    )
    
    rotation_qubit1 = st.selectbox(
        "Rotation on Qubit 1:",
        ["none", "h", "s", "t", "x", "y", "z"],
        format_func=lambda x: {
            "none": "No rotation",
            "h": "Hadamard (H)",
            "s": "Phase (S)",
            "t": "T gate",
            "x": "Pauli-X",
            "y": "Pauli-Y",
            "z": "Pauli-Z"
        }[x]
    )
    
    st.markdown("---")
    st.markdown("#### 📊 Simulation Settings")
    shots = st.slider("Number of Shots", 100, 5000, 1024, help="Number of measurement repetitions")
    
    st.markdown("---")
    st.markdown("#### Qiskit Info")
    st.write(f"🔬 Qiskit version: {qiskit.__version__}")
    
    st.markdown("---")
    if st.button("🚀 Explore Quantum Correlations", use_container_width=True):
        st.session_state.run_simulation = True

# Main content area
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📋 Entanglement Description")
    
    st.markdown("""
    <div class="info-box">
    <h4 style="color: #000000;">🔗 Quantum Entanglement Explained:</h4>
    <p style="color: #000000;"><b>Bell State Creation:</b></p>
    <ol style="color: #000000;">
        <li style="color: #000000;"><b>Superposition</b>: H gate puts first qubit in (|0⟩+|1⟩)/√2 state</li>
        <li style="color: #000000;"><b>Entanglement</b>: CNOT gate correlates both qubits</li>
        <li style="color: #000000;"><b>Result</b>: Creates |Φ⁺⟩ = (|00⟩ + |11⟩)/√2 Bell state</li>
    </ol>
    <p style="color: #000000;"><b>Key Property:</b> Measuring one qubit instantly determines the other, regardless of distance!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Entanglement facts
    st.markdown("### 💡 Entanglement Facts")
    
    st.markdown("""
    <div class="entanglement-card">
    <h3>🎯 Perfect Quantum Correlation</h3>
    <p>In Bell states, qubits are perfectly correlated:</p>
    <p><b>• Both 0 or both 1</b></p>
    <p>No intermediate probabilities!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Gate explanations
    st.markdown("### 🎯 Gate Effects on Entanglement")
    
    gate_effects = {
        "h": "**Hadamard**: Creates superposition, essential for entanglement",
        "s": "**Phase gate**: Adds π/2 phase, affects interference",
        "t": "**T gate**: Adds π/4 phase, used in quantum algorithms", 
        "x": "**Pauli-X**: Bit flip, changes |0⟩↔|1⟩",
        "y": "**Pauli-Y**: Combined bit and phase flip",
        "z": "**Pauli-Z**: Phase flip, |1⟩→-|1⟩"
    }
    
    if rotation_qubit0 != "none" or rotation_qubit1 != "none":
        st.info("Additional rotations can modify entanglement and measurement probabilities")

with col2:
    if st.session_state.run_simulation:
        with st.spinner("🔄 Exploring quantum correlations..."):
            try:
                # Create quantum circuit
                qc3 = QuantumCircuit(2, 2)

                # Create Bell state (core entanglement)
                if apply_h0:
                    qc3.h(0)
                if apply_cx:
                    qc3.cx(0, 1)

                # Apply additional rotations to qubit 0
                if rotation_qubit0 != "none":
                    if rotation_qubit0 == "h":
                        qc3.h(0)
                    elif rotation_qubit0 == "s":
                        qc3.s(0)
                    elif rotation_qubit0 == "t":
                        qc3.t(0)
                    elif rotation_qubit0 == "x":
                        qc3.x(0)
                    elif rotation_qubit0 == "y":
                        qc3.y(0)
                    elif rotation_qubit0 == "z":
                        qc3.z(0)

                # Apply additional rotations to qubit 1
                if rotation_qubit1 != "none":
                    if rotation_qubit1 == "h":
                        qc3.h(1)
                    elif rotation_qubit1 == "s":
                        qc3.s(1)
                    elif rotation_qubit1 == "t":
                        qc3.t(1)
                    elif rotation_qubit1 == "x":
                        qc3.x(1)
                    elif rotation_qubit1 == "y":
                        qc3.y(1)
                    elif rotation_qubit1 == "z":
                        qc3.z(1)

                qc3.measure([0, 1], [0, 1])

                # Run simulation
                job3 = sim.run(qc3, shots=shots)
                result3 = job3.result()
                counts3 = result3.get_counts()
                
                # Calculate correlation metrics
                total = sum(counts3.values())
                same_state_prob = (counts3.get('00', 0) + counts3.get('11', 0)) / total
                diff_state_prob = (counts3.get('01', 0) + counts3.get('10', 0)) / total
                
                # Store results
                st.session_state.entanglement_results = {
                    'counts': counts3,
                    'circuit': qc3,
                    'shots': shots,
                    'same_state_prob': same_state_prob,
                    'diff_state_prob': diff_state_prob,
                    'correlation_strength': abs(same_state_prob - diff_state_prob)
                }
                
                st.session_state.run_simulation = False
                
            except Exception as e:
                st.error(f"Error running entanglement simulation: {e}")

    if st.session_state.entanglement_results is not None:
        results = st.session_state.entanglement_results
        
        st.markdown("### 📊 Entanglement Results")
        
        # Display correlation metrics
        col_metrics1, col_metrics2, col_metrics3 = st.columns(3)
        
        with col_metrics1:
            st.metric("Same State Probability", f"{results['same_state_prob']:.1%}")
        
        with col_metrics2:
            st.metric("Different State Probability", f"{results['diff_state_prob']:.1%}")
        
        with col_metrics3:
            correlation_strength = results['correlation_strength']
            if correlation_strength > 0.8:
                st.metric("Correlation Strength", "Strong 🔗")
            elif correlation_strength > 0.5:
                st.metric("Correlation Strength", "Medium 🔄")
            else:
                st.metric("Correlation Strength", "Weak 🔀")
        
        # Display circuit
        st.markdown("#### 🔧 Quantum Circuit")
        fig_circuit, ax_circuit = plt.subplots(figsize=(10, 4))
        results['circuit'].draw('mpl', ax=ax_circuit)
        ax_circuit.set_title("Quantum Correlation Circuit", fontsize=14, fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig_circuit)
        
        # Display results in columns
        col_results1, col_results2 = st.columns(2)
        
        with col_results1:
            st.markdown("#### 📈 Measurement Correlations")
            fig_hist, ax_hist = plt.subplots(figsize=(8, 5))
            plot_histogram(results['counts'], ax=ax_hist, color=['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4'])
            ax_hist.set_title("Bell State Measurement Correlations", fontweight='bold')
            ax_hist.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig_hist)
            
        with col_results2:
            st.markdown("#### 🔍 Correlation Analysis")
            
            # State probabilities
            st.markdown("**State Probabilities:**")
            for state, count in sorted(results['counts'].items()):
                percentage = (count / results['shots']) * 100
                col_prob1, col_prob2, col_prob3 = st.columns([1, 2, 1])
                with col_prob1:
                    st.markdown(f"**|{state}⟩**")
                with col_prob2:
                    st.progress(percentage/100)
                with col_prob3:
                    st.markdown(f"**{percentage:.1f}%**")
            
            # Entanglement analysis
            st.markdown("#### 🧪 Entanglement Verification")
            
            if results['same_state_prob'] > 0.9:
                st.success("✅ **Perfect Entanglement**: Qubits are perfectly correlated!")
                st.info("This is characteristic of Bell states where measurements always match")
            elif results['same_state_prob'] > 0.7:
                st.warning("🔗 **Strong Correlation**: Qubits are highly entangled")
            elif results['same_state_prob'] > 0.5:
                st.info("🔄 **Moderate Correlation**: Some entanglement present")
            else:
                st.error("🔀 **Weak Correlation**: Little to no entanglement")
            
            # Theoretical explanation
            st.markdown("#### 💡 Quantum Insights")
            if apply_h0 and apply_cx:
                if rotation_qubit0 == "none" and rotation_qubit1 == "none":
                    st.write("**Pure Bell State |Φ⁺⟩**")
                    st.write("- Perfect correlation: 50% |00⟩, 50% |11⟩")
                    st.write("- Maximum entanglement")
                else:
                    st.write("**Modified Entangled State**")
                    st.write("- Additional gates modify the entanglement")
                    st.write("- Can create different types of quantum correlations")
            else:
                st.write("**Classical or Partial Entanglement**")
                st.write("- Missing core entanglement gates")
                st.write("- Reduced quantum correlations")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Built with Qiskit ⚛️ | Quantum Correlation Explorer"
    "</div>",
    unsafe_allow_html=True
)