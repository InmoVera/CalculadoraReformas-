import streamlit as st

# Reformas y sus impactos
reformas_impacto = {
    "Pintar": (0.01, 0.03),
    "Cambiar ventanas": (0.03, 0.05),
    "Cambiar puertas": (0.01, 0.02),
    "Reformar el baño": (0.03, 0.06),
    "Reformar la cocina": (0.05, 0.10),
    "Cambiar la instalación eléctrica": (0.02, 0.05),
    "Cambiar el suelo": (0.02, 0.04),
    "Instalar calefacción": (0.03, 0.07),
    "Instalar aire acondicionado": (0.02, 0.05),
    "Climatizar toda la vivienda": (0.05, 0.12),
    "Instalar placas solares": (0.03, 0.08),
    "Reformar la fachada": (0.04, 0.07),
    "Reformar el jardín": (0.03, 0.08),
    "Reformar el tejado": (0.05, 0.10),
}

# Función para calcular incremento
def calcular_incremento(valor_inicial, reformas):
    incremento_total = 0
    for reforma in reformas:
        if reforma in reformas_impacto:
            rango = reformas_impacto[reforma]
            incremento = valor_inicial * ((rango[0] + rango[1]) / 2)
            incremento_total += incremento
    return incremento_total

# Interfaz de usuario
st.title("Calculadora de Incremento de Valor de Vivienda")

valor_vivienda = st.number_input("Introduce el valor actual de tu vivienda (€):", step=1000)
reformas = st.multiselect(
    "Selecciona las reformas que quieres realizar:",
    list(reformas_impacto.keys())
)

if st.button("Calcular Incremento"):
    incremento_total = calcular_incremento(valor_vivienda, reformas)
    st.write(f"El incremento estimado en el valor de tu vivienda es de: {incremento_total:.2f} €")
