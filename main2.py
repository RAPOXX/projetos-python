import pandas as pd 
import matplotlib.pyplot as plt

associados = pd.read_excel('./associados.xlsx')

print(associados)

socios_genero_masculino = associados.loc[associados['Sexo'] == 'MASCULINO',['Sexo']]
socios_genero_feminino = associados.loc[associados['Sexo'] == 'FEMININO',['Sexo']]

fig,ax = plt.subplots()

fig.suptitle("RELATORIO DE GÊNERO DE SOCIOS")

ax.pie([len(socios_genero_masculino),len(socios_genero_feminino)],autopct='%1.1f%%',labels=['MASCULINO','FEMININO'])

ax.legend()

plt.show()