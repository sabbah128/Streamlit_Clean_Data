import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
# from st_aggrid import AgGrid
# import requests
from streamlit_lottie import st_lottie
import json


@st.cache_data()
def load_df(penguin_file):
    if penguin_file is not None:
        penguins_df = pd.read_csv(penguin_file)
    else:
        st.write('Data has not inserted yet!')
        st.stop()
    return penguins_df

# def load_lottieurl(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

st.title("Palmer's Penguins")

# lottie_penguin = load_lottieurl(
#     "https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json")

with open('penguin.json', 'r') as f:
    data = json.load(f)
st_lottie(data, height=200)

st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

penguins_df = load_df(st.file_uploader('Select Your Local Penguins CSV'))

# AgGrid(penguins_df, height=300, fit_columns_on_grid_load=True)
st.dataframe(penguins_df, use_container_width=True)
selected_x_var = st.selectbox('What do you want the x variable to be?', 
                            ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?', 
                            ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g'])
selected_gender = st.selectbox('What gender do you want to filter for?',
                                ['All genguins', 'Male penguins', 'Female penguins'])

if selected_gender == 'Male penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
    shape_sex = 'triangle'
elif selected_gender == 'Female penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
    shape_sex = 'square'
else:
    shape_sex = 'circle'

alt_chart = (alt.Chart(penguins_df,                       
                       title="Scatterplot of Palmer's Penguins")
                       .mark_point(shape=shape_sex)
                       .encode(x=selected_x_var, y=selected_y_var, color="species",)
                       .interactive())

st.altair_chart(alt_chart, use_container_width=True)