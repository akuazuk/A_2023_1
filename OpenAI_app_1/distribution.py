import streamlit as st
import numpy as np
from scipy.stats import beta

def plot_beta_pdf(a, b, x, y_min, y_max):
    x_grid = np.linspace(x.min(), x.max(), 250)
    pdf = beta.pdf(x_grid, a, b)
    
    return st.area_chart(pdf, x_grid, y_min=y_min, y_max=y_max)

a = st.slider("a", 0.1, 10.0, 2.0, step=0.1)
b = st.slider("b", 0.1, 10.0, 2.0, step=0.1)
x = np.linspace(0, 1, 100)

plot_beta_pdf(a, b, x, 0, 5)
