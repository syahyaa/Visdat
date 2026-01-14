import streamlit as st
import matplotlib.pyplot as plt 
import pandas as pd 
from mpl_toolkits.mplot3d import Axes3D

# dataset utama 
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# dataset tambahan
penjualan_weekdays = [70, 80, 90, 95, 100, 110, 115, 120, 130]
penjualan_weekend = [80, 90, 100, 110, 120, 130, 140, 160, 200]

# data untuk analisis
data = {
    'suhu' : [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan_Cokelat' :  [40, 45, 50, 55, 65, 68, 70, 75, 80],
    'Penjualan_Vanila' : [70, 78, 80, 78, 72, 70, 82, 85, 81],
    'Penjualan_Stroberi' : [58, 55, 52, 65, 68, 60, 68, 70, 73],
    'Kelembapan' : [50, 65, 70, 75, 80, 85, 90, 95, 100]
}

# konversi ke dataframe
df = pd.DataFrame(data)

# Layout Utama
st.title('Visualisasi Scatter Plot Penjualan Es Krim')
st.sidebar.header('Pengaturan Visualisasi')

# Menu di sidebar 
option = st.sidebar.selectbox(
    "Pilih contoh scatter plot",
    [
        "Basic Scatter Plot",
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis dengan Scatter Plot",
        "3D Scatter Plot"
    ]
)

# Identitas kelompok 
st.caption("Praktikum 5 - Matplotlib Scatter Plot")
st.markdown("""
Kelompok 26:
1. Syahidah Yuli Amaliah - 0110122220 
2. Izzuddin Ahmad Alqosam - 0110122052
3. Adi Triadi -0110222077
""")

# Basic Scatter Plot   
def basic_scatter():
    st.subheader("Basic Scatter Plot")

    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)

    ax.set_title("Hubungan Penjualan Es Krim dengan Suhu")
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan Es Krim")

    st.pyplot(fig)

# Kustomisasi Scatter Plot 
def custom_scatter():
    st.subheader("Kustomisasi Scatter Plot")

    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange', edgecolors='black')

    ax.set_title("Hubungan Penjualan Es Krim dengan Suhu")
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan Es Krim")
    ax.grid(True)
    ax.legend(["Penjualan"])

    st.pyplot(fig)

# Multiple Scatter Plot 
def multiple_scatter():
    st.subheader("Multiple Scatter Plot")

    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color='green', label='Hari Kerja', s=80)
    ax.scatter(suhu, penjualan_weekend, color='purple', label='Akhir Pekan', s=80)

    ax.set_title('Hubungan Penjualan Es Krim dengan Suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    ax.legend()

    st.pyplot(fig)

# Analisis dengan Scatter Plot
def scatter_3_variabel():
    st.subheader("Analisis dengan Scatter Plot")

    # Opsi jenis es krim
    jenis_eskrim = st.selectbox('Pilih Jenis Es Krim', ['Cokelat', 'Vanila', 'Stroberi'])

    # logika untuk opsi jenis eskrim berdasarkan pilihan
    if jenis_eskrim == 'Cokelat':
        penjualan_jenis = df['Penjualan_Cokelat']
    elif jenis_eskrim == 'Vanila':
        penjualan_jenis = df['Penjualan_Vanila']
    else:
        penjualan_jenis = df['Penjualan_Stroberi']

    st.subheader("Data Penjualan dan Suhu")
    st.dataframe(df)

    # Scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['suhu'], penjualan_jenis, c=df['Kelembapan'], s=100, cmap='coolwarm', alpha=0.7)

    # Styling
    ax.set_title(f'Hubungan Penjualan {jenis_eskrim} vs Suhu dan Kelembapan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
    fig.colorbar(scatter, label='Kelembapan (%)')

    st.pyplot(fig)

    # Ringkasan Hubungan
    st.subheader("Analisis Hubungan")
    st.write(f'Grafik menunjukkan hubungan antara suhu, kelembapan, dan penjualan es krim jenis **{jenis_eskrim}**')

# 3D Scatter Plot

def scatter_3D():
    st.subheader("3D Scatter Plot")

    fig = plt.figure(figsize=(15, 11))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(suhu, penjualan_weekdays, penjualan_weekend, color='orange', s=80, label='Data Penjualan')
    ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Versi 3D)')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Weekdays')
    ax.set_zlabel('Penjualan Weekend')
    ax.legend()

    st.pyplot(fig)

# Routing berdasarkan pilihan menu
if option == "Basic Scatter Plot":
    basic_scatter()
elif option == "Kustomisasi Scatter Plot":
    custom_scatter()
elif option == "Multiple Scatter Plot":
    multiple_scatter()
elif option == "Analisis dengan Scatter Plot":
    scatter_3_variabel()
elif option == "3D Scatter Plot":
    scatter_3D()