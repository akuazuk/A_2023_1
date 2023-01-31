import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, beta

st.title("Normal and Beta Distribution Plotting App")

mu = st.sidebar.slider("Mean", -10, 10, 0)
sigma = st.sidebar.slider("Standard Deviation", 0.1, 10.0, 1.0)
a = st.sidebar.slider("a (Beta Distribution)", 1, 100.0, 1.0)
b = st.sidebar.slider("b (Beta Distribution)", 1, 100.0, 1.0)
prob = st.sidebar.slider("Probability (for Beta Distribution)", 0.0, 1.0, 
0.5, step=0.01)

x = np.linspace(-10, 10, num=100)
normal = norm.pdf(x, mu, sigma)
beta_dist = beta.pdf(x, a, b)

beta_range = beta.ppf([prob, 1-prob], a, b)

st.write("## Normal Distribution")
st.line_chart(normal)

st.write("## Beta Distribution")
st.line_chart(beta_dist)
st.write("Beta Distribution range for given probability: [%.2f, %.2f]" % 
(beta_range[0], beta_range[1]))

if st.button("Update Plot"):
    beta_range = beta.ppf([prob, 1-prob], a, b)
    st.write("Beta Distribution range for given probability: [%.2f, %.2f]" 
% (beta_range[0], beta_range[1]))

