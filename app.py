import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


@st.cache
def extractyear(data, year):
    return data[data['sampleYear']==year]

@st.cache
def loaddata():
    return pd.read_csv('ASL_small.csv', usecols = ["Species", "sampleYear", "Length"])

st.title("Salmon Data")

#open datafile
data_small = loaddata()

st.header("Salmon Lengths by Year")
pickyear = st.selectbox("Select a Year", np.sort(data_small['sampleYear'].unique())[:-1])

yeardata = extractyear(data_small, pickyear)

fig, ax = plt.subplots(figsize=(8,6))


for s in yeardata['Species'].unique():
    species = yeardata[yeardata['Species']==s]
    species = species[species['Length'] < 1500]
    ax.hist(species['Length'], label = s, bins = 30, histtype='step', density=True, linewidth=2)
ax.legend(loc=2, fontsize = 12)
ax.set_xlabel('Length (mm)', fontsize = 12)
ax.set_ylabel('Probability Density', fontsize = 12)
ax.set_xlim(0, 1500)

st.write(fig)
