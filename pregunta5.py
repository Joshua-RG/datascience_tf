import pandas as pd 
import matplotlib.pyplot as plt

#lectura del archivo
archivo = 'dataframe_limpio.csv'

df = pd.read_csv(archivo)

print("Columnas del DataFrame:")
print(df.columns)


estadisticas_canales = df.groupby('channel_title').agg({
    'video_id': 'count',        # Frecuencia
    'views': 'sum'              # Suma de vistas
}).reset_index()

# Renombrar las columnas
estadisticas_canales.columns = ['Channel Title', 'Frecuencia', 'Suma de Vistas']


# Ordenar por frecuencia y vistas en orden descendente
estadisticas_canales = estadisticas_canales.sort_values(by=['Frecuencia', 'Suma de Vistas'], ascending=[False, False])

# Tomar los top 10 primeros y ultimos para la visualización
top_canales = estadisticas_canales.head(10)
top_ultimos_canales = estadisticas_canales.tail(10)

# --------------------- Crear un gráfico para los top 10 primeros-------------------------
fig, ax = plt.subplots(figsize=(10, 10))

#Colores para las tablas: Donde azul es para las tablas x frecuencia y purple para las tablas x vistas
colores_tabla1_2 = ['blue', 'lightblue']
colores_tabla3 = ['purple', 'pink']

barras = ax.barh(top_canales['Channel Title'], top_canales['Frecuencia'],color=colores_tabla1_2)

#Para que vaya en orden descendente
ax.invert_yaxis()

# Mostrar el valor alcanzado para cada barra
for barra in barras:
    valor = barra.get_width()
    ax.annotate(f'{valor}', xy=(valor, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0), textcoords='offset points', va='center', ha='left')

ax.set_xlabel('Suma de Frecuencia')
ax.set_title('Top 10 de canales que contienen mas videos en tendencia')
plt.tight_layout()
plt.show()


# --------------------- Crear un gráfico para los top 10 ultimos-------------------------
fig, axes = plt.subplots(ncols=1, nrows=2 ,figsize=(10, 6)) # En este grafico se crean 2 tablas debido a la coincidencia de numero de frecuencia

#crear grafico por numero de frecuencia
barras_frecuencia = axes[0].barh(top_ultimos_canales['Channel Title'], top_ultimos_canales['Frecuencia'],color=colores_tabla1_2)

for barra in barras_frecuencia:
    valor = barra.get_width()
    axes[0].annotate(f'{valor}', xy=(valor, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0), textcoords='offset points', va='center', ha='left')

# Configurar el gráfico por numero de frecuencia
axes[0].set_xlabel('Suma de Frecuencia')
axes[0].set_ylabel('Nombre del canal')
axes[0].set_title('Recuento de frecuencia')


# crear grafico por numero de vistas
barras_vistas = axes[1].barh(top_ultimos_canales['Channel Title'], top_ultimos_canales['Suma de Vistas'],color=colores_tabla3)
axes[1].invert_yaxis()

for barra in barras_vistas:
    valor = barra.get_width()
    axes[1].annotate(f'{valor}', xy=(valor, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0), textcoords='offset points', va='center', ha='left')

# Configurar el gráfico por numero de vistas
axes[1].set_xlabel('Suma de Vistas acumuladas')
axes[1].set_ylabel('Nombre del canal')
axes[1].set_title('Recuento de vistas')

#Titulo general
fig.suptitle('Top 10 canales que contienen menos videos en tendencia')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
