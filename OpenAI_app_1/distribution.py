import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

def plot_distribution(distribution_type, a, b):
    if distribution_type == 'Normal':
        mu = 0
        sigma = 1
        s = np.random.normal(mu, sigma, 1000)
        count, bins, ignored = plt.hist(s, 30, density=True)
        plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - 
mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
        plt.title('Normal Distribution')
        plt.xlabel('X')
        plt.ylabel('Probability')
    else:
        x = np.linspace(0, 1, 1000)
        beta = np.random.beta(a, b, 1000)
        count, bins, ignored = plt.hist(beta, 30, density=True)
        y = (x**(a-1)) * ((1-x)**(b-1)) / (b ** (a+b-1) / ((a-1)*(b-1)))
        plt.plot(x, y, linewidth=2, color='r')
        plt.title('Beta Distribution')
        plt.xlabel('X')
        plt.ylabel('Probability')
    return plt

distribution_type = st.sidebar.selectbox("Select Distribution Type", 
["Normal", "Beta"])

if distribution_type == 'Beta':
    a = st.sidebar.slider("a", 0, 10, 1)
    b = st.sidebar.slider("b", 0, 10, 1)

fig, ax = plt.subplots()
plot = plot_distribution(distribution_type, a, b)
st.pyplot(fig)

