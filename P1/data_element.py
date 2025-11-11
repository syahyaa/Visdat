import streamlit as st
import pandas as pd #mengelola data frame (table)
import numpy as np #Data numerik
import altair as alt #diagram chart

# identitas Kelompok
st.title('Identitas Kelompok')
st.subheader('Kelompok 26')
st.markdown('''
            Anggota 1
            - Nama : Syahidah Yuli Amaliah
            - Nim : 0110122220
            - Roll : Data Element dan Data Media
            
            Anggota 2
            - Nama : Izzuddin Ahmad Alqosam
            - Nim : 0110122052
            - Roll : Text Element dan Form
            
            Anggota 3
            - Nama : Adi Triadi
            - Nim : 110222077
            - Roll : Button
            
            ''')

# _______________________________________________________________________________________________
st.markdown("<h2 style='text-align: center;'>Data Frame</h2>", unsafe_allow_html=True)
# st.subheader('Data Frame')
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)
st.dataframe(df) #menampilkan data

# Menampilkan highligt nilai minimum
st.subheader('Highligth minimum value data frame')
st.dataframe(df.style.highlight_min(axis=0))

# _______________________________________________________________________________________________
# Table statis
st.subheader('Table Statis')
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)
# Menampilkan table statis
st.table(df)

# _______________________________________________________________________________________________
# Matrics: komponen tampilan angka penting
st.header('Matrics')
st.metric(label='Temperature', value='31 c', delta='1.2 c')

# matric sesuai delta_color
cal1, cal2, cal3 = st.columns(3)

# Menampilkan idikator data
cal1.metric('curah hujan', '100 cm', '10 cm') #naik baik
cal2.metric(label='povulasi', value='125 miliar', delta='1 miliar', delta_color='inverse') #naik tapi buruk
cal3.metric(label='pelanggan', value=100, delta=10, delta_color='off') #netral

# menampilkan metric
st.metric(label='speed', value=None, delta=0) #kosong / naik baik di settingan default
st.metric('Treets', '91456', '-1132649') #penurunan

# _______________________________________________________________________________________________
# The write() Function as a Superfunction
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)
st.write('Here is our data', df, 'Data is in Dataframe format.\n', '\nWrite is super function')

# Defining chart 
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns = ['a','b']
)
chart = alt.Chart(df).mark_bar().encode(x='a', y='b', tooltip=['a','b'])
st.write(chart)

# _______________________________________________________________________________________________
# Math calculations with no functions defined
"Adding 5 & 4 =", 5 + 4
# Displaying Variable 'a' and its value
a = 5
'a', a

# Markdown with Magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""

# Dataframe using magic
import pandas as pd
df = pd.DataFrame({'col': [1, 2]})
'dataframe', df

# Magic working on Charts
import matplotlib.pyplot as plt 
import numpy as np

s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)

# Magic chart
"chart", chart

