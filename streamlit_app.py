import streamlit as st
import sympy as sp
import numpy as np
import pandas as pd

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
max_iter = st.number_input("Maksimum iterasi", value = 50, min_value = 1, max_value = 100)

if st.button("Hitung Solusi"):
    try:
        x, y = sp.symbols("x y")   

        f1_sym = sp.sympify(f1)
        f2_sym = sp.sympify(f2)

        st.subheader("Persamaan yang Digunakan")
        st.write("f1 =", f1_sym)
        st.write("f2 =", f2_sym)

        J = sp.Matrix([[sp.diff(f1_sym, x), sp.diff(f1_sym, y)], [sp.diff(f2_sym, x), sp.diff(f2_sym, y)]])
        st.subheader("Jacobian Matrix")
        st.write(J)

        F = sp.Matrix([f1_sym, f2_sym])
        F_func = sp.lambdify((x, y), F, "numpy")
        J_func = sp.lambdify((x, y), J, "numpy")

        xk, yk = x0, y0

        iter_data = []

        for i in range(int(max_iter)):
            F_val = np.array(F_func(xk, yk), dtype=float).flatten()
            J_val = np.array(J_func(xk, yk), dtype=float)

            detJ = np.linalg.det(J_val)
            
            if abs(detJ) < 1e-10:
                st.error("Jacobian singular atau mendekati nol. Coba tebakan awal lain.")
                break

            delta = np.linalg.solve(J_val, F_val)

            xk = xk - delta[0]
            yk = yk - delta[1]

            error = np.linalg.norm(delta)
            if error < tol:
                break

        st.success("Solusi berhasil dihitung")

        st.write(f"Jumlah iterasi: {i + 1}")
        st.write("x ≈ ", xk)
        st.write("y ≈ ", yk)

        if i == int(max_iter) - 1:
            st.warning("Solusi belum konvergen dalam batas iterasi maksimum")
            
    except Exception as e:
        st.error("Terjadi kesalahan dalam perhitungan")
        st.exception(e)
      
