import streamlit as st
import datetime
import pandas as pd

# form
# Text box
st.title('Text Box')
name = st.text_input('Masukan nama kamu')
st.write('Nama kamu adalah', name)

#________________________________________________________________________________________
# Text Area
input_text = st.text_area('Silahkan Review')
st.write('''Hasil Review Kamu: \n''',input_text)

#________________________________________________________________________________________
# Number Input
num = st.number_input('Masukan Nomor Kamu', 0, 10, 5, 2)
st.write('Nilai Min. 0, \n Nilai Max. 10')
st.write('Nilai Default 5, \n Nilai Langkah 2')
st.write('Nilai setelah menambahkan angka adalah', num)

#________________________________________________________________________________________
# Time
st.title('Time')
st.time_input('Pilih Waktu')

#________________________________________________________________________________________
# Date
st.title('Date')
st.date_input('Pilih Tanggal')
st.date_input('Pilih Tanggal', value=datetime.date(1989, 12, 25), min_value=datetime.date (1987, 1, 1), max_value=datetime.date(2005, 12, 1))

#________________________________________________________________________________________
# Color
st.title('Pilih Warna')
color_code = st.color_picker('Pilih warna yang kamu suka')
st.header(color_code)

#________________________________________________________________________________________
# Data Upload
st.title('CSV Data')
data_file = st.file_uploader('Upload File CSV', type=['csv'])
details = st.button('Check Detail')
if details:
    file_detail = {'File name': data_file.name, 'file_type' : data_file.type, 'file_size' : data_file.size}
    st.write(file_detail)
    df = pd.read_csv(data_file)
    st.dataframe(df)
else:
    st.write('Tidak ada file CSV yang di upload')

#________________________________________________________________________________________
# Submit Button
my_form = st.form(key='form')
a = my_form._text_input(label='Masukan teks')
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)
