import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

st.title("Beta Distribution Probability Density Function Visualization")

alpha, beta = st.slider("alpha", 1, 10, 1), st.slider("beta", 1, 10, 1)

dist = beta(alpha, beta)

x = np.linspace(0, 1, 100)
y = dist.pdf(x)

st.write("The probability density function of the Beta distribution with alpha =", alpha, "and beta =", beta, "is:")

plt.plot(x, y)
plt.fill_between(x, y, 0, alpha=0.2)
plt.title("Beta Distribution PDF")
plt.xlabel("x")
plt.ylabel("pdf(x)")

st.pyplot()

