import pandas as pd 
import plotly.express as px
import streamlit as st

st.set_page_config(page_title ="Lab Grown Meat Companies, November 2023",
                  page_icon =":bar_chart:",
                  layout = "centered")

data_file = pd.read_excel(
    io = 'PythonProjectDataset.xlsx',
    engine = 'openpyxl',
    sheet_name = 'Sheet1',
    usecols= 'A:G',
    nrows = 25,
)

# --- Main Page ---

st.title("Lab Grown Meat Companies, November 2023")    # Title
st.markdown("Outlook of companies in the sector of for lab grown meat")   # Inserts new paragraph
st.dataframe(data_file)

# --- visualizations ---
product_type = data_file.groupby(by=["Animal Product"])
st.dataframe(product_type)

# --- Commands to test ---
# streamlit run app.py

