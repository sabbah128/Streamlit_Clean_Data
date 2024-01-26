import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie


st.title('This is a test for learning Streamlit.')
st.markdown('and this is a markdown function.')
st.write('and this is a markdown function.')

list_mean = []
prec_heads = st.number_input(label='Chance of coins lnding on Heads',
                             min_value=0.0, max_value=1.0, value=0.5)

title = st.text_input('Graph Title')

if title == '':
    title = 'Default'

binom = np.random.binomial(1, prec_heads, 1000)

for i in range(10000):
    list_mean.append(np.random.choice(binom, 500, replace=True).mean())

fig1, ax1 = plt.subplots(figsize=(5, 4))
plt.hist(list_mean, range=[0, 1])
plt.title(title)
st.pyplot(fig1)

