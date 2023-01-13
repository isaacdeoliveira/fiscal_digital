import json
import psycopg2
import folium
import webbrowser
import pandas as pd
import jellyfish as jf
import string
import geopandas
import webbrowser


conexao = psycopg2.connect(host='faus.arapiraca.al.gov.br', port = '5432', database='db_faus',
user='fiscal', password='db#f1sc@l@R@19')
cursor = conexao.cursor()  
sql = 'SELECT COUNT(*) FROM public.termo_auto_infracao WHERE bairro_infracao_auto_infracao  ILIKE' +"'olho%'"
cursor.execute(sql)
conexao.commit()
bairros = cursor.fetchall()

bairros_chave = pd.read_csv("C:/Users/EquipeDev/Documents/bairros_chaves.csv", encoding='latin1')

auto_infracao = []


for i in bairros_chave["chave"]:
    sql = 'SELECT COUNT(*) FROM public.termo_auto_infracao WHERE bairro_infracao_auto_infracao  ILIKE '+"'" + i +"'"
    cursor.execute(sql)
    conexao.commit()
    qtd_auto_infracao = cursor.fetchall()
    #auto_infracao.append(qtd_auto_infracao[0][0])

conexao.close()
bairros_chave["Auto de Infração"] = auto_infracao


map = folium.Map(location=[-9.751969332753832, -36.656550027706835], zoom_start=12,  tiles='OpenStreetMap')
'''
folium.Choropleth(
    geo_data = geo_bairros,
    name="choropleth",
    data = bairros_chave,
    columns=["Bairro", "Auto de Infração"],
    key_on = 'bairros_chave.Bairro',
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Auto de Infração",
).add_to(map)'''

map.save("map.html")
#webbrowser.open("map.html")
