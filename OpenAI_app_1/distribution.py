import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

st.title("Beta Distribution Interactive Plot")

alpha_slider = st.slider("Alpha (α) Value", 1, 10, 1)
beta_slider = st.slider("Beta (β) Value", 1, 10, 1)

alpha, beta = alpha_slider, beta_slider
x = np.linspace(0, 1, 100)
y = beta.pdf(x, alpha, beta)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot()

prob_slider = st.slider("Probability", 0, 1.0, 0.5)

prob = prob_slider
lower_bound, upper_bound = beta.ppf([prob, 1 - prob], alpha, beta)

st.markdown(f"Range of probabilities with {100 * prob:.0f}% confidence:")
st.markdown(f"Lower bound: {lower_bound:.2f}")
st.markdown(f"Upper bound: {upper_bound:.2f}")
