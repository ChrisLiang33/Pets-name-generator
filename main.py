import langchain_helper as lch
import streamlit as st

st.title('pets name generator')

user_animal_type = st.sidebar.selectbox('what is your pet', ('cat', 'dog', 'cow'))

if user_animal_type == 'cat':
    user_pet_color = st.sidebar.text_area('what color is your cat', max_chars=15)
if user_animal_type == 'dog':
    user_pet_color = st.sidebar.text_area('what color is your dog', max_chars=15)
if user_animal_type == 'cow':
    user_pet_color = st.sidebar.text_area('what color is your cow', max_chars=15)
  
if user_pet_color:
    response = lch.generate_pet_name(user_animal_type, user_pet_color)
    st.text(response['pet_name'])