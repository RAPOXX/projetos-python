import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
        
#le os dados dessa planilha excel        
dados_df = pd.read_excel('./dados.xlsx')

#organiza esses dados por categoria
dados_baba = dados_df.loc[dados_df['CATEGORIA'] == 'BABÁ']
dados_motorista = dados_df.loc[dados_df['CATEGORIA'] == 'MOTORISTA']
dados_acompanhante = dados_df.loc[dados_df['CATEGORIA'] == 'ACOMPANHANTE']

def listaLinhas(coluna):
    linhas = []
    for linha in coluna:
        linhas.append(str(linha))

    return linhas
    
def listaIdades(nascimentos):   
    idades = []
    for nascimento in nascimentos:      
        nasc_f = str(nascimento)
        nasc_ano = nasc_f.rsplit('-')[0] 

        if nasc_f == '**/**/****':
            pass
        else :        
            idade = 2023 - int(nasc_ano.replace('/',''))
            if(len(str(idade)) > 2) :
                pass
            else:
                idades.append(idade)
    return idades

def calcMediaIdades(idades):
    total_idades = 0 

    for idade in idades:
        total_idades += idade

    media_idades = total_idades / len(idades)  
    return int(media_idades)

#lista as datas de nascimentos por categoria
dados_acompanhante_nascimento = listaLinhas(dados_acompanhante['DATA DE NASCIMENTO'])
dados_baba_nascimento = listaLinhas(dados_baba['DATA DE NASCIMENTO'])
dados_motorista_nascimento = listaLinhas(dados_motorista['DATA DE NASCIMENTO'])

#lista as idades  dessas categorias
acomphantes_idades = listaIdades(dados_acompanhante_nascimento)
babas_idades = listaIdades(dados_baba_nascimento)
motoristas_idades = listaIdades(dados_motorista_nascimento)

#media de idade de cada categoria
acomphantes_idades_media = calcMediaIdades(acomphantes_idades)
babas_idades_media = calcMediaIdades(babas_idades)
motoristas_idades_media = calcMediaIdades(motoristas_idades)

print(acomphantes_idades_media)
print(babas_idades_media)
print(motoristas_idades_media)

idades_medias = [acomphantes_idades_media,motoristas_idades_media,babas_idades_media]
total = 0

for idade in idades_medias:n
    total += idade

print(total)
fig,ax = plt.subplots()


ax.pie(idades_medias,explode=(0,0.1,0),labels=['ACOMPANHANTES','MOTORISTAS','BABAS'],autopct='%1.1f%%',shadow=True)

plt.show()