import streamlit as st
import sympy as sp
import numpy as np

st.title("Aplikasi SPNL Newton Raphson")
st.write("Aplikasi ini digunakan untuk menyelesaikan Sistem Persamaan Non-Linear dengan menggunakan metode Newton Raphson")

st.subheader("Masukkan Persamaan")
f1 = st.text_input("Persamaan 1", placeholder = "contoh = x**2 + y**2 - 5")
f2 = st.text_input("Persamaan 2", placeholder = "contoh = x*y - 1")

st.subheader("Masukkan Tebakan Awal")
x0 = st.number_input("Tebakan awal x", value=1.0)
y0 = st.number_input("Tebakan awal y", value=1.0)

st.subheader("Masukkan Parameter")
tol = st.number_input("Toleransi", value = 1e-6, min_value = 0.0, format = "%.6e")
max_iter = st.number_input("Maksimum iterasi", value = 50, min_value = 1, max_value = 1000)

if st.button("Tampilkan Input"):
  st.write("Persamaan 1: ", f1)
  st.write("Persamaan 2: ", f2)
  st.write("Tebakan awal: x = ", x0, ", y = ", y0)
  st.write("Toleransi:", tol)
  st.write("Maksimum iterasi:", max_iter)

if st.button("Cek Persamaan"):
    try:
        x, y = sp.symbols('x y')
        f1_sym = sp.sympify(f1)
        f2_sym = sp.sympify(f2)

        st.success("Persamaan valid")
        st.write("f1 =", f1_sym)
        st.write("f2 =", f2_sym)

    except:
        st.error("Format persamaan salah")

if st.button("Hitung Turunan Parsial"):
        x, y = sp.symbols("x y")
        f1_sym = sp.sympify(f1)

        df1_dx = sp.diff(f1_sym, x)
        df1_dy = sp.diff(f1_sym, y)
