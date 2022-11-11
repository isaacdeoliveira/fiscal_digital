
class Produtividade:
    import psycopg2
    def __init__(self, matricula, data_inicial, data_final):
        self.matricula = matricula
        self.data_inicial = data_inicial
        self.data_final = data_final
    
    def notificacao():
        conexao = psycopg2.connect(host='faus.arapiraca.al.gov.br', port = '5432', database='db_faus',
        user='fiscal', password='db#f1sc@l@R@19')
        cursor = conexao.cursor()  
        sql= "SELECT "
        cursor.execute(sql)
        conexao.commit()
        sql = "SELECT * FROM "
        return 0
    def auto_infracao():
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
        return 0
    def processos_finalizados():
        return 0