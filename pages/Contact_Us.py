import streamlit as st

st.header('Contact Me!')

with st.form(key='email_forms'):
    user_email = st.text_input('Enter your email address')
    message =  st.text_area('Your message here please')
    button = st.form_submit_button( )
    
    if button:
        message = message + user_email
        