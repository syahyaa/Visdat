import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ================= KONFIGURASI GLOBAL =================
sns.set_style("whitegrid")
sns.set_palette("muted")  # ⭐ lebih lembut dari Set2

plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.titlesize"] = 13
plt.rcParams["axes.labelsize"] = 11
plt.rcParams["xtick.labelsize"] = 10
plt.rcParams["ytick.labelsize"] = 10

st.set_page_config(page_title="Dashboard Analisis Kesehatan", layout="wide")

# ================= LOAD DATA =================
df = pd.read_excel("UAS_FIX_DATA_BERSIH.xlsx")
df.columns = df.columns.str.strip()

# ================= SIDEBAR FILTER =================
st.sidebar.header("🔍 Filter Data Pasien")

min_age, max_age = int(df["AGE"].min()), int(df["AGE"].max())
age_range = st.sidebar.slider(
    "Rentang Usia",
    min_value=min_age,
    max_value=max_age,
    value=(min_age, max_age)
)

gender_filter = st.sidebar.multiselect(
    "Jenis Kelamin",
    options=df["GENDER"].unique(),
    default=df["GENDER"].unique()
)

diagnosis_filter = st.sidebar.multiselect(
    "Diagnosis",
    options=df["DIAGNOSIS"].unique(),
    default=df["DIAGNOSIS"].unique()
)

df_filtered = df[
    (df["AGE"].between(age_range[0], age_range[1])) &
    (df["GENDER"].isin(gender_filter)) &
    (df["DIAGNOSIS"].isin(diagnosis_filter))
]

# ================= HEADER =================
st.title("📊 Dashboard Analisis Risiko Penyakit")

# ================= KPI =================
col1, col2, col3 = st.columns(3)
col1.metric("Jumlah Pasien", df_filtered.shape[0])
col2.metric("Rata-rata Usia", round(df_filtered["AGE"].mean(), 1))
col3.metric("Rata-rata LDL", round(df_filtered["CHOLESTEROLLDL"].mean(), 2))

# ================= TABS =================
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Distribusi",
    "📈 Tren",
    "🔥 Korelasi",
    "🧪 Analisis Lanjut"
])

# ================= TAB 1 =================
with tab1:
    colA, colB = st.columns(2)

    with colA:
        st.subheader("Distribusi Diagnosis")
        fig, ax = plt.subplots(figsize=(6,4))
        sns.countplot(
            x="DIAGNOSIS",
            data=df_filtered,
            palette="Blues",  # ⭐
            ax=ax
        )
        ax.set_xlabel("Diagnosis")
        ax.set_ylabel("Jumlah Pasien")
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    with colB:
        st.subheader("Distribusi Gender")
        pie_data = df_filtered["GENDER"].value_counts()
        fig, ax = plt.subplots(figsize=(6,4))
        ax.pie(
            pie_data,
            labels=pie_data.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=["#4c78a8", "#f58518"],  # ⭐
            textprops={"color": "white"}
        )
        ax.axis("equal")
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

# ================= TAB 2 =================
with tab2:
    st.subheader("Tren Rata-rata LDL berdasarkan Usia")

    line_data = (
        df_filtered
        .groupby("AGE")["CHOLESTEROLLDL"]
        .mean()
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(8,4))
    sns.lineplot(
        x=line_data.index,
        y=line_data.values,
        marker="o",
        color="#2a9d8f",  # ⭐
        linewidth=2.5,    # ⭐
        ax=ax
    )
    ax.set_xlabel("Usia")
    ax.set_ylabel("Rata-rata LDL")
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

# ================= TAB 3 =================
with tab3:
    st.subheader("Heatmap Korelasi Variabel Medis")

    num_df = df_filtered[
        ["AGE", "DIASTOLICBP", "CHOLESTEROLLDL", "CHOLESTEROLTRIGLYCERIDES"]
    ]

    fig, ax = plt.subplots(figsize=(7,4))
    sns.heatmap(
        num_df.corr(),
        annot=True,
        cmap="RdBu_r",  # ⭐
        center=0,       # ⭐
        fmt=".2f",
        linewidths=0.5, # ⭐
        linecolor="white",
        ax=ax
    )
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

# ================= TAB 4 =================
with tab4:
    colC, colD = st.columns(2)

    with colC:
        st.subheader("Distribusi Usia Pasien")
        fig, ax = plt.subplots(figsize=(6,4))
        sns.histplot(
            df_filtered["AGE"],
            bins=10,
            kde=True,
            color="#457b9d",  # ⭐
            ax=ax
        )
        ax.set_xlabel("Usia")
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    with colD:
        st.subheader("Hubungan Usia vs LDL")
        fig, ax = plt.subplots(figsize=(6,4))
        sns.scatterplot(
            x="AGE",
            y="CHOLESTEROLLDL",
            data=df_filtered,
            color="#e76f51",  # ⭐
            alpha=0.7,       # ⭐
            ax=ax
        )
        ax.set_xlabel("Usia")
        ax.set_ylabel("LDL")
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    st.subheader("Perbandingan LDL per Diagnosis")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.boxplot(
        x="DIAGNOSIS",
        y="CHOLESTEROLLDL",
        data=df_filtered,
        palette="Set3",  # ⭐
        ax=ax
    )
    ax.set_xlabel("Diagnosis")
    ax.set_ylabel("LDL")
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

# ================= KESIMPULAN =================
st.header("📌 Kesimpulan")
st.markdown("""
Dashboard ini menyajikan analisis data kesehatan pasien melalui:
- **Distribusi** diagnosis dan gender  
- **Tren LDL** berdasarkan usia  
- **Korelasi** antar variabel medis  
- **Analisis lanjutan** menggunakan histogram, scatter, dan boxplot  

Dashboard ini dirancang untuk membantu analisis risiko penyakit secara visual dan interaktif.
""")