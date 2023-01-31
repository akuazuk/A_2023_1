import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stt

st.title("Beta Distribution Plotter")

alpha = st.slider("Alpha", 0.1, 5.0, 2.0, 0.1)
beta = st.slider("Beta", 0.1, 5.0, 2.0, 0.1)

beta_dist = stt.beta(alpha, beta)

x = np.linspace(beta_dist.ppf(0.01), beta_dist.ppf(0.99), 100)

st.write("## Beta PDF")
st.write("### Alpha =", alpha)
st.write("### Beta =", beta)

plt.plot(x, beta_dist.pdf(x), 'k-', lw=2, label='frozen pdf')

st.write("## Beta CDF")
st.write("### Alpha =", alpha)
st.write("### Beta =", beta)

plt.plot(x, beta_dist.cdf(x), 'k--', lw=2, label='frozen cdf')

st.write("## Beta SF (Survival Function)")
st.write("### Alpha =", alpha)
st.write("### Beta =", beta)

plt.plot(x, beta_dist.sf(x), 'k:', lw=2, label='frozen sf')

plt.legend()
st.pyplot()

