from model.Cotacoes import Cotacoes
from connection.mongo_queries import MongoQueries
import pandas as pd

class Controller_Cotacoes():
    
    def __init__(self):
        self.mongo = MongoQueries()
        pass
    
    def inserir_cotacoes(self) -> None:
        
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        while self.verifica_existencia(coluns='FUNDOS', seek={}):
            ticker = input("informe o ticker do fundo: ")
        
        # Solicita ao usuario o cadastro do cotacoes
        cota = self.cadastrar_cotacao(ticker=ticker)

        if self.verifica_existencia(coluna='COTACOES', seek={}):
            
            #Inserir o cadastro do Fundo
            self.mongo.recover_data(coluns="COTACOES", external=True, seek={}) 
                
            # Recupera os dados do novo ticker criado transformando em um DataFrame
            df_fundo  = self.mongo.recover_data(coluns='COTACOES', seek={})

            print(df_fundo.ticker.values[0], df_fundo.mes.values[0])
        else: 
            print('já existe uma cota cadastrada desse mês')
        return
    
    def atualizar_cotacoes(self):
        
        # Cria uma nova conexão com o banco que permite alteração
       
        self.mongo.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        mes = input("informe mês: ")
        while self.verifica_existencia(colu ='COTACOES', coluna=['ID','TICKER','MES']):
            ticker = input("informe o ticker do fundo: ")
            mes = input("informe mês: ")
        
        df_cota = self.verifica_existencia(coluns='COTACOES', seek={}) #criar consulta  
        
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
            
                self.mongo.db.administradores.update_one({"TICKER": ticker},{"$set": document}, upsert=True)
            else:
                print("Não foi informado informações pra alteração")    
        else: 
            print('Ticker do Fundo informado não existe!')
        return
    
    '''falta realizar deleção'''
    def deletar_cotacoes(self):
        
        # Cria uma nova conexão com o banco que permite alteração
        
        self.mongo.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        mes = input("informe mês: ")
        while self.verifica_existencia(coluns='COTACOES', seek={}):
            ticker = input("informe o ticker do fundo: ")
            mes = input("informe mês: ")
        
        df_cota = self.mongo.recover_data(coluns="COTACOES", seek={})
        
        if not df_cota.empty:

            #Inserir o cadastro do Fundo
            self.mongo.recover_data(coluns='COTACOES', seek={}, external=True)

        return
    
    def cadastrar_cotacao(self, ticker:str='') -> Cotacoes:
        mes:str = ''
        cotacao = Cotacoes()

         # Cria uma nova conexão com o banco que permite alteração
        
        self.mongo.connect()
        
        if ticker == '':
            ticker = input("Ticker (Novo): ")
            while self.verifica_existencia(coluns='FUNDOS', seek={}):
                ticker = input("informe o ticker do fundo: ")
        
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
    

    def verifica_existencia(self, coluns:str=None, seek:dict={}) -> bool:
        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_cliente = pd.DataFrame(self.mongo.db[coluns].find(seek))
       
        return df_cliente.empty