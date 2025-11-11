import streamlit as st 
import numpy as np 
st.title("Contaiher")
with st.container():

    st.write("Element Inside Contianer") 
    # Defining Chart Element 
    st.line_chart(np.random.randn(40, 4)) 
    st.write("Element Outside Container")


import streamlit as st 
import numpy as np 
st.title("Out of Onder Container")
# Defining Contianers
container_one = st.container()
container_one.write("Element One Inside Contianer") 
st.write("Element Qutside Contianer") 
# Now insert few more elements in the container_one 
container_one.write("Element Two Inside Contianer")
container_one.line_chart(np.random.randn(40, 4))