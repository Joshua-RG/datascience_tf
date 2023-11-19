import pandas as pd 

import matplotlib.pyplot as plt

archivo = 'dataframe_limpio.csv'


df = pd.read_csv(archivo)

df['trending_date'] = pd.to_datetime(df['trending_date'], format='%y.%d.%m')

# Crear nuevas columnas 'año' y 'mes' que contengan el año y el mes de cada fecha
df['año'] = df['trending_date'].dt.year
df['mes'] = df['trending_date'].dt.month

# Contar la cantidad de videos por año y mes
conteo_por_año_mes = df.groupby(['año', 'mes']).size().unstack()
conteo_por_año_mes = conteo_por_año_mes.fillna(0)

# Filtrar por años 2017 y 2018
conteo_2017 = conteo_por_año_mes.loc[2017]
conteo_2018 = conteo_por_año_mes.loc[2018]

# Crear el gráfico de líneas (fiebre)
plt.plot(conteo_2017.index, conteo_2017.values, marker='o', label='2017')
plt.plot(conteo_2018.index, conteo_2018.values, marker='o', label='2018')

# Anotar los valores de los puntos
for i, txt in enumerate(conteo_2017.values):
    plt.annotate(txt, (conteo_2017.index[i], txt), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(conteo_2018.values):
    plt.annotate(txt, (conteo_2018.index[i], txt), textcoords="offset points", xytext=(0,10), ha='center')

# Configurar el gráfico
plt.xlabel('Mes')
plt.ylabel('Número de videos en tendencia')
plt.title('Número de videos en tendencia por mes')

# Mostrar la leyenda sin duplicados
plt.legend(title='Año', prop={'size': 10}, loc='center right')

plt.xticks(rotation=45, ha='right')
plt.grid(True)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
#*
# Crear el gráfico de columnas (bar chart)
#width = 0.35  # Ancho de las columnas
#fig, ax = plt.subplots()
#bar_2017 = ax.bar(conteo_2017.index, conteo_2017.values, width, label='2017')
#bar_2018 = ax.bar(conteo_2018.index + width, conteo_2018.values, width, label='2018')

# Anotar el valor de cada barra en el gráfico
#for rect in bar_2017 + bar_2018:
#    height = rect.get_height()
#    ax.text(rect.get_x() + rect.get_width() / 2, height, f'{int(height)}', ha='center', va='bottom')

# Configurar el gráfico
#ax.set_xlabel('Mes')
#ax.set_ylabel('Número de Publicaciones')
#ax.set_title('Número de Publicaciones por fecha de tendencia')

#ax.set_xticks(conteo_2017.index + width / 2)
#ax.set_xticklabels(conteo_2017.index)
#ax.legend(title='Año', loc=0)
# Mostrar el gráfico
#plt.show()#
