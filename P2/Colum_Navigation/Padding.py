import streamlit as st
from PIL import Image

img = Image.open(r"D:\Collage\SMT 7\06. Visdat\P2\Aset\4.jpeg")
st.title("Padding")
# Defining Padding with columns 
col1, padding, col2 = st.columns((10,2,10)) 
with col1: 
    col1.image(img)
with col2:
    col2.image(img)