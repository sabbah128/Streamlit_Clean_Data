import pandas as pd
import numpy as np
import streamlit as st
import matplotlib


url = '.\Final_TPA_data.xlsx'
df = pd.read_excel(st.file_uploader('Insert your file:', type=["csv", "xlsx", "txt"]))
st.write(df.head(7))