import streamlit as st
import numpy as np
from joblib import load

# Load model Decision Tree yang telah disimpan
model = load('Decision_tree_classifier_acc.joblib')

# Fungsi untuk prediksi kualitas pemain
def predict_player_quality(age, overall, potential, weight):
    # Data input sebagai array
    input_features = np.array([[age, overall, potential, weight]])  # 4 fitur
    prediction = model.predict(input_features)[0]  # Prediksi kelas (Bagus/Sedang/Tidak Bagus)
    return prediction

# Streamlit UI
st.title("Prediksi Kualitas Pemain FIFA")
st.write("Masukkan data pemain untuk memprediksi apakah pemain itu **Bagus**, **Sedang**, atau **Tidak Bagus**.")

# Input dari pengguna
age = st.number_input("Umur (Age):", min_value=15, max_value=50)
overall = st.number_input("Overall:", min_value=20, max_value=99)
potential = st.number_input("Potensi (Potential):", min_value=20, max_value=99)
weight = st.number_input("Berat (Weight):", min_value=20, max_value=200)

# Tombol Prediksi
if st.button("Prediksi"):
    # Lakukan prediksi berdasarkan input pengguna
    prediction = predict_player_quality(age, overall, potential, weight)
    
    # Tampilkan hasil prediksi
    st.write("### Hasil Prediksi")
    if prediction == "Bagus":
        st.success(f"Prediksi: **Bagus** 🌟")
    elif prediction == "Sedang":
        st.warning(f"Prediksi: **Sedang** ⚖️")
    else:
        st.error(f"Prediksi: **Tidak Bagus** ❌")







