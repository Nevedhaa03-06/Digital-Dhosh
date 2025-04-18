# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qfB4WOY367xya6UvodPqKGLDCYVLUjUy
"""



import streamlit as st
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

# Load Excel data
@st.cache_data
def load_data():
    df = pd.read_excel("S_V_P_K.xlsx")
    return df

def smooth_signal(signal, window_length=11, polyorder=3):
    return savgol_filter(signal, window_length, polyorder)

# Streamlit App
st.title("Ayurvedic Pulse Data Visualization")

df = load_data()

if df is not None:
    st.subheader("Raw Data Preview")
    st.write(df.head())

    # Assuming columns are named exactly as 'Vata', 'Pitta', 'Kapha'
    for dosha in ['Vata', 'Pitta', 'Kapha']:
        if dosha in df.columns:
            st.subheader(f"{dosha} Pulse Waveform")

            raw_signal = df[dosha].dropna().values
            smoothed_signal = smooth_signal(raw_signal)

            fig, ax = plt.subplots()
            ax.plot(raw_signal, label="Raw", alpha=0.5)
            ax.plot(smoothed_signal, label="Smoothed", linewidth=2)
            ax.set_title(f"{dosha} Pulse")
            ax.legend()
            st.pyplot(fig)
        else:
            st.warning(f"{dosha} column not found in the dataset.")