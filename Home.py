import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('The Best Company')
content='''
Societas nostra magnis laudibus ornatur! Excellence in omnibus operibus nostris praestamus et clientibus solida solutio semper praebemus. 
Officia nostra celeriter et summa cura perficiuntur, dum innovatio et integritas sunt fundamenta nostra. Cum optimis in mercatu contendimus, fidelitatem clientium nostri confisi sumus.
Laboramus ut omnes fines superemus et summam qualitatem afferamus. 
Societas nostra non solum mercatus, sed etiam communitates adiuvat, crescens et prosperans una cum eis
'''

st.write(content)

col1, col2, col3 = st.columns(3)

df=pd.read_csv('data.csv')

with col1:
   for index,row in df[:4].iterrows():
        name = f"{row['first name']} {row['last name']}"
        st.subheader(name.title())
        st.write(row['role'])
        st.image('C:/Users/1000490/Desktop/Python/Projects/practice_website/images/' + row['image'])
    
   
        
        
with col2:
   for index,row in df[4:8].iterrows():
        name = f"{row['first name']} {row['last name']}"
        st.subheader(name.title())
        #st.header(row['first name'].capitalize() + ' ' + row['last name'].capitalize())
        st.write(row['role'])
        st.image('C:/Users/1000490/Desktop/Python/Projects/practice_website/images/' + row['image'])
        
with col3:
    for index,row in df[8:].iterrows():
        name = f"{row['first name']} {row['last name']}"
        st.subheader(name.title())
        #st.header(row['first name'].capitalize() + ' ' + row['last name'].capitalize())
        st.write(row['role'])
        st.image('C:/Users/1000490/Desktop/Python/Projects/practice_website/images/' + row['image'])
