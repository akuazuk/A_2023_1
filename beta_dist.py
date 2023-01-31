import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import scipy.stats as stt

st.title("Beta Distribution Plotter")

alpha = st.slider("Alpha", 1, 50, 25, 1)
beta = st.slider("Beta", 1, 50, 25, 1)

beta_dist = stt.beta(alpha, beta)

x = np.linspace(beta_dist.ppf(0), beta_dist.ppf(1), 100)

#st.write("### Alpha =", alpha)
#st.write("### Beta =", beta)

plt.plot(x, beta_dist.pdf(x), 'k', lw=2, color='orange', label='pdf')


plt.plot(x, beta_dist.cdf(x), 'k', lw=2, color='lightgreen', label='cdf')


plt.plot(x, beta_dist.sf(x), 'k', lw=2, color='darkblue', label='sf')

plt.legend()
st.pyplot()

