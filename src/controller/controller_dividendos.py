from model.dividendos import Dividendos
from connection.mongo_queries import MongoQueries
import pandas as pd

class Controller_Dividendos():
   
    def __init__(self):
        self.mongo = MongoQueries()
        pass
    
    def inserir_Dividendos(self) -> None:

        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        ## Solicita ao usuário o código do fundo a ser alterado
        div_ticker = input("informe o ticker do fundo: ")
        data_pag = input("Informe Data pagamento (Novo): ")
        while not self.verifica_existencia(coluns='DIVIDENDOS', seek={}):
            div_ticker = input("informe o ticker do fundo: ")
            data_pag = input("Informe Data pagamento (Novo): ")

        divid = self.cadastrar_dividendos(ticker=div_ticker, data_pag=data_pag)
        
        if self.verifica_existencia(coluns='DIVIDENDOS', seek={}):
            #Inserir o cadastro do Fundo
            self.mongo.db.dividendos.update_one({})
                
            # Recupera os dados do novo ticker criado transformando em um DataFrame
            df_div = self.mongo.recover_data(coluns="DIVIDENDOS", seek={})
            print(df_div.ticker.values[0], df_div.data_pag.values[0])
        else:
            print("Já existe divindendo com essa informações cadastrado no sistema.")
        return
    
    def atualizar_Dividendos(self):

        # Cria uma nova conexão com o banco que permite alteração
       
        self.mongo.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        div_ticker = input("informe o ticker do fundo: ")
        data_pag = input("Informe Data pagamento (Novo): ")
        while self.verifica_existencia(coluns='DIVIDENDOS', seek={}):
            div_ticker = input("informe o ticker do fundo: ")
            data_pag = input("Informe Data pagamento (Novo): ")

        df_div = self.mongo.recover_data(coluns='DIVIDENDOS', seek={})
        # df_div = oracle.sqlToDataFrame(f"""SELECT ID,TICKER, DATA_PAG FROM DIVIDENDOS  WHERE TICKER = '{div_ticker}' AND DATA_PAG ='{data_pag}'""")
        
        atual_div = self.cadastrar_dividendos(ticker=div_ticker, data_pag=data_pag)

        dict_div = atual_div.__dict__
        aux_dict = {}

        for inf in dict_div:
                if dict_div[inf] !='':
                    aux_dict.update({inf:dict_div[inf]})
 
        if len(aux_dict) != 0:   
            document = {key: value for key, value in aux_dict.items()}
            
            self.mongo.db.dividendos.update_one({"TICKER": "DIVIDENDOS"},{"$set": document}, upsert=True)
            
            
            df_div = self.mongo.recover_data(coluns="DIVIDENDOS", seek={})
            #df_div = oracle.sqlToDataFrame(f"""SELECT TICKER, DATA_PAG, COTA_BASE, ULT_DIVID, RENDIMENTO, DIV_YIELD FROM DIVIDENDOS  WHERE TICKER = '{atual_div.get_ticker()}' AND DATA_PAG ='{atual_div.get_data_pag()}'""")
            print("Atualizado!")
            print(df_div.head())
        else:
            print("Não foi Informado registro para alteração")
        return
    
    def deletar_Dividendos(self):

        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        div_ticker = input("informe o ticker do fundo: ")
        data_pag = input("Informe Data pagamento (Novo): ")
        
        while self.verifica_existencia(coluns='DIVIDENDOS', seek={}):
            div_ticker = input("informe o ticker do fundo: ")
            data_pag = input("Informe Data pagamento (Novo): ")

        df_div = self.mongo.recover_data(coluns='DIVIDENDOS', seek={})
        #df_div = oracle.sqlToDataFrame(f"""SELECT ID, TICKER, DATA_PAG, COTA_BASE, ULT_DIVID, RENDIMENTO, DIV_YIELD FROM DIVIDENDOS  WHERE TICKER = '{div_ticker}' AND DATA_PAG ='{data_pag}'""")

        if not df_div.empty:
            #query = f""" DELETE FROM DIVIDENDOS WHERE TICKER = '{df_div.ticker.values[0]}' AND DATA_PAG ='{df_div.data_pag.values[0]}' AND ID='{df_div.id.values[0]}'"""
            self.mongo.db.dividendos.delete_one({"ticker": df_div.ticker.values[0]})
            print("deletado com sucesso !")
        else:
            print("Registro informado Não encontrado")
        return
    
    def cadastrar_dividendos(self, ticker:str='', data_pag:str='') -> Dividendos:
        
        dividendo = Dividendos()
        
        while ticker == '' or data_pag =='':
            ticker = input("informe o ticker do fundo: (Novo): ")
            data_pag = input("Informe Data pagamento (Novo): ")

        dividendo.set_ticker(ticker=ticker)
        dividendo.set_data_pag(data_pag=data_pag)
        dividendo.set_div_yield(div_yield= input("Informe Dividend Yield (Novo): "))
        dividendo.set_cota_base(cota_base= input("Informe cotação (Novo): "))
        dividendo.set_rendimento(rendimento= input("Informe Rendimento dividendo (Novo): "))
        dividendo.set_ult_divid(ult_divid= input("Informe porcentagem do Dy.Ult (Novo): "))
        
        return dividendo
    
    def verifica_existencia(self, coluns:str=None, seek:dict={}) -> bool:
        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_cliente = pd.DataFrame(self.mongo.db[coluns].find(seek))
       
        return df_cliente.empty
    