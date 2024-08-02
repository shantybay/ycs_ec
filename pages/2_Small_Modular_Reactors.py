import streamlit as st

st.title("Small Modular Nuclear Reactors ")

with st.container():
    st.subheader('YCS Position Paper Engagement:lightning:')
    st.write('In forming our position papers, YCS would like to hear from you the YCS membership and board to ensure that our views are accurately represented. Included below are some notes around SMRs and some resources. If you have additional resources please submit them along with your comments to the form below')
    st.write('Thank you')
    st.subheader('Pre-operation')
    st.write('Serious concerns around mining practices in Northern Saskatchewan from years of mining uranium and the negative affects that have and continue to affect the habitat')
    st.write('Long haul transportation of materials from mining to refining to the location of the reactor in the Yukon')
    st.write('Long lead times on permitting and construction will make it unfeasible that the technology will be useful given the tight timelines necessary to lower GHG emissions and to reduce reliance of fossil fuels, namely diesel generators')
    st.subheader('Operation')
    st.write('Remote location and employees with very specific skillset will be difficult to attract and retain leaving the operation of the reactor vulnerable to inappropriate care and maintenance')
    st.write('Should an emergency occur, given the remote nature and lack of expertise and experience with this equipment, the emergency could turn catastrophic quickly with devastating consequences.')
    st.write('Very expensive')
    st.write('No GHG at site and no particulate matter for improved local air quality compared to diesel generators or LNG(benefit)')
    st.write('Almost no flexibility in operation (don’t want to get into this). But with the profile of demand curves being extremely variable in smaller communities, based on weather and time of day, a mini nuke does not have the capability for fluctuations, better suited to a consistent industrial operation compared to usage for civilians')
    st.write('If an SMR was in place there would not be a significant customer base in the summer months, therefore the utility would be seeking heavy industrial customers to purchase excess electricity. ')
    st.write('High energy density, small footprint of system therefore potentially less disturbance to the surrounding areas in the construction phase (benefit)')

    st.subheader('Post-operation')
    st.write('Until a reasonable disposal method for radioactive material is presented, the level of potential for significant harm to humans and wildlife is far too great to consider this technology')
    st.write(f'Modularity of units to be able to shipped out in a shipping container offsite is promising, though with the unknown of where the used fuel will be transported to and the risk in transportation along long stretches of highways that are vulnerable to natural disasters or human error in driving operation, leaves for far too great a risk for this technology to be considered viable')
    st.subheader(f'Resources')
    st.write('YG Contracted a consultant to compile the following feasibility report')
    st.write('[YG SMR Feasibility Report >](https://emrlibrary.gov.yk.ca/energy/feasibility-study-of-small-modular-reactors-in-the-yukon-2023.pdf)')
    st.write('Sierra Club Position and Info')
    st.write('[Sierra Club SMR >](https://www.sierraclub.org/iowa/blog/2022/08/small-modular-reactors)')
    st.write('[David Suzuki Foundation Article>](https://davidsuzuki.org/story/burying-radioactive-nuclear-waste-poses-enormous-risks/?utm_source=mkto-none-smSubscribers-readOnline-body&utm_medium=email&utm_campaign=scienceMatters-nuclearWaste-en-02aug2024&mkt_tok=MTg4LVZEVS0zNjAAAAGUsb2vgeRvSRUk5EvYWnzjrn7Y7hqQFvZcuovqBcEgHXykgTlfhZDeu1JdGTs7Xf3NSngAiFni-gPoCC_QBmuiKAWdTfdO8DJW9dbzWZkv4aO_oA)')
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
