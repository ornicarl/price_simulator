from pypmml import Model
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

model = Model.load("model_Classification_of_REG_CodeINSEE.xml")

st.text_input(label='BEH_TypeGarage')

model.predict(['OTHER',
 'APARTMENT',
 'LESSEE',
 '28',
 '124',
 '0',
 '8',
 '-1',
 'NO_ANTECEDENT',
 '100.00',
 '100',
 '20000',
 'RC',
 '75120',
 'IDS',
 '29',
 '55',
 '171',
 '6',
 'BER'])