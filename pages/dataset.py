import streamlit as st
import pandas as pd

def main():
    st.title("📊 View Your Dataset")
    st.write("Upload your dataset to view it here.")

    # File uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        try:
            # Read and display the dataset
            data = pd.read_csv(uploaded_file)
            st.subheader("Dataset Preview")
            st.write(data.head())

            # Show dataset info
            st.subheader("Dataset Information")
            st.write(data.describe())

            st.write(f"**Number of Rows:** {data.shape[0]}")
            st.write(f"**Number of Columns:** {data.shape[1]}")
        except Exception as e:
            st.error(f"Error loading dataset: {e}")
