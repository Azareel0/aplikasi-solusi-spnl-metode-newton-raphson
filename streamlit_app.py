import streamlit as st

st.title("Aplikasi SPNL Newton Raphson")
st.write("Aplikasi ini digunakan untuk menyelesaikan Sistem Persamaan Non-Linear dengan menggunakan metode Newton Raphson")

st.subheader("Masukkan Persamaan")
f1 = st.text_input("Persamaan 1", placeholder = "contoh = x**2 + y**2 - 5")
f2 = st.text_input("Persamaan 2", placeholder = "contoh = x*y - 1")

st.subheader("Masukkan Tebakan Awal")
x0 = st.number_input("Tebakan awal x", value=1.0)
y0 = st.number_input("Tebakan awal y", value=1.0)
