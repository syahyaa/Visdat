import streamlit as st
from PIL import Image

img = Image.open(r"D:\Collage\SMT 7\06. Visdat\P2\Aset\1.jpeg")
st.title("Grid")
# Defining no of Rows
for a in range(4):
# Defining no. of columns with size
    cols = st.columns((1, 1, 1,1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)