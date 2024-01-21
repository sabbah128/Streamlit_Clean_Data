import numpy as np
import pandas as pd
import streamlit as st


st.title("SF Trees")
st.write(
"""This app analyzes trees in San Francisco using
a dataset kindly provided by SF DPW"""
)
trees_df = pd.read_csv("trees.csv")

df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"]).reset_index()

# df_dbh_grouped.columns = ["dbh", "tree_count"]
st.write(df_dbh_grouped)

# st.line_chart(df_dbh_grouped, x="dbh", y="tree_count")