
class Produtividade:
    import psycopg2


    def __init__(self, matricula, data_inicial, data_final):
        self.matricula = matricula
        self.data_inicial = data_inicial
        self.data_final = data_final
    
    def notificacao():
        sql = "SELECT * FROM "
        conexao = psycopg2.connect(host='faus.arapiraca.al.gov.br', port = '5432', database='db_faus',
                                   user='fiscal', password='db#f1sc@l@R@19')
        cursor = conexao.cursor()  
        cursor.execute(sql)
        conexao.commit()

        return 0
    def auto_infracao():
        sql_lavratura = "SELECT COUNT(id_auto_infracao) FROM public.termo_auto_infracao WHERE fiscal_lavratura_auto_infracao = '100854' AND data_lavratura_auto_infracao >= '2023-01-01' AND data_lavratura_auto_infracao <= '2023-01-31'"
        sql_testemunha = "SELECT COUNT(id_auto_infracao) FROM public.termo_auto_infracao WHERE fiscal_testemunha_auto_infracao ILIKE '%100854%' AND data_lavratura_auto_infracao >= '2023-01-01' AND data_lavratura_auto_infracao <= '2023-01-31'"
        return 0
    def embargo():
        return 0
    def interdicao():
        return 0
    def apreensao():
        return 0
    def plantao():
        return 0
    def processos_criados():
        sql_abertura = "SELECT COUNT(codigo_processo) FROM public.processo WHERE data_processo >= '2023-01-01' AND data_processo <= '2023-01-31' AND fiscal_matricula_processo = '100854'"
        sql_participante = "SELECT * FROM public.processo WHERE data_processo >= '2023-01-01' AND data_processo <= '2023-01-31' AND fiscais_participantes ILIKE '%100854%'"
        return 0
    def processos_finalizados():
        sql = "SELECT COUNT(id) FROM public.processos_finalizados WHERE ano ='2023' AND mes = 'Jan' AND fiscal = '100854' AND status = 'Finalizado';"
        return 0