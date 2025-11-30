import streamlit as st

st.title("Aplikasi SPNL Newton Raphson")
st.write("Aplikasi ini digunakan untuk menyelesaikan Sistem Persamaan Non-Linear dengan menggunakan metode Newton Raphson")

st.subheader("Masukkan Persamaan")
f1 = st.text_input("Persamaan 1", placeholder = "x**2 + y**2 - 5")
f2 = st.text_input("Persamaan 2", placeholder = "x*y - 1")
