import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import datetime as datetime
import altair as alt

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

#load data
df_agg = pd.read_csv('Aggregated_Metrics_By_Video.csv').iloc[1:,:]
df_agg_sub = pd.read_csv('Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
df_comments = pd.read_csv('All_Comments_Final.csv')
df_time = pd.read_csv('Video_Performance_Over_Time.csv')


st.header('st.write')

st.write('har har, *mahadev* :sunglasses: ')

st.write(1233345)

#create simple dataframe with 2 coloum
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second colomn': [10,20,30,40]
})

st.write(df)

st.write(df.columns)

st.write('Bholenath' ,df , 'mahadev')

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns= ['a','b','c']
)

c = alt.Chart(df2).mark_bar().encode(
    x='a', y='b', size='c' , color='c' , tooltip=['a','b','c']
)

st.write(c)