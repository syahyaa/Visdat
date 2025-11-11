import streamlit as st

# Teks element
# st.title('Ini judul')
# st.header ('ini header') #header
# st.subheader ('ini sub header') #sub header
# st.text('ini teks biasa') #teks polos
# st.markdown('**ini teks boald** dan *ini teks italic*') #teks bold dan italic
# st.markdown('''
#             - baris 1 (bullet list)
#             1. baris 2 (Number list)
#             * baris 3 (bullet list)
#             ''')
# st.caption('caption gambar') #caption gambar


# Praktikum mandiri
st.text('__________________________________________')
st.title('Praktikum 1 Visdat')
st.subheader('Identitas Mahasiswa')
st.markdown('''
            - Nama : Syahidah Yuli Amaliah
            - Nim : 0110122220
            - Mk : Visualisasi Data
            ''')

# Menampilkan Rumus
st.markdown("<h2 style='text-align: center;'>Menulis Rumus Matematika</h2>", unsafe_allow_html=True)
st.latex(r'''\cos^2\theta =1-2\sin^2\theta ''') #Trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 +2ab ''') #kuadrat binominal

# Menyimpan code
st.markdown('Menampilkan code')
st.header('Displaying Code')
st.subheader('Python code')

# simpan ke varible
code = ''''
def hello():
    print('hello, streamlit!)
'''
st.code(code, language='python')

# Menampilkan code java
st.subheader('Java code')
st.code(''' 
        public class GFG {
            public static void main(string arg[]){
                System.out.printIn('Hallo Word!);
            }
        }
        ''', language='Java')
# Fungsi st.code bida di gunakan untuk bahasa lain

st.subheader('JavaScript code')
st.code(''' 
        <p id='demo'></p>
        <script>
        try {
            addalert('Wellcome guest!'); // Kesalahan ketik (addalaert)
            sengaja dibuat untuk menimbulkan error
        }
        catch(err) {
            document.getElemantById('demo').innerHTML = err.message; // menampilkan pesan error di elemen HTML dengan id 'demo'
        }
        </script>
        ''', language='Java')
# Fungsi st.code bida di gunakan untuk bahasa lain




