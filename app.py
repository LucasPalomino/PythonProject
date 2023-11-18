from PIL import Image
import pandas as pd 
import plotly.express as px
import streamlit as st

st.set_page_config(page_title ="Lab Grown Meat Companies, November 2023",
                  page_icon =":bar_chart:",
                  layout = "centered")

df = pd.read_excel(
    io ='PythonProjectDataset.xlsx',
    engine ='openpyxl',
    sheet_name ='Sheet1',
    usecols ='A:G',
    nrows = 25,
)

# --- Load Assets ---
img_company_logos = Image.open("images/companies.png")

# --- Main Page ---

st.title("Lab Grown Meat Companies, November 2023")
st.markdown("Outlook of companies in the sector of for lab grown meat")
st.image(img_company_logos)
st.button('Go to company overview')
st.dataframe(df)

product_frequency = df['Animal Product'].value_counts()
product_frequency = product_frequency.rename_axis('Animal Product').reset_index(name='Count')
bar_chart = px.bar(product_frequency, x='Animal Product', y='Count', title ='Frequency of Product')
st.plotly_chart(bar_chart)

# --- Side Bar ---
st.sidebar.title('Navigation')

options = st.sidebar.radio('Sort by',
options = ['Animal Product',
           'Country',
           'Funding Stage'])


# --- Visualizations ---
 

if options == 'Animal Prdouct':
    st.write('Working on it')
elif options == 'Country':
    st.write('Hello!')
elif options == 'Funding Stage':
    #show graph filtered by country
    print('tempfile')

# --- Commands to test ---
# streamlit run app.py

