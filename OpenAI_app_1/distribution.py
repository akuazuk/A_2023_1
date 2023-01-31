import numpy as np
import scipy.stats as stats
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_background_color='black')

# Define beta distribution
a = st.slider("a", 0.1, 10.0, 1.0)
b = st.slider("b", 0.1, 10.0, 1.0)

x = np.linspace(0, 1, 100)
y = stats.beta.pdf(x, a, b)

# Plot the beta distribution
fig, ax = plt.subplots(figsize=(10, 5), facecolor='black')
ax.plot(x, y, 'red', lw=2)
ax.set_facecolor('black')
st.pyplot(fig)

# Show shaded area under the curve
start, end = st.slider("Probability range", 0, 1, (0.1, 0.9))

# Calculate the area under the curve in the given range
x_range = np.linspace(start, end, 100)
y_range = stats.beta.pdf(x_range, a, b)
area = np.trapz(y_range, x_range)

# Plot the shaded area
fig, ax = plt.subplots(figsize=(10, 5), facecolor='black')
ax.fill_between(x_range, y_range, 0, color='red', alpha=0.5)
ax.plot(x, y, 'red', lw=2)
ax.set_facecolor('black')
ax.annotate(f"P({start:.2f} < X < {end:.2f}) = {area:.2f}", (start + end) 
/ 2, 0.05, color='red', fontsize=14)
st.pyplot(fig)

