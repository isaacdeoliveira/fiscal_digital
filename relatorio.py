from base64 import encode
import json
import psycopg2
import folium
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import style
plt.style.use('bmh')


nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

conexao = psycopg2.connect(host='faus.arapiraca.al.gov.br', port = '5432', database='db_faus',
user='fiscal', password='db#f1sc@l@R@19')
cursor = conexao.cursor()  
meses = [["2022-01-01","2022-01-31"], ["2022-02-01","2022-01-29"], ["2022-03-01","2022-03-31"], 
         ["2022-04-01","2022-04-30"], ["2022-05-01","2022-05-30"], ["2022-06-01","2022-06-30"], 
         ["2022-07-01","2022-07-31"], ["2022-08-01","2022-08-31"], ["2022-09-01","2022-09-30"], 
         ["2022-10-01","2022-10-31"], ["2022-11-01","2022-11-30"], ["2022-12-01","2022-12-31"] ]

processos_mes = []
for i in range(len(meses)):
    mes_selected = meses[i]
    mes_inicio = mes_selected[0]
    mes_fim = mes_selected[1]
    #print(mes_inicio, '-', mes_fim)
    sql= "SELECT COUNT( numero_processo) FROM public.processo WHERE data_processo > "+ "'" + mes_inicio + "'" + "AND data_processo <"+ "'" + mes_fim +"'"
    #print(sql)
    #sql_notificacao = "SELECT numero_processo_notificacao, latitude, longitude FROM termo_notificacao"
    cursor.execute(sql)
    conexao.commit()
    retorno = cursor.fetchall()
    processos_mes.append(retorno[0][0])

data_set_processos = pd.DataFrame(index = nomes_meses, columns=['Processos'], data=processos_mes)
print(data_set_processos)

data_set_processos.loc['Janeiro'] = 222
data_set_processos.loc['Fevereiro'] = 79
data_set_processos.loc['Março'] = 168
data_set_processos.loc['Abril'] = 15
data_set_processos.loc['Maio'] = 163
data_set_processos.loc['Junho'] = 33 + data_set_processos.loc['Junho']
data_set_processos.loc['Julho'] = 147 + data_set_processos.loc['Julho']
data_set_processos.loc['Agosto'] = 10 + data_set_processos.loc['Agosto']
data_set_processos.loc['Setembro'] = 10 + data_set_processos.loc['Setembro']
data_set_processos.loc['Outubro'] = 10 + data_set_processos.loc['Outubro']
data_set_processos.loc['Novembro'] = 10 + data_set_processos.loc['Novembro']
data_set_processos.loc['Dezembro'] = 10 + data_set_processos.loc['Dezembro']

print(data_set_processos)
print(data_set_processos['Processos'].mean())

plt.figure(figsize=(10,8))
plt.bar(nomes_meses, data_set_processos["Processos"], width=0.5)
plt.xlabel("Meses")
plt.ylabel("Quantidade de processos")
plt.title('Processos de ações ostensivas - 2022')
plt.show()

##################################### motificações ###################################################

notificacao_mes = []
for i in range(len(meses)):
    mes_selected = meses[i]
    mes_inicio = mes_selected[0]
    mes_fim = mes_selected[1]
    sql_not = "SELECT COUNT(numero_bloco_notificacao) FROM public.termo_notificacao WHERE data_lavratura_notificacao >" + "'" + mes_inicio  + "'" +  "AND data_lavratura_notificacao <" +"'" + mes_fim + "'" 
    cursor.execute(sql_not)
    conexao.commit()
    retorno_not = cursor.fetchall()
    notificacao_mes.append(retorno_not[0][0])

data_set_notificacao = pd.DataFrame(index= nomes_meses, columns= ['Notificações'], data=notificacao_mes)

data_set_notificacao.loc['Janeiro'] = 103
data_set_notificacao.loc['Fevereiro'] = 18 
data_set_notificacao.loc['Março'] = 72 + data_set_notificacao.loc['Março']
data_set_notificacao.loc['Abril'] = 3 + data_set_notificacao.loc['Abril']
data_set_notificacao.loc['Maio'] = 104 + data_set_notificacao.loc['Maio']
data_set_notificacao.loc['Junho'] = 7 + data_set_notificacao.loc['Junho']
data_set_notificacao.loc['Julho'] = 69 + data_set_notificacao.loc['Julho']
data_set_notificacao.loc['Agosto'] = 2 + data_set_notificacao.loc['Agosto']
data_set_notificacao.loc['Setembro'] = 0 + data_set_notificacao.loc['Setembro']
data_set_notificacao.loc['Outubro'] = 1 + data_set_notificacao.loc['Outubro']
data_set_notificacao.loc['Novembro'] = 1 + data_set_notificacao.loc['Novembro']
data_set_notificacao.loc['Dezembro'] = 0 + data_set_notificacao.loc['Dezembro']
print(data_set_notificacao)

plt.figure(figsize=(10,8))
plt.bar(nomes_meses, data_set_notificacao["Notificações"], width=0.5)
plt.xlabel("Meses")
plt.ylabel("Quantidade de termos")
plt.title('Notificações em ações fiscais - 2022')
plt.show()

########################################### auto de infração ##########################################


auto_infracao_mes = []
for i in range(len(meses)):
    mes_selected = meses[i]
    mes_inicio = mes_selected[0]
    mes_fim = mes_selected[1]
    sql_auto = "SELECT COUNT(numero_bloco_auto_infracao) FROM public.termo_auto_infracao WHERE data_lavratura_auto_infracao >" + "'" + mes_inicio+ "'" +"AND data_lavratura_auto_infracao  <" + "'" + mes_fim + "'" 
    cursor.execute(sql_auto)
    conexao.commit()
    retorno_not = cursor.fetchall()
    auto_infracao_mes.append(retorno_not[0][0])

data_set_auto_infracao = pd.DataFrame(index= nomes_meses, columns= ['Auto de Infração'], data = auto_infracao_mes)

data_set_auto_infracao.loc['Janeiro'] = 213 + data_set_auto_infracao.loc['Janeiro']
data_set_auto_infracao.loc['Fevereiro'] = 68 + data_set_auto_infracao.loc['Fevereiro'] 
data_set_auto_infracao.loc['Março'] = 115 + data_set_auto_infracao.loc['Março']
data_set_auto_infracao.loc['Abril'] = 13 + data_set_auto_infracao.loc['Abril']
data_set_auto_infracao.loc['Maio'] = 79 + data_set_auto_infracao.loc['Maio']
data_set_auto_infracao.loc['Junho'] = 27 + data_set_auto_infracao.loc['Junho']
data_set_auto_infracao.loc['Julho'] = 82 + data_set_auto_infracao.loc['Julho']
data_set_auto_infracao.loc['Agosto'] = 7 + data_set_auto_infracao.loc['Agosto']
data_set_auto_infracao.loc['Setembro'] = 0 + data_set_auto_infracao.loc['Setembro']
data_set_auto_infracao.loc['Outubro'] = 0 + data_set_auto_infracao.loc['Outubro']
data_set_auto_infracao.loc['Novembro'] = 1 + data_set_auto_infracao.loc['Novembro']
data_set_auto_infracao.loc['Dezembro'] = 1 + data_set_auto_infracao.loc['Dezembro']
print(data_set_auto_infracao)

plt.figure(figsize=(10,8))
plt.bar(nomes_meses, data_set_auto_infracao["Auto de Infração"], width=0.5)
plt.xlabel("Meses")
plt.ylabel("Quantidade de termos")
plt.title('Autos de infração em ações fiscais - 2022')
plt.show()



########################################### Embargos ##########################################


embargos_mes = []
for i in range(len(meses)):
    mes_selected = meses[i]
    mes_inicio = mes_selected[0]
    mes_fim = mes_selected[1]
    sql_emb = "SELECT COUNT(numero_bloco_termo_embargo) FROM public.termo_embargo WHERE data_lavratural_termo_embargo >"+ "'"+ mes_inicio + "'"+ " AND data_lavratural_termo_embargo  < " +"'"+ mes_fim+"'" 

    cursor.execute(sql_emb)
    conexao.commit()
    retorno_not = cursor.fetchall()
    print(retorno[0][0])
    embargos_mes.append(retorno_not[0][0])
    
data_set_embargos = pd.DataFrame(index= nomes_meses, columns= ['Embargos'], data = embargos_mes)

data_set_embargos.loc['Janeiro'] = 52 + data_set_embargos.loc['Janeiro']
data_set_embargos.loc['Fevereiro'] = 1 + data_set_embargos.loc['Fevereiro'] 
data_set_embargos.loc['Março'] = 15 + data_set_embargos.loc['Março']
data_set_embargos.loc['Abril'] = 1 + data_set_embargos.loc['Abril']
data_set_embargos.loc['Maio'] = 8 + data_set_embargos.loc['Maio']
data_set_embargos.loc['Junho'] = 5 + data_set_embargos.loc['Junho']
data_set_embargos.loc['Julho'] = 16 + data_set_embargos.loc['Julho']
data_set_embargos.loc['Agosto'] = 3 + data_set_embargos.loc['Agosto']
data_set_embargos.loc['Setembro'] = 0 + data_set_embargos.loc['Setembro']
data_set_embargos.loc['Outubro'] = 0 + data_set_embargos.loc['Outubro']
data_set_embargos.loc['Novembro'] = 0 + data_set_embargos.loc['Novembro']
data_set_embargos.loc['Dezembro'] = 0 + data_set_embargos.loc['Dezembro']

print(data_set_embargos)

plt.figure(figsize=(10,8))
plt.bar(nomes_meses, data_set_embargos["Embargos"], width=0.5)
plt.xlabel("Meses")
plt.ylabel("Quantidade de termos")
plt.title('Embargos realizados em ações fiscais - 2022')
plt.show()



########################################### Interdições ##########################################


inter_mes = []
for i in range(len(meses)):
    mes_selected = meses[i]
    mes_inicio = mes_selected[0]
    mes_fim = mes_selected[1]
    sql_inter = "SELECT COUNT(id_termo_interdicao) FROM public.termo_interdicao WHERE data_lavratura_termo_interdicao >" + "'" + mes_inicio +"'" + "AND data_lavratura_termo_interdicao <" +"'" + mes_fim + "'" 

    cursor.execute(sql_inter)
    conexao.commit()
    retorno_int = cursor.fetchall()
    print(retorno[0][0])
    inter_mes.append(retorno_int[0][0])
    
data_set_inter = pd.DataFrame(index= nomes_meses, columns= ['Interdição'], data = inter_mes)

data_set_inter.loc['Janeiro'] = 0 + data_set_inter.loc['Janeiro']
data_set_inter.loc['Fevereiro'] = 1 + data_set_inter.loc['Fevereiro'] 
data_set_inter.loc['Março'] = 0 + data_set_inter.loc['Março']
data_set_inter.loc['Abril'] = 0 + data_set_inter.loc['Abril']
data_set_inter.loc['Maio'] = 0 + data_set_inter.loc['Maio']
data_set_inter.loc['Junho'] = 1 + data_set_inter.loc['Junho']
data_set_inter.loc['Julho'] = 17 + data_set_inter.loc['Julho']
data_set_inter.loc['Agosto'] = 0 + data_set_inter.loc['Agosto']
data_set_inter.loc['Setembro'] = 0 + data_set_inter.loc['Setembro']
data_set_inter.loc['Outubro'] = 0 + data_set_inter.loc['Outubro']
data_set_inter.loc['Novembro'] = 0 + data_set_inter.loc['Novembro']
data_set_inter.loc['Dezembro'] = 0 + data_set_inter.loc['Dezembro']

print(data_set_inter)

plt.figure(figsize=(10,8))
plt.bar(nomes_meses, data_set_inter["Interdição"], width=0.5)
plt.xlabel("Meses")
plt.ylabel("Quantidade de termos")
plt.title('Interdições realizadas em ações fiscais - 2022')
plt.show()


