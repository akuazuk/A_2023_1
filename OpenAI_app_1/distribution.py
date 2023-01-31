import random
import streamlit as st

st.title("Two Dice Rolling Simulator")

def simulate_rolls(num_rolls):
    num_sixes = 0
    for i in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == 6 and dice2 == 6:
            num_sixes += 1
    return num_sixes

# Initialize the number of rolls and runs
num_rolls = st.slider("Number of rolls per simulation", min_value=1, max_value=1000, value=100, step=1)
num_runs = st.slider("Number of simulations", min_value=1, max_value=1000, value=100, step=1)

if st.button("Roll Dice"):
    result = simulate_rolls(num_rolls)
    total_sixes = 0
    for i in range(num_runs):
        total_sixes += simulate_rolls(num_rolls)
    st.write("After", num_rolls * num_runs, "rolls, the average number of sixes is:", total_sixes/num_runs)
    st.write("The a posteriori probability of getting two sixes is:", total_sixes/(num_rolls * num_runs))

