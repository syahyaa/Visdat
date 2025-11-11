import streamlit as st 
from PIL import Image

#Defining Columns
col1, col2 = st.columns(2)

# Inserting Elements in column 1 
col1.write("First Column") 
col1.image(r"D:\Collage\SMT 7\06. Visdat\P2\Aset\1.jpeg") 
# Inserting Elements in column 2 
col2.write("Second Column") 
col2.image(r"D:\Collage\SMT 7\06. Visdat\P2\Aset\2.jpeg")

# Kelompok 26