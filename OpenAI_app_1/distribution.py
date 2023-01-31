import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, norm

st.set_page_config(page_title="Beta & Normal Distribution Plot", 
page_icon=":chart_with_upwards_trend:", layout="wide")

st.header("Beta & Normal Distribution Plot")

# Create the sliders for Beta distribution
alpha_slider = st.slider("Alpha (Shape 1)", 0.1, 10.0, 1.0, 0.1)
beta_slider = st.slider("Beta (Shape 2)", 0.1, 10.0, 1.0, 0.1)

# Plot the Beta distribution
x = np.linspace(0, 1, 100)
y = beta.pdf(x, alpha_slider, beta_slider)
plt.plot(x, y)

st.pyplot()

# Plot the normal distribution
mean_slider = st.slider("Mean", -5.0, 5.0, 0.0, 0.1)
std_slider = st.slider("Standard Deviation", 0.1, 5.0, 1.0, 0.1)

x = np.linspace(-5, 5, 100)
y = norm.pdf(x, mean_slider, std_slider)
plt.plot(x, y)

st.pyplot()

