import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 

# Header 
st.title("Praktikum 06 Visualisasi Data")
st.write("Kelompok 26")
st.markdown("""      
Kelompok 26:
1. Syahidah Yuli Amaliah - 0110122220 
2. Izzuddin Ahmad Alqosam - 0110122052
3. Adi Triadi -0110222077
""")
# Dataset
stores = ['Store A', 'Store B', 'Store C']
male = [150, 180, 160]
female = [140, 200, 180]

product_a = [200, 250, 300]
product_b = [150, 300, 200]

# Data quarter 
q1_male = [150, 180, 160]
q1_female = [140, 200, 180]
q2_male = [170, 190, 175]
q2_female = [130, 210,160]

# 1 Grafik Stacked Vertikal Bar Chart 
st.subheader("1 Stacked Vertikal Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))   
ax.bar(x, male, label='Male', color='blue')
ax.bar(x, female, bottom=male, label='Female', color='pink')

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)

# 2 Grafik Stacked Vertikal Bar Chart 
st.subheader("2 Stacked Vertikal Bar Chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label='Product A', color='blue')
ax.bar(x, product_b, bottom=product_a, label='Product B', color='yellow')

ax.set_title('Sales transaction by Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)

# 3 Grafik Kustomisasi Stacked Vertikal Bar Chart 
st.subheader("3 Kustomisasi Stacked Vertikal Bar Chart")

fig, ax = plt.subplots()
ax.bar(x, product_a, color='purple')
ax.bar(x, product_b, bottom=product_a, color='orange')

for i in range(len(x)):
    plt.text(x[i], product_a[i] / 2, str(product_a[i]), ha='center', color='white')
    plt.text(x[i], product_a[i] + product_b[i] / 2, str(product_b[i]), ha='center', color='black')

ax.set_xticks(x)
ax.set_xticklabels(stores)

st.pyplot(fig)

# 4 Grafik Multiple Stacked Vertikal Bar Chart
st.subheader("4 Multiple Stacked Vertikal Bar Chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

# quarter 1
ax.bar(x - width/2, q1_male, label='Q1 Male', color='lightblue', width=width)
ax.bar(x - width/2, q1_female, bottom=q1_male, label='Q1 Female', color='pink', width=width)

# quarter 2
ax.bar(x + width/2, q2_male, label='Q2 Male', color='blue', width=width)
ax.bar(x + width/2, q2_female, bottom=q2_male, label='Q2 Female', color='red', width=width)

ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticks(x)
ax.set_xticklabels(stores)
ax.legend()

st.pyplot(fig)