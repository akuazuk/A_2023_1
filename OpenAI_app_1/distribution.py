import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

st.title("Beta Distribution Density Probability Plot")

a, b = st.slider("Shape parameters", 0.1, 5.0, (1.0, 3.0)), st.slider("Shape parameters", 0.1, 5.0, (1.0, 3.0))

x = np.linspace(0, 1, 100)
y = beta.pdf(x, a, b)

plt.plot(x, y, label='beta pdf')

st.plotly_chart(plt)

prob_range_start, prob_range_end = st.slider("Probability Range", 0.0, 1.0, (0.0, 1.0))

prob_range = np.linspace(prob_range_start, prob_range_end, 100)
prob_area = beta.cdf(prob_range_end, a, b) - beta.cdf(prob_range_start, a, b)

st.write(f"The probability of the range [{prob_range_start}, {prob_range_end}] is: {prob_area:.3f}")

plt.fill_between(prob_range, 0, beta.pdf(prob_range, a, b), alpha=0.5)

st.plotly_chart(plt)

