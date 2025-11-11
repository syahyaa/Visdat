import streamlit as st
import base64
from PIL import Image

# Image
st.markdown("<h2 style='text-align: center;'>Menampilkan Gambar</h2>", unsafe_allow_html=True)
st.write("Menampilkan Gambar")
# Menampilkan gambar dengan menentukan path file
st.image(r"D:\Collage\SMT 7\06. Visdat\P1\Aset\4.jpeg",width=150)
# Sumber gambar dari Unsplash
st.write("Sumber Gambar: https://www.pinterest.com/")

# Menampilkan beberapa gambar sekaligus
st.write("Menampilkan Beberapa Gambar")

# Daftar file gambar hewan
animal_images = [
    r"D:\Collage\SMT 7\06. Visdat\P1\Aset\1.jpeg",
    r"D:\Collage\SMT 7\06. Visdat\P1\Aset\2.jpeg",
    r"D:\Collage\SMT 7\06. Visdat\P1\Aset\3.jpeg",
]

# Menampilkan beberapa gambar dengan lebar 150 piksel
st.image(animal_images, width=150) #gambarnya berurut kesamping
# gambarnya berurut ke bawah
# st.image(animal_images[0], width=150)
# st.image(animal_images[1], width=150)
# st.image(animal_images[2], width=150)

# Sumber gambar dari Unsplash
st.write("Sumber Gambar: https://www.pinterest.com/")

# ________________________________________________________________________________________
# Background Image
st.markdown("<h2 style='text-align: center;'>Background</h2>", unsafe_allow_html=True)
# Fungsi untuk mengatur gambar sebagai latar belakang
def add_local_background_image(image):
    # Membuka file gambar dalam mode biner
    with open(image, "rb") as img:
        # Mengubah gambar menjadi string base64
        encoded_string = base64.b64encode(img.read())

    # Menampilkan keterangan sumber gambar
    st.write("Sumber Gambar: https://www.pinterest.com/")

    # Menambahkan kode CSS untuk menampilkan gambar sebagai latar belakang
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Menampilkan teks keterangan
st.write("Gambar Latar Belakang")

# Memanggil fungsi untuk menampilkan gambar latar belakang
add_local_background_image(r"D:\Collage\SMT 7\06. Visdat\P1\Aset\5.jpeg")

# ________________________________________________________________________________________
# Resize Image
# Membuka gambar asli dari path
original_image = Image.open(r"D:\Collage\SMT 7\06. Visdat\P1\Aset\3.jpeg")

# Menampilkan gambar asli
# st.title("Gambar Asli")
st.markdown("<h2 style='text-align: center;'>Gambar Asli</h2>", unsafe_allow_html=True)
st.image(original_image)

# Mengubah ukuran gambar menjadi 600x400 piksel
resized_image = original_image.resize((1000, 250))

# Menampilkan gambar yang sudah diubah ukurannya
# st.title("Gambar Setelah Diubah Ukurannya")
st.markdown("<h2 style='text-align: center;'>Gambar setelah diubah ukuran</h2>", unsafe_allow_html=True)
st.image(resized_image)

# syahidah yuli amaliah-0110122220
