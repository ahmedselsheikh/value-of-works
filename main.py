import pandas as pd
import streamlit as st
import openpyxl

st.set_page_config(layout='wide')

data_frame = openpyxl.load_workbook('data.xlsx')
sheet_names = data_frame.sheetnames
print(sheet_names)
st.sidebar.header("Al-naghi company projects")
project = st.sidebar.selectbox("Select the project", options=sheet_names)

if project in sheet_names:
    df = pd.read_excel('data.xlsx', sheet_name=project, skiprows=4)
    # st.write(df)
    column_names = df.columns.tolist()
    filter_columns = st.sidebar.multiselect('Select Filter Column', options=column_names)
    filtered_df = df.copy()
    for col in filter_columns:
        selected_values = st.sidebar.multiselect(f'select{col}:', options=filtered_df[col].unique())
        filtered_df = filtered_df[filtered_df[col].isin(selected_values)]
    st.write(filtered_df)
    total_value_of_works = round(filtered_df['قيمه اجمالي الاعمال '].sum(), 2)
    total_value_of_current_works = round(filtered_df['الاعمال الحالية'].sum(), 2)
    total_discounts = round(filtered_df['اجمالى الخصومات '].sum(), 2)
    current_discounts = round(filtered_df['خصومات الحالى'].sum(), 2)
    total_current_payable_amount = total_value_of_current_works - current_discounts
    st.dataframe({'البيان': ['اجمالى الأعمال', 'اجمالى الخصومات', 'اجمالى الأعمال الحالية',
                             'اجمالى الخصومات الحالية', 'اجمالى المستحق صرفه الحالى'],
                  'القيمة بالجنيه': [total_value_of_works, total_discounts, total_value_of_current_works,
                                     current_discounts, total_current_payable_amount]
                  }, width=500)

