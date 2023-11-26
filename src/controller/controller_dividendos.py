from model.dividendos import Dividendos
from connection.mongo_queries import MongoQueries
import pandas as pd

class Controller_Dividendos():
   
    def __init__(self):
        self.mongo = MongoQueries()
        pass
    
    def inserir_Dividendos(self) -> None:

        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()

        ## Solicita ao usuário o código do fundo a ser alterado
        div_ticker = input("informe o ticker do fundo: ")
        data_pag = input("Informe Data pagamento (Novo): ")
        while not self.verifica_existencia(db=db, coluns='DIVIDENDOS', seek=[("ticker", div_ticker),("data_pag", data_pag)], header=[()]):
            div_ticker = input("informe o ticker do fundo: ")
            data_pag = input("Informe Data pagamento (Novo): ")

        #df_div = self.mongo.recover_data(db=db, coluns='DIVIDENDOS', seek=[("ticker", div_ticker),("data_pag", data_pag)], header=[()])
        div = self.cadastrar_dividendos(ticker=div_ticker, data_pag=data_pag)
        
        #Inserir o cadastro do Fundo
        result = db["DIVIDENDOS"].insert_one({
                                            "ticker": div.get_ticker(),
                                            "data_pag": div.get_data_pag(),
                                            "cota_base": div.get_cota_base(),
                                            "ult_divid": div.get_ult_divid(),
                                            "rendimento": div.get_rendimento(),
                                            "div_yield": div.get_div_yield()
                                        })
                
        if result.inserted_id !='':
            # Recupera os dados do novo ticker criado transformando em um DataFrame
            df_div = self.mongo.recover_data(db=db, coluns="DIVIDENDOS", seek=[("ticker", div.get_ticker()),("data_pag", div.get_data_pag())], header=[()])
            print(df_div.ticker.values[0], df_div.data_pag.values[0])
        else:
            print("Já existe divindendo com essa informações cadastrado no sistema.")
        return
    
    def atualizar_Dividendos(self):

        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        div_ticker = input("informe o ticker do fundo: ")
        data_pag = input("Informe Data pagamento (Novo): ")
        while self.verifica_existencia(db=db, coluns='DIVIDENDOS', seek=[("ticker", div_ticker),("data_pag", data_pag)], header=[()]):
            div_ticker = input("informe o ticker do fundo: ")
            data_pag = input("Informe Data pagamento (Novo): ")
        
        atual_div = self.cadastrar_dividendos(ticker=div_ticker, data_pag=data_pag)

        dict_div = atual_div.__dict__
        aux_dict = {}

        for inf in dict_div:
                if dict_div[inf] !='':
                    aux_dict.update({inf:dict_div[inf]})
 
        if len(aux_dict) != 0:   
            document = {key: value for key, value in aux_dict.items()}
            
            result = db["DIVIDENDOS"].update_one({"ticker": div_ticker, "data_pag": data_pag },{"$set": document})

            if result.matched_count >0:
                df_div = self.mongo.recover_data(db=db, coluns='DIVIDENDOS', seek=[("ticker", div_ticker),("data_pag", data_pag)], header=[()])
            
                print("Atualizado!")
                print(df_div.head())
        else:
            print("Não foi Informado registro para alteração")
        return
    
    def deletar_Dividendos(self):

        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        div_ticker = input("informe o ticker do fundo: ")
        data_pag = input("Informe Data pagamento (Novo): ")
        while self.verifica_existencia(db=db, coluns='DIVIDENDOS', seek=[("ticker", div_ticker),("data_pag", data_pag)], header=[()]):
            div_ticker = input("informe o ticker do fundo: ")
            data_pag = input("Informe Data pagamento (Novo): ")

        df_div = self.mongo.recover_data(db=db, coluns='DIVIDENDOS', seek=[("ticker", div_ticker),("data_pag", data_pag)], header=[()])
        
        if not df_div.empty:
           result = db["DIVIDENDOS"].delete_one({"ticker": df_div.ticker.values[0], "data_pag": df_div.data_pag.values[0]})
           if result.deleted_count > 0:
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
    
    def verifica_existencia(self,db, coluns:str=None, seek:list=(), header:list=()) -> bool:
        
        if len(header) > 1:
            aux_header = dict(header)
        else:
            aux_header = {}
        
        df_cliente = pd.DataFrame(db[coluns].find(dict(seek), aux_header))
        
        return df_cliente.empty