import streamlit as st
import time

# Membuat Button
st.title('Creat Radio Buttons')
gender = st.radio(
    'Silahkan Pilih Jenis Kelamin',
    ('Laki-Laki', 'Perempuan', 'Other')
)
# Perkondisian 
if gender == 'Male':
    st.write('Kamu telah memilih Laki-Laki')
elif gender == 'Famale':
    st.write('Kamu telah memilih Perempuan')
else:
    st.write('Kamu memilih yang lain')
    
#________________________________________________________________________________________
# Membuat Check Boxes
st.title('Membuat Checkboxes')
st.write('Silahkan Pilih Hobbi')
# Pilihan Chack Boxes
check_1 = st.checkbox('Membaca Buku')
check_2 = st.checkbox('Menonton Film')
check_3 = st.checkbox('Olahraga')

#________________________________________________________________________________________
# Membuat Drop-Downs
st.title('Membuat Dropdown')
hobby = st.selectbox('Pilih hoby kamu: ',('Membaca Buku', 'Menonton Film', 'Olahraga'))

#________________________________________________________________________________________
# Multi select
st.title('Multi Select')
hobbies = st.multiselect('Apa hobi kamu?', ['Membaca Buku', 'Menonton Film', 'Olahraga', 'Bermain game'],['Membaca Buku', 'Bermain game'])

#________________________________________________________________________________________
# Download Button
st.title('Download button')
down_btn = st.download_button(
    label='Download Image', data=open(r'D:\Collage\SMT 7\06. Visdat\P1\Aset\1.jpeg', 'rb'),file_name='Freediving.jpeg', mime='image/jpeg'
) #rb untuk membaca nama file yg ada angkanya jdi binary/text

#________________________________________________________________________________________
# Progres Bars
st.title('Progres Bar')
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

#________________________________________________________________________________________
# Spinners
st.title('Spinner')
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hallo Data Analis')

