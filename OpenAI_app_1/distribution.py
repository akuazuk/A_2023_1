import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, beta

st.title("Normal and Beta Distribution Plotter")

# plot normal distribution
mu = st.slider("Mean of Normal Distribution", 0.0, 10.0, 5.0)
sigma = st.slider("Standard Deviation of Normal Distribution", 0.1, 5.0, 
1.0)
normal = norm(mu, sigma)

# plot beta distribution
a = st.slider("Alpha of Beta Distribution", 1.0, 10.0, 1.0)
b = st.slider("Beta of Beta Distribution", 1.0, 10.0, 1.0)
beta_dist = beta(a, b)

while True:
    # plot the distributions
    x = np.linspace(mu-3*sigma, mu+3*sigma, 100)
    normal_pdf = normal.pdf(x)

    x_beta = np.linspace(beta_dist.ppf(0.01), beta_dist.ppf(0.99), 100)
    beta_pdf = beta_dist.pdf(x_beta)

    st.write("#### Normal Distribution")
    plt.plot(x, normal_pdf, label='pdf', color='blue')
    plt.fill_between(x, normal_pdf, 0, color='blue', alpha=0.3)
    plt.legend()
    st.pyplot()

    st.write("#### Beta Distribution")
    plt.plot(x_beta, beta_pdf, label='pdf', color='green')
    plt.fill_between(x_beta, beta_pdf, 0, color='green', alpha=0.3)
    plt.legend()
    st.pyplot()

    mu = st.slider("Mean of Normal Distribution", 0.0, 10.0, mu)
    sigma = st.slider("Standard Deviation of Normal Distribution", 0.1, 
5.0, sigma)
    normal = norm(mu, sigma)

    a = st.slider("Alpha of Beta Distribution", 1.0, 10.0, a)
    b = st.slider("Beta of Beta Distribution", 1.0, 10.0, b)
    beta_dist = beta(a, b)

    if st.button("Re-plot"):
        pass
    else:
        break

