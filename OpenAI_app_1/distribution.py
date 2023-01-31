import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

st.set_option('deprecation.showPyplotGlobalUse', False)

α_beta = st.slider('α for Beta distribution', 0.1, 10.0, 2.0)
β_beta = st.slider('β for Beta distribution', 0.1, 10.0, 2.0)

x = np.linspace(0, 1, num=100)
y = beta.pdf(x, α_beta, β_beta)

fig, ax = plt.subplots()
ax.plot(x, y)

lower_bound, upper_bound = st.beta_dist_interval()

if lower_bound:
lower_bound = float(lower_bound)
upper_bound = float(upper_bound)
ax.fill_between(x, 0, y, where=(x >= lower_bound) & (x <= upper_bound), 
color='gray', alpha=0.5)

st.pyplot(fig)
