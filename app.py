from PIL import Image
import pandas as pd 
import plotly.express as px
import streamlit as st

# Page Configuration
st.set_page_config(page_title = 'Lab Grown Meat Companies, November 2023',
                  page_icon = ':bar_chart:',
                  layout = 'centered')

# Importing Data
dataset = pd.read_excel(
    io = 'PythonProjectDataset.xlsx',
    engine = 'openpyxl',
    sheet_name = 'Sheet1',
    usecols = 'A:H',
    dtype={'Year Founded': str},
    nrows = 25)

# Loading image
company_logos = Image.open('images/companies.png')

# Side Bar options
animal_product_options = dataset['Animal Product'].unique()
country_options = dataset['Country'].unique()
funding_stage_options = dataset['Funding Stage'].unique()

# Sidebar selection boxes
st.sidebar.title('Filter Selection')
animal_product = st.sidebar.selectbox('Animal Product', options=['(No Selection)'] + list(animal_product_options))
country = st.sidebar.selectbox('Country', options=['(No Selection)'] + list(country_options))
funding_stage = st.sidebar.selectbox('Funding Stage', options=['(No Selection)'] + list(funding_stage_options))

# Filtering the dataset based on user selection
filtered_dataset = dataset

if animal_product != '(No Selection)':
    filtered_dataset = filtered_dataset[filtered_dataset['Animal Product'] == animal_product]

if country != '(No Selection)':
    filtered_dataset = filtered_dataset[filtered_dataset['Country'] == country]

if funding_stage != '(No Selection)':
    filtered_dataset = filtered_dataset[filtered_dataset['Funding Stage'] == funding_stage]


# Creating plotly visualizations
def calculate_frequency(dataframe):
    count_list = filtered_dataset[dataframe].value_counts().reset_index()
    return(count_list)

# Bar Chart
product_frequency = calculate_frequency('Animal Product')
bar_chart = px.bar(product_frequency, 
                   x = 'Animal Product', 
                   y = 'count', 
                   labels = {'count' : 'Number of Companies'},
                   title = 'Type of Product by Company')

# Bubble Chart
year_frequency = calculate_frequency('Year Founded')
bubble_chart = px.scatter(year_frequency, 
                          x ='Year Founded', 
                          y = 'count',
                          range_y = [0,7],
                          labels ={'count' : 'Number of Companies'},
                          title = 'Company Year Founded')

# Geo Map
geo_data = filtered_dataset.drop_duplicates(subset = 'Company Name')
company_location = px.scatter_geo(geo_data, 
                     labels = 'City',
                     lat = 'Latitude', 
                     lon = 'Longitude',
                     color = 'Country',
                     title = 'Company Location',
                     template = 'plotly')

# Adding elements to page
st.title('Cell-Based Meat Companies')

st.markdown('---')

st.image(company_logos)

st.markdown('---')

st.subheader('A small sample of companies creating meat from cell cultures.')

st.markdown('''This dashboard contains information about 20 companies as of November 2023.
            The interactive boxes allow to filter the data displayed in the visualizations below.
            The source code is uploaded [here](https://github.com/LucasPalomino/PythonProject).''')

st.markdown('---')

st.plotly_chart(company_location, use_container_width = True)

st.markdown('---')

# Adding graphs in columns
col1, col2 = st.columns(2)
col1.plotly_chart(bar_chart, use_container_width = True)
col2.plotly_chart(bubble_chart, use_container_width = True)

# Displaying dataset table without coordinates
st.dataframe(filtered_dataset.drop(columns = ['Latitude', 'Longitude']))

st.markdown('---')