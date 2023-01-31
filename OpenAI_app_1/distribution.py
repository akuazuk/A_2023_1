import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

st.set_page_color(background_color='black')

st.title("Beta Distribution")

a = st.slider("a", 0.01, 10.0)
b = st.slider("b", 0.01, 10.0)

x = np.linspace(stats.beta.ppf(0.01, a, b), stats.beta.ppf(0.99, a, b), 
100)

fig, ax = plt.subplots()
ax.plot(x, stats.beta.pdf(x, a, b), 'k-', lw=5, alpha=0.6, label='beta 
pdf')
st.pyplot(fig)

prob = st.slider("prob", 0.0, 1.0)

x = np.linspace(stats.beta.ppf(0.01, a, b), stats.beta.ppf(prob, a, b), 
100)

fig, ax = plt.subplots()
ax.fill_between(x, stats.beta.pdf(x, a, b), 0, color='#5fba7d', alpha=0.5)
ax.plot(x, stats.beta.pdf(x, a, b), 'k-', lw=5, alpha=0.6, label='beta 
pdf')
st.pyplot(fig)

