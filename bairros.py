import json
import psycopg2
import folium
from folium.plugins import StripePattern
import webbrowser
import pandas as pd
import jellyfish as jf
import string
import geopandas as gpd
import webbrowser


conexao = psycopg2.connect(host='faus.arapiraca.al.gov.br', port = '5432', database='db_faus',
user='fiscal', password='db#f1sc@l@R@19')
cursor = conexao.cursor()  
bairros_chave = pd.read_csv("C:/Users/EquipeDev/Documents/bairros_chaves.csv", encoding='latin1')
geoJSON = gpd.read_file('C:/Users/EquipeDev/Desktop/faus_holiday/produtividade/fiscal_digital/bairros_arapiraca.geojson')

auto_infracao = []

###################### Auto de Infração ############################################################################
for i in bairros_chave["chave"]:
    sql = 'SELECT COUNT(*) FROM public.termo_auto_infracao WHERE bairro_infracao_auto_infracao  ILIKE '+"'" + i +"'"
    cursor.execute(sql)
    conexao.commit()
    qtd_auto_infracao = cursor.fetchall()
    auto_infracao.append(qtd_auto_infracao[0][0])
bairros_chave["auto_infracao"] = auto_infracao
auto_geojson = []
for i in geoJSON.BAIRRO:
    valor_auto = bairros_chave[bairros_chave.Bairro== i]["auto_infracao"].values[0]
    auto_geojson.append(valor_auto)
    
geoJSON["auto_infracao"] = auto_geojson






map_auto = folium.Map(location=[-9.751969332753832, -36.656550027706835], zoom_start=12,  tiles='OpenStreetMap')

# Set up Choropleth map
folium.Choropleth(
geo_data=geoJSON,
data=geoJSON,
columns=['BAIRRO',"auto_infracao"],
key_on="feature.properties.BAIRRO",
fill_color='YlGnBu',
fill_opacity=1,
line_opacity=0.5,
legend_name="Quantidade de Auto de Infração",
smooth_factor=0,
Highlight= True,
line_color = "#0000",
name = "Quantidade de Auto de Infração",
show=False,
overlay=True,
nan_fill_color = "White"
).add_to(map_auto)



map_auto.save("map_auto.html")
webbrowser.open("map_auto.html")
########################## Notificação ##############################################################################

notificacao = [] 

for i in bairros_chave["chave"]:
    sql = 'SELECT COUNT(*) FROM public.termo_notificacao WHERE bairro_infracao_notificacao  ILIKE '+"'" + i +"'"
    cursor.execute(sql)
    conexao.commit()
    qtd_notificacao = cursor.fetchall()
    notificacao.append(qtd_notificacao[0][0])
bairros_chave["notificacao"] = notificacao
notificacao_geojson = []
for i in geoJSON.BAIRRO:
    valor_notificacao = bairros_chave[bairros_chave.Bairro== i]["notificacao"].values[0]
    notificacao_geojson.append(valor_notificacao)
    
geoJSON["notificacao"] = notificacao_geojson

map_notificacao = folium.Map(location=[-9.751969332753832, -36.656550027706835], zoom_start=12,  tiles='OpenStreetMap')

# Set up Choropleth map
folium.Choropleth(
geo_data=geoJSON,
data=geoJSON,
columns=['BAIRRO',"notificacao"],
key_on="feature.properties.BAIRRO",
fill_color='YlGnBu',
fill_opacity=1,
line_opacity=0.5,
legend_name="Quantidade de Notificações",
smooth_factor=0,
Highlight= True,
line_color = "#0000",
name = "Quantidade de Notificações",
show=False,
overlay=True,
nan_fill_color = "White"
).add_to(map_notificacao)



map_notificacao.save("map_notificacao.html")
webbrowser.open("map_notificacao.html")
############################# Embargo ###############################################################################
sql_embargo = 'SELECT numero_processo_termo_embargo, data_lavratural_termo_embargo, latitude, longitude FROM public.termo_embargo'
cursor.execute(sql_embargo)
conexao.commit()
embargos = cursor.fetchall()
df_embargos = pd.DataFrame(embargos, columns=["Processos", "Data", "latitude", "longitude"])
print(df_embargos)
df_embargos.to_excel('df_embargos.xlsx',sheet_name='dados')
map_embargo = map_auto
for i in embargos:
    if i[2] !='':
        #print([float(i[2]), float(i[3])])
        folium.Marker(
                        location=[float(i[2]), float(i[3])],
                        popup = str(i[0]),
                        icon=folium.Icon(color="red", icon="info-sign"),
                      ).add_to(map_embargo)
map_embargo.save("map_embargo.html")
webbrowser.open("map_embargo.html")
############################# Interdição #############################################################################

conexao.close()