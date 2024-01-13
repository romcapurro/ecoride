import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página de Streamlit
st.set_page_config(page_title='EcoRide MVP', layout="wide")

# Cargar datos desde el archivo CSV
car_electric = pd.read_csv('ElectricCarData_Clean.csv')


def new_line():
    st.markdown("<br>", unsafe_allow_html=True)


# Configuración de estilo de Streamlit con CSS
st.markdown(
    """
    <style>
        body {
            background-color: #404040; /* Cambiar a gris grafito */
            color: #fafafa;
        }
        .streamlit-title {
            color: #f21111;
        }
        .stButton>button {
            background-color: #404040; /* Cambiar a gris grafito */
            color: #fafafa;
        }
        .stMarkdown {
            font-size: 10px !important; /* Ajustar el tamaño de la tipografía */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Agregar el título 'EcoRide MVP'
st.title('EcoRide MVP')
new_line()
new_line()


# Seleccionar el Top 10 por alcance de autos eléctricos
los_10_autos_alcance = car_electric.nlargest(10, 'Range_Km')

# Crear una columna con el nombre de la marca y el modelo
los_10_autos_alcance['Modelos'] = los_10_autos_alcance['Brand'] + \
    ' ' + los_10_autos_alcance['Model']

# Configuración de estilo para desactivar la cuadrícula de Seaborn
sns.set_style("whitegrid")

# Gráfico de barras (Alcance de Autos Eléctricos)
st.title('Top 10 de Autos Eléctricos por Alcance')
new_line()
new_line()
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(los_10_autos_alcance['Modelos'], los_10_autos_alcance['Range_Km'], color=[
              '#404040', 'orange'], edgecolor='black')
# Ajustar el tamaño de la tipografía
ax.set_xlabel('Modelos de Autos Eléctricos', fontsize=8)
ax.set_ylabel('Alcance en Kilómetros con Carga Completa de Batería',
              fontsize=6)  # Ajustar el tamaño de la tipografía
ax.set_title('Alcance de Autos Eléctricos por Kilómetros',
             fontsize=6)  # Ajustar el tamaño de la tipografía
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center',
            va='bottom', fontsize=6)  # Ajustar el tamaño de la tipografía
# Ajustar el tamaño de la tipografía
plt.xticks(rotation=45, ha='right', fontsize=6)
plt.yticks(fontsize=6)  # Ajustar el tamaño de la tipografía
st.pyplot(fig)

# Configuración de estilo para desactivar la cuadrícula de Seaborn
sns.set_style("white")
new_line()

# Gráfico de dispersión (Relación entre Precio y Kilometraje)
st.title('Relación entre Precio y Kilometraje')
fig, ax = plt.subplots(figsize=(4, 2))
scatter = ax.scatter(los_10_autos_alcance['PriceEuro'],
                     los_10_autos_alcance['Range_Km'], color='white', edgecolor='#404040')
# Ajustar el tamaño de la tipografía
ax.set_xlabel('Precio (Euro)', fontsize=6)
# Ajustar el tamaño de la tipografía
ax.set_ylabel('Kilometraje (Km)', fontsize=6)
# Ajustar el tamaño de la tipografía
ax.set_title('Relación entre Precio y Kilometraje', fontsize=6)
ax.set_facecolor('#404040')
plt.xticks(fontsize=6)  # Ajustar el tamaño de la tipografía
plt.yticks(fontsize=6)  # Ajustar el tamaño de la tipografía
st.pyplot(fig)
new_line()
# KPIs de Autos Eléctricos
st.title('KPIs de Autos Eléctricos')

# Calcular KPIs
eficiencia = los_10_autos_alcance['Efficiency_WhKm'].mean()
kilometraje = los_10_autos_alcance['Range_Km'].mean()
relacion_eficiencia_kilometraje = los_10_autos_alcance['Efficiency_WhKm'].sum(
) / los_10_autos_alcance['Range_Km'].sum()
eficiencia_por_precio = eficiencia / los_10_autos_alcance['PriceEuro'].mean()

# Mostrar tarjetas para KPIs
st.metric('Eficiencia Energética Promedio', eficiencia, 'Wh/Km')
st.metric('Kilometraje Promedio', kilometraje, 'Km')
st.metric('Relación Eficiencia-Kilometraje', relacion_eficiencia_kilometraje)
st.metric('Eficiencia por Precio', eficiencia_por_precio)
