#library
import streamlit as st
import matplotlib.pyplot as plt 

#dataset (data sample)
month = ['jan', 'feb', 'mar', 'apr', 'mei', 'jun', 'jul', 'aug', 'sep', 'okt', 'nov', 'des']
product_a_sales = [10, 20, 15, 25, 30, 45,40, 50, 60, 55, 65, 70]
product_b_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# Layout streamlit
st.title('Visualisasi penjualan produk')
st.subheader('Pengaturan Grafik')
option = st.sidebar.selectbox('Pilih tipe visualisasi', ('Single line plot', 'multiple & customization', 'jenis garis untuk menunjukan tren', 'subplot'))


# single line plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(month, product_a_sales, label='Product A')
    ax.set_title ('Penjualan produk A perbulan')
    ax.set_xlabel('bulan')
    ax.set_ylabel('penjualan')
    st.pyplot(fig)
    
# multiple line
def customimize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(month, product_a_sales, label = 'product A', linestyle ='--', marker = 'o', color= 'blue')
    ax.plot(month, product_b_sales, label = 'product B', linestyle ='-', marker = 'x', color= 'red')

    ax.set_title ('Penjualan produk perbulan')
    ax.set_xlabel('bulan')
    ax.set_ylabel('penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    
# Data sample
product_c_sales=[18, 22, 25, 28, 32, 38, 42, 45, 48, 52, 56, 60]
product_d_sales=[7, 9, 11, 13, 16, 18, 20, 23, 25, 28, 30, 33]

def tren_line():
    fig, ax = plt.subplots()
    ax.plot(month, product_c_sales, label = 'product C', linestyle ='--', marker = 'o', color= 'green')
    ax.plot(month, product_d_sales, label = 'product D', linestyle ='-', marker = 'x', color= 'orange')

    ax.set_title ('Penjualan produk perbulan dengan tren')
    ax.set_xlabel('bulan')
    ax.set_ylabel('penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    
def subplot():
    fig, ax = plt.subplots(2,1, figsize=(8, 10))
    
    # produk c
    ax[0].plot(month, product_c_sales, label = 'product C', linestyle ='-.', marker = 'd', color= 'green')
    ax[0].set_title('penjualan produk perbulan')
    ax[0].set_xlabel('bulan')
    ax[0].set_ylabel('penjualan')
    ax[0].legend()
    ax[0].grid(True)

    # produk d
    ax[1].plot(month, product_d_sales, label = 'product D', linestyle ='-.', marker = 'd', color= 'purple')
    ax[1].set_title('penjualan produk perbulan')
    ax[1].set_xlabel('bulan')
    ax[1].set_ylabel('penjualan')
    ax[1].legend()
    ax[1].grid(True)
    
    plt.tight_layout()
    st.pyplot(fig)
    
# Perkondisian visualisasi sesuai menu
if option == 'Single line plot':
    line_plot()
elif option == 'multiple & customization':
    customimize_line_plot()
elif option == 'jenis garis untuk menunjukan tren':
    tren_line()
elif option == 'subplot':
    subplot()
    
        