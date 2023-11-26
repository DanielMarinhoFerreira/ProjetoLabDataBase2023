from model.Cotacoes import Cotacoes
from connection.mongo_queries import MongoQueries
import pandas as pd

class Controller_Cotacoes():
    
    def __init__(self):
        self.mongo = MongoQueries()
        pass
    
    def inserir_cotacoes(self) -> None:
        
        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        while self.verifica_existencia(coluns='FUNDOS', seek={}):
            ticker = input("informe o ticker do fundo: ")
        
        # Solicita ao usuario o cadastro do cotacoes
        cota = self.cadastrar_cotacao(ticker=ticker)

        if self.verifica_existencia(coluna='COTACOES', seek={}):
            
            #Inserir o cadastro do Fundo
            result = db["COTAOES"].insert_one({
                                        "ticker": cota.get_ticker(),
                                        "data_cota": cota.get_data_cota(),
                                        "cota_atual": cota.get_cota_atual(),
                                        "redimento_atual": cota.get_rendimento_atual(),
                                        "minimo_cota": cota.get_minimo(),
                                        "maximo_cota": cota.get_maximo(),
                                        "abertura": cota.get_abertura(),
                                        "volume_cotas": cota.get_volume_cotas(),
                                        "mes": cota.get_mes(),
                                        "p_vp": cota.get_mes()
                                        })
            
            if result.inserted_id !='':  
                # Recupera os dados do novo ticker criado transformando em um DataFrame
                df_fundo  = self.mongo.recover_data(db=db, coluns='COTACOES', seek=[("ticker", cota.get_ticker()),("mes", cota.get_mes())], header=[("_id", 0),("ticker",1),("mes",1)])

                print(df_fundo.ticker.values[0], df_fundo.mes.values[0])
        else: 
            print('já existe uma cota cadastrada desse mês')
        return
    
    def atualizar_cotacoes(self):
        
        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        mes = input("informe mês: ")
        while self.verifica_existencia(db=db, coluns='COTACOES', seek=[("ticker", ticker),("mes", mes)], header=[("_id", 0),("ticker",1),("mes",1)]):
            ticker = input("informe o ticker do fundo: ")
            mes = input("informe mês: ")
        
        df_cota = self.mongo.recover_data(db=db, coluns='COTACOES', seek=[("ticker", ticker),("mes", mes)], header=[("_id", 0),("ticker",1),("mes",1)])
        
        if not df_cota.empty:
            
            cotacao = Cotacoes()
            cotacao.set_cota_atual(cota_atual = input("Cotação Atual (Novo): "))
            cotacao.set_rendimento_atual(rendimento = input("Rendimento (Novo): "))
            cotacao.set_minimo(minimo_cota = input("Cota minima (Novo): "))
            cotacao.set_maximo(maximo_cota= input("Cota maxima (Novo): "))
            cotacao.set_abertura(abertura= input("Abertura (Novo): "))
            cotacao.set_volume_cotas(volume_cotas= input("Valume Cotas (Novo): "))
            cotacao.set_p_vp(p_vp= input("P_VP (Novo): "))

            dict_cota = cotacao.__dict__
            aux_dict = {}
            
           
            for inf in dict_cota:
                if dict_cota[inf] !='':
                    aux_dict.update({inf:dict_cota[inf]})
            
            if len(aux_dict) != 0:   
                document = {key: value for key, value in aux_dict.items()}
            
                self.mongo.db.administradores.update_one({"ticker": ticker, "mes": mes},{"$set": document}, upsert=True)
            else:
                print("Não foi informado informações pra alteração")    
        else: 
            print('Ticker do Fundo informado não existe!')
        return
    
    
    def deletar_cotacoes(self):
        
        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        mes = input("informe mês: ")
        while self.verifica_existencia(db=db, coluns='COTACOES', seek=[("ticker", ticker),("mes", mes)], header=[("_id", 0),("ticker",1),("mes",1)]):
            ticker = input("informe o ticker do fundo: ")
            mes = input("informe mês: ")
        
        df_cota = self.mongo.recover_data(db=db, coluns='COTACOES', seek=[("ticker", ticker),("mes", mes)], header=[("_id", 0),("ticker",1),("mes",1)])
        
        if not df_cota.empty:
            result = db["COTACOES"].delete_one({"ticker":df_cota.ticker.values[0], "mes": df_cota.mes.values[0]})

            if result.deleted_count > 0:
                print(f"Cotação ticker {str(df_cota.ticker.values[0])} mes: {str(df_cota.mes.values[0])} deletada do sistema")
        return
    
    def cadastrar_cotacao(self, ticker:str='') -> Cotacoes:
        mes:str = ''
        cotacao = Cotacoes()

         # Cria uma nova conexão com o banco que permite alteração
        
        self.mongo.connect()
        
        if ticker == '' and mes == '':
            ticker = input("Ticker (Novo): ")
            while self.verifica_existencia(coluns='FUNDOS', seek={}):
                ticker = input("informe o ticker do fundo: ")
                mes = input("Mês cotação (Novo): ")
        
        cotacao.set_ticker(ticker)
        cotacao.set_data_cota(data_atual = input("Data cotação (Novo): "))
        cotacao.set_cota_atual(cota_atual = input("Cotação Atual (Novo): "))
        cotacao.set_rendimento_atual(rendimento = input("Rendimento (Novo): "))
        cotacao.set_minimo(minimo_cota= input("Cota minima (Novo): "))
        cotacao.set_maximo(maximo_cota= input("Cota maxima (Novo): "))
        cotacao.set_abertura(abertura= input("Abertura (Novo): "))
        cotacao.set_volume_cotas(volume_cotas= input("Valume Cotas (Novo): "))
        
        mes= input("Mês cotação (Novo): ")
        
        while not self.verifica_existencia(coluns='COTACOES', seek={}):
            mes = input("Mês cotação (Novo): ")

        cotacao.set_mes(mes)
        cotacao.set_p_vp(p_vp= input("P_VP (Novo): "))
  
        return cotacao 
    

    def verifica_existencia(self,db, coluns:str=None, seek:list=(), header:list=()) -> bool:
        
        if len(header) > 1:
            aux_header = dict(header)
        else:
            aux_header = {}
        
        df_cliente = pd.DataFrame(db[coluns].find(dict(seek), aux_header))
        
        return df_cliente.empty