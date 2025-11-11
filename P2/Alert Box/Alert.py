import streamlit as st
import logging

st.success("This is a success alert!")
st.warning("This is a warning alert!")  
st.info("This is an info alert!")
st.error("This is an error alert!")
# st.exception("This is an exception alert!")
try:
    1 / 0
except Exception as e:
    st.error("This is an exception alert!")
    logging.exception("Exception occurred")