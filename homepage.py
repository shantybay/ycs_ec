import streamlit as st
import requests
#from streamlit_lottie import st_lottie


st.set_page_config(
    page_title="Position Paper Development",
    page_icon=":shark",
)



# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code!=200:
#         return None
#     return r.json()

# create figure




#----LOAD ASSETS ----
#lottie_coding = load_lottieurl('https://assets2.lottiefiles.com/private_files/lf30_psn7xxju.json')

st.title("Yukon Conservation Society")
with st.container():
    st.write('---')
    #st.header('Yukon Conservation Society')
    st.write('##')
    left_column, right_column = st.columns((1,2))
    # with left_column:
    #     st_lottie(lottie_coding, height = 300, key ='coding')
    # with right_column:
    st.header("YCS EC Position Paper Development ")
    st.write("YCS is committed to engaging with our membership and board to ensure that our position papers accurately reflect the views of the organization")
    st.write('More Resources and Positions will be posted to this page as we progress')
st.sidebar.success("Select a page above")



# if "my_input" not in st.session_state:
#     st.session_state["my_input"]=""
#
# my_input=st.text_input("Input  text here :evergreen_tree:", st.session_state["my_input"])
# submit=st.button("Submit")
#
# if submit:
#     st.session_state["my_input"]=my_input
#     st.write("You have enetered: ", my_input)
