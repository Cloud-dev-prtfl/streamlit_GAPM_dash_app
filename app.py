import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')

# Page Title
st.markdown('## GAPMINDER Dashbord')

# SideBar   
st.sidebar.subheader("GAPMINDER Dashbord",divider='blue')


df = pd.read_csv('gapminder_data_graphs.csv')

# Computation 
unique_years = df['year'].unique()

print(unique_years)


# Add dropdown 

selected_year = st.selectbox(label="Year",
                             options=unique_years)

df_plot = df[df['year']==selected_year]

##st.write(df_plot)

average_gdp = round(df_plot['gdp'].mean(),2)
average_life_exp = round(df_plot['life_exp'].mean(),2)
average_hdi = round(df_plot['hdi_index'].mean(),2)

# Add 3 columns and metric widget
col1,col2,col3 = st.columns([1,1,1],border=True)
col1.metric(label='Average GDP', value=average_gdp)
col2.metric(label='Average Life Expectancy', value=average_life_exp)
col3.metric(label='Average HDI', value=average_hdi)

# Add the scatter plot 
title = 'Plot of GDP vs Life expectancy for year {}'.format(selected_year)
scatter_plot = px.scatter(data_frame=df_plot,x='gdp',y='life_exp',color='continent',title=title)
st.plotly_chart(scatter_plot)


# Add boxplot and columns 
col4,col5 = st.columns(2,border=True)
boxplot1 = px.box(data_frame=df_plot,x='continent',y='gdp',title='Distribution of the GDP across the diffrent continent year {}'.format(selected_year))
histo_gdp = px.histogram(data_frame=df_plot,x='gdp',title='Distribution of the GDP across the diffrent continent year {}'.format(selected_year))

col4.plotly_chart(boxplot1,use_container_width=True)
col5.plotly_chart(histo_gdp,use_container_width=True)

col6,col7 = st.columns(2,border=True)

boxplot3 = px.box(data_frame=df_plot,x='continent',y='hdi_index',title='Distribution of the HDI across the diffrent continent year {}'.format(selected_year))
histo_hdi = px.histogram(data_frame=df_plot,x='hdi_index',title='Distribution of the HDI across the diffrent continent year {}'.format(selected_year))

col6.plotly_chart(boxplot3,use_container_width=True)
col7.plotly_chart(histo_hdi,use_container_width=True)




