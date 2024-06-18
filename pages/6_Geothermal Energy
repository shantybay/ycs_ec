import streamlit as st
import pandas as pd

st.title('Geothermal Energy')

st.write('---')






st.header(":mailbox: Have your say! :house_with_garden:")

contact_form ="""
<form action="https://formsubmit.co/energy@yukonconservation.ca" method="POST">
     <input type="text" name="name", placeholder ="Your name" optional>
     <input type="email" name="email", placeholder= 'Your email' required>
     <textarea name="message" placeholder="Your messsage"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)


#Use local CSS File

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("pages/style/style.css")
