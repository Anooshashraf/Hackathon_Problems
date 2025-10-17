# ==========================================
# Problem 2 – Quantum Coin Game Simulator
# ==========================================

import streamlit as st
import qiskit
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np
import random

# Configure the page
st.set_page_config(
    page_title="Quantum Coin Game Simulator",
    page_icon="🪙",
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
    .win-card {
        background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
    .loss-card {
        background: linear-gradient(135deg, #ff6b6b 0%, #c44d4d 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🪙 Quantum Coin Game Simulator</div>', unsafe_allow_html=True)

# Initialize simulator
sim = AerSimulator()

# Initialize session state
if 'game_results' not in st.session_state:
    st.session_state.game_results = None
if 'games_played' not in st.session_state:
    st.session_state.games_played = 0
if 'wins' not in st.session_state:
    st.session_state.wins = 0
if 'run_game' not in st.session_state:
    st.session_state.run_game = False

# Sidebar for configuration
with st.sidebar:
    st.markdown("### ⚙️ Game Configuration")
    
    st.markdown("---")
    st.markdown("#### 🎯 Player's Strategy")
    player_strategy = st.selectbox(
        "Choose your quantum strategy:",
        ["quantum", "classical"],
        format_func=lambda x: {
            "quantum": "🧬 Quantum Strategy (H gate)", 
            "classical": "📊 Classical Strategy (No gate)"
        }[x]
    )
    
    st.markdown("---")
    st.markdown("#### 🎲 Game Settings")
    num_games = st.slider("Number of Games to Play", 1, 10, 5, help="Number of coin flip games to simulate")
    
    st.markdown("---")
    st.markdown("#### Qiskit Info")
    st.write(f"🔬 Qiskit version: {qiskit.__version__}")
    
    st.markdown("---")
    if st.button("🎮 Play Quantum Coin Game", use_container_width=True):
        st.session_state.run_game = True

# Main content area
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 📋 Game Description")
    
    st.markdown("""
    <div class="info-box">
    <h4 style="color: #000000;">🎯 The Quantum Coin Game:</h4>
    <p style="color: #000000;"><b>Game Rules:</b></p>
    <ol style="color: #000000;">
        <li style="color: #000000;"><b>Setup</b>: Quantum coin starts in |0⟩ state (Heads)</li>
        <li style="color: #000000;"><b>Player's Move</b>: Apply your chosen strategy (quantum or classical)</li>
        <li style="color: #000000;"><b>Referee's Move</b>: Referee applies a random operation (I, X, or H gate)</li>
        <li style="color: #000000;"><b>Measurement</b>: Coin is measured - Heads (0) or Tails (1)</li>
    </ol>
    <p style="color: #000000;"><b>Winning Condition:</b> Coin shows Heads (0) - YOU WIN! 🎉</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Strategy explanations
    st.markdown("### 🎯 Strategy Effects")
    
    strategy_info = {
        "quantum": """
        **🧬 Quantum Strategy (H gate)**:
        - Creates superposition: |0⟩ → (|0⟩+|1⟩)/√2
        - Gives you quantum advantage
        - Higher win probability against referee's moves
        """,
        "classical": """
        **📊 Classical Strategy (No gate)**:
        - Keeps coin in original |0⟩ state
        - No quantum effects
        - Lower win probability
        """
    }
    
    if player_strategy == "quantum":
        st.success(strategy_info["quantum"])
    else:
        st.info(strategy_info["classical"])
    
    # Statistics
    st.markdown("### 📊 Game Statistics")
    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.metric("Games Played", st.session_state.games_played)
    with col_stat2:
        if st.session_state.games_played > 0:
            win_rate = (st.session_state.wins / st.session_state.games_played) * 100
            st.metric("Win Rate", f"{win_rate:.1f}%")

with col2:
    if st.session_state.run_game:
        with st.spinner("🔄 Playing quantum coin games..."):
            try:
                # Initialize game results
                game_history = []
                wins = 0
                
                for game_num in range(num_games):
                    # Create quantum circuit for one coin flip
                    qc = QuantumCircuit(1, 1)
                    
                    # Player's move
                    if player_strategy == "quantum":
                        qc.h(0)  # Apply Hadamard for quantum strategy
                    
                    # Referee's random move
                    referee_move = random.choice(['i', 'x', 'h'])
                    if referee_move == 'x':
                        qc.x(0)
                    elif referee_move == 'h':
                        qc.h(0)
                    # 'i' does nothing (identity)
                    
                    # Measure the coin
                    qc.measure(0, 0)
                    
                    # Run simulation (1 shot per game)
                    job = sim.run(qc, shots=1)
                    result = job.result()
                    counts = result.get_counts()
                    
                    # Determine winner (Heads = 0 = Win)
                    outcome = list(counts.keys())[0]
                    is_win = (outcome == '0')
                    if is_win:
                        wins += 1
                    
                    # Store game result
                    game_history.append({
                        'game_number': game_num + 1,
                        'circuit': qc,
                        'referee_move': referee_move,
                        'outcome': outcome,
                        'is_win': is_win,
                        'counts': counts
                    })
                
                # Store overall results
                st.session_state.game_results = {
                    'game_history': game_history,
                    'total_games': num_games,
                    'wins': wins,
                    'player_strategy': player_strategy,
                    'win_rate': (wins / num_games) * 100
                }
                
                # Update session statistics
                st.session_state.games_played += num_games
                st.session_state.wins += wins
                st.session_state.run_game = False
                
            except Exception as e:
                st.error(f"Error running game simulation: {e}")

    if st.session_state.game_results is not None:
        results = st.session_state.game_results
        
        # Overall results
        st.markdown("### 📊 Game Results Summary")
        
        col_sum1, col_sum2, col_sum3 = st.columns(3)
        with col_sum1:
            st.metric("Total Games", results['total_games'])
        with col_sum2:
            st.metric("Wins", results['wins'])
        with col_sum3:
            st.metric("Win Rate", f"{results['win_rate']:.1f}%")
        
        # Strategy performance
        st.markdown(f"#### 🎯 Performance with { 'Quantum' if results['player_strategy'] == 'quantum' else 'Classical'} Strategy")
        
        if results['win_rate'] > 50:
            st.success(f"🎉 Excellent! Your {results['player_strategy']} strategy is winning!")
        else:
            st.warning(f"💡 Try switching to quantum strategy for better results!")
        
        # Individual game results
        st.markdown("#### 🎮 Individual Game Results")
        
        for game in results['game_history']:
            col_game1, col_game2, col_game3, col_game4 = st.columns([2, 2, 1, 2])
            
            with col_game1:
                st.write(f"**Game {game['game_number']}**")
            
            with col_game2:
                referee_move_name = {
                    'i': 'No Move (I)',
                    'x': 'Flip (X)',
                    'h': 'Superposition (H)'
                }[game['referee_move']]
                st.write(f"Referee: {referee_move_name}")
            
            with col_game3:
                outcome_symbol = "🪙 Heads" if game['outcome'] == '0' else "🪙 Tails"
                st.write(outcome_symbol)
            
            with col_game4:
                if game['is_win']:
                    st.markdown('<div class="win-card">🎉 WIN!</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="loss-card">💥 Loss</div>', unsafe_allow_html=True)
        
        # Circuit visualization for last game
        st.markdown("#### 🔧 Quantum Circuit (Last Game)")
        if results['game_history']:
            last_game = results['game_history'][-1]
            fig_circuit, ax_circuit = plt.subplots(figsize=(8, 3))
            last_game['circuit'].draw('mpl', ax=ax_circuit)
            ax_circuit.set_title(f"Game {last_game['game_number']} Circuit\n(Referee: {last_game['referee_move'].upper()})", 
                               fontsize=12, fontweight='bold')
            plt.tight_layout()
            st.pyplot(fig_circuit)
        
        # Theoretical win probabilities
        st.markdown("#### 📈 Theoretical Analysis")
        
        if results['player_strategy'] == 'quantum':
            st.write("**Quantum Strategy Win Probability:**")
            st.write("- Against I gate: 50%")
            st.write("- Against X gate: 50%") 
            st.write("- Against H gate: 100%")
            st.write("**Overall expected: ~67%** 🚀")
        else:
            st.write("**Classical Strategy Win Probability:**")
            st.write("- Against I gate: 100%")
            st.write("- Against X gate: 0%")
            st.write("- Against H gate: 50%")
            st.write("**Overall expected: ~50%** 📊")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Built with Qiskit ⚛️ | Quantum Coin Game Simulator"
    "</div>",
    unsafe_allow_html=True
)