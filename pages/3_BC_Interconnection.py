import streamlit as st
import pandas as pd
st.title('BC Interconnection')


#st.write("You have enetered ", st.session_state["my_input"])



# left_column, right_column = st.columns((2,1))
# with left_column:
st.write('---')
st.subheader("Losing Energy Sovereinty ")

st.write("---")

st.subheader('Environmental Disruption')


st.write("---")

st.subheader('Reliability and Resilience')
st.header('Potential Route ')
st.write('place holder map')

st.write("---")


participant_data = pd.DataFrame([[60.7,-135.11],[60.51,-134.33], [60.74,-135.10], [60.71, -135.03], [60.62,-135.0], [60.7,-135.11],\
[60.72,-135.07], [60.70, -135.03], [60.74,-135.10],[60.72,-135.07], [60.72,-135.07],[60.78, -135.07], [60.70, -135.11], \
[60.70, -135.02],[60.52,-134.33],[60.71,-135.09],[60.78,-135.16],[60.71,-135.03], [60.77,-135.10], [60.70, -135.11], [60.78,-135.13]\
,[60.71,-135.05], [60.48,-134.85],],
columns =['latitude', 'longitude'])
#data_of_map = pd.DataFrame(np.random.randn(10, 2) / [60, 60] + [60.7, -135.05],columns = ['latitude', 'longitude'])


st.map(participant_data)





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
