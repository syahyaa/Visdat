import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


st.title('Bar Chart')
st.write('kelompok 26')
st.markdown(''' 
            1. Syahidah yuli amaliah
            2. Izzudin ahmad al qosam
            3. Adi Triadi
            ''')

# Data sample
data = {
    'jurusan': ['Informatika', 'Sistem Informasi', 'Teknik Komputer', 'Teknologi Informasi'],
    'jumlah_mahasiswa': [120, 80, 60, 40]
    }

df = pd.DataFrame(data)

# Streamlit bar chart
st.title('Jumlah Mahasiswa per Jurusan')
st.bar_chart(df.set_index('jurusan'))

st.title('Bar Chart dengan Matplotlib')
fig, ax = plt.subplots()
ax.bar(data['jurusan'], data['jumlah_mahasiswa'], color=['skyblue'])
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

st.pyplot(fig)

st.title('Kustomisasi Bar Chart dengan Matplotlib')
fig, ax = plt.subplots()
colors = ['skyblue', 'lightgreen', 'salmon', 'orange']
bars = ax.bar(data['jurusan'], data['jumlah_mahasiswa'], color=colors)
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
            str(bar.get_height()), ha='center')
    
st.pyplot(fig)

# Multiple Bar Chart
st.title('Multiple Bar Chart')
data2023 = [120, 150, 100, 80]
data2024 = [140, 160, 110, 90]

x = range(len(data['jurusan']))
width = 0.4

fig, ax = plt.subplots()
ax.bar(x, data2023, width=width, label='2023', color='skyblue')
ax.bar([p + width/2 for p in x], data2024, width=width, label='2024', color='lightgreen')

ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width/4 for p in x])
ax.set_xticklabels(data['jurusan'])
ax.legend()

st.pyplot(fig)

# Pola dan Trend dengan Bar Chart
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Data jumlah mahasiswa per jurusan selama 5 tahun
data = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Ilmu Komputer': [100, 110, 120, 130, 140],
    'Sistem Informasi': [120, 125, 135, 145, 160],
    'Teknik Informatika': [90, 95, 100, 105, 110],
    'Data Science': [70, 75, 80, 85, 90]
}

# Membuat dataframe
df = pd.DataFrame(data)

# Streamlit App
st.title("Visualisasi Tren Jumlah Mahasiswa Memilih Jurusan Komputer (5 Tahun Terakhir)")

# Filter Tahun
filter_tahun = st.multiselect("Pilih Tahun:", df['Tahun'], default=df['Tahun'])

# Filter Jurusan
jurusan_list = ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science']
filter_jurusan = st.multiselect("Pilih Jurusan:", jurusan_list, default=jurusan_list)

# Filter data berdasarkan input user
filtered_data = df[df['Tahun'].isin(filter_tahun)][['Tahun'] + filter_jurusan]

# Tampilkan tabel
st.subheader("Data Jumlah Mahasiswa")
st.dataframe(filtered_data)

# Bar Chart
st.subheader("Bar Chart dengan Filter")
fig, ax = plt.subplots(figsize=(10, 6))

x = range(len(filtered_data['Tahun']))
width = 0.2

for i, jur in enumerate(filter_jurusan):
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

# Penyesuaian chart
ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks([p + width * len(filter_jurusan) / 2 - width / 2 for p in x])
ax.set_xticklabels(filtered_data['Tahun'])
ax.legend()

# Tampilkan plot di Streamlit
st.pyplot(fig)
