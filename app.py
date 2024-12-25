import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Comparación de Descriptores de Reactividad Química")
st.write("Jesus Alvarado-Huayhuaz")
# Descripción
st.write("Esta aplicación compara los descriptores de reactividad química de dos moléculas utilizando la teoría conceptual de DFT. Puedes ingresar los valores de energía de ionización (I) y afinidad electrónica (A) para cada molécula.")

# Entradas de usuario
st.header("Entradas")

# Valores para la molécula 1
st.subheader("Molécula 1")
mol1_name = st.text_input("Nombre de la molécula 1", "H2O")
mol1_I = st.number_input(f"Energía de Ionización de {mol1_name} (eV)", value=12.62, step=0.01)
mol1_A = st.number_input(f"Afinidad Electrónica de {mol1_name} (eV)", value=0.30, step=0.01)

# Valores para la molécula 2
st.subheader("Molécula 2")
mol2_name = st.text_input("Nombre de la molécula 2", "NH3")
mol2_I = st.number_input(f"Energía de Ionización de {mol2_name} (eV)", value=10.07, step=0.01)
mol2_A = st.number_input(f"Afinidad Electrónica de {mol2_name} (eV)", value=0.40, step=0.01)

# Funciones para calcular los descriptores
def calculate_descriptors(I, A):
    mu = -(I + A) / 2
    chi = -mu
    eta = (I - A) / 2
    S = 1 / eta if eta != 0 else 0
    omega = mu ** 2 / (2 * eta) if eta != 0 else 0
    return mu, chi, eta, S, omega

# Cálculo para ambas moléculas
mu1, chi1, eta1, S1, omega1 = calculate_descriptors(mol1_I, mol1_A)
mu2, chi2, eta2, S2, omega2 = calculate_descriptors(mol2_I, mol2_A)

# Mostrar resultados
st.header("Resultados")

# Tabla de descriptores
data = {
    "Descriptor": ["Potencial Químico (μ)", "Electronegatividad (χ)", "Dureza Química (η)", "Suavidad Química (S)", "Electrofilicidad (ω)"],
    mol1_name: [mu1, chi1, eta1, S1, omega1],
    mol2_name: [mu2, chi2, eta2, S2, omega2]
}

st.table(data)

# Gráficas
st.header("Gráficas")

def plot_bars():
    labels = ["μ", "χ", "η", "S", "ω"]
    mol1_values = [mu1, chi1, eta1, S1, omega1]
    mol2_values = [mu2, chi2, eta2, S2, omega2]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(x - width/2, mol1_values, width, label=mol1_name)
    ax.bar(x + width/2, mol2_values, width, label=mol2_name)

    ax.set_ylabel("Valores")
    ax.set_title("Comparación de Descriptores")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    st.pyplot(fig)

def plot_radar():
    labels = ["μ", "χ", "η", "S", "ω"]
    mol1_values = [mu1, chi1, eta1, S1, omega1]
    mol2_values = [mu2, chi2, eta2, S2, omega2]

    # Radar chart setup
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    mol1_values += mol1_values[:1]
    mol2_values += mol2_values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    ax.plot(angles, mol1_values, label=mol1_name, linewidth=2)
    ax.fill(angles, mol1_values, alpha=0.25)
    
    ax.plot(angles, mol2_values, label=mol2_name, linewidth=2)
    ax.fill(angles, mol2_values, alpha=0.25)

    ax.set_yticks([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.legend()

    st.pyplot(fig)

# Botones para mostrar gráficas
if st.button("Mostrar Gráfica de Barras"):
    plot_bars()

if st.button("Mostrar Radar Chart"):
    plot_radar()

# Tabla de descriptores
data1 = {
    "Descriptor": ["Energía de Ionización (I)", "Afinidad Electrónica (A)", "Potencial Químico (μ)", "Electronegatividad (χ)", "Dureza Química (η)", "Suavidad Química (S)", "Electrofilicidad (ω)"],
    "Interpretación": ["H2O necesita más energía para perder un electrón, por lo que es menos reactivo como nucleófilo.",
          "(Energía liberada al aceptar un electrón) NH3  tiene una mayor tendencia a aceptar electrones en comparación con H2O",
          "H2O es más estable químicamente y menos propenso a intercambiar electrones.",
          "H2O es más electronegativo, lo que indica una mayor atracción hacia los electrones.",
          "H2O es más duro, lo que significa que es menos propenso a la transferencia de carga.",
          "NH3 es más suave, por lo que puede redistribuir su densidad electrónica más fácilmente.",
          "(Propensión general a aceptar densidad electrónica) H2O es un mejor electrófilo y tiene más capacidad para aceptar electrones (Descriptor contextual en una interacción química | Incluye la dureza química, reflejando estabilidad tras aceptar electrones)."
         ]
    #mol2_name: [mu2, chi2, eta2, S2, omega2]
}

st.table(data1)
