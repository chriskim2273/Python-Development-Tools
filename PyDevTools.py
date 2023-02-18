import streamlit as st
st.text_input("Separable Text", key="text")
article_list = []
for link in st.session_state.text.split(" "):
    article_list.append(link)

article_list