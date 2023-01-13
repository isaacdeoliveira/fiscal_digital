import json
import psycopg2
import folium
import webbrowser
import pandas as pd
import jellyfish as jf
import string
conexao = psycopg2.connect(host='faus.arapiraca.al.gov.br', port = '5432', database='db_faus',
user='fiscal', password='db#f1sc@l@R@19')
cursor = conexao.cursor()  

sql = "SELECT id_auto_infracao, numero_bloco_auto_infracao, bairro_infracao_auto_infracao, latitude, longitude FROM public.termo_auto_infracao WHERE data_lavratura_auto_infracao >= '2022-01-01' AND data_lavratura_auto_infracao <= '2022-12-31' "
cursor.execute(sql)
conexao.commit()
dados = cursor.fetchall()
df_dados = pd.DataFrame(dados, columns=["id_auto_infracao", "Número do termo", "Bairro", "latitude", "longitude" ])

print(jf.levenshtein_distance('gato', str.lower('GATO')))
dados_geojson = df_dados.to_json()
conexao.close()
teste = 'Senenador Arnon de Melo'
for i in df_dados.Bairro:
    similaridade = 1 - jf.levenshtein_distance(str.lower(i),teste)/len(teste)
    if similaridade > 0.5:
        print(teste, '--',i)
    
   