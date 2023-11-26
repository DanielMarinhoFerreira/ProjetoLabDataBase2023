from model.Administradores import Administradores 
from connection.mongo_queries import MongoQueries
from time import sleep
import pandas as pd

class Controller_Admin():
    
    def __init__(self):
        self.mongo = MongoQueries()
       

    def inserir_admin(self) -> None:

        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()
        
       
        # Solicita CNPJ do administrador 
        admin = input("informe o Cnpj do Administrador: ")
            
        while not admin.isnumeric() or len(admin) > 14 or len(admin) <= 13:
            admin = input("informe o Cnpj do Administrador: ")
       

        if self.verifica_existencia(db=db, coluns="ADMINISTRADORES", seek=[("cnpj_admin", admin)], header=[("_id",0),('cnpj_admin', 1)]): #Verificar se exista no banco na tabela fondos 
            # solicita o restante do cadastro 
            admin = self.cadastrar_admin(cnpj_admin=admin)
            
            # Inserir o cadastro do Fundo
            result = db["ADMINISTRADORES"].insert_one({
                                            "nome": admin.get_nome(),
                                            "telefone": admin.get_telefone(),
                                            "email": admin.get_email(),
                                            "url_site": admin.get_url_site(),
                                            "cnpj_admin": admin.get_cnpj_admin()
                                            })
            
            if result.inserted_id !='':
                # Recupera os dados do novo ticker criado transformando em um DataFrame
                seek_admin = self.mongo.recover_data(db=db, coluns="ADMINISTRADORES",seek=[('cnpj_admin',admin.get_cnpj_admin())], header=[()]) #erminar com dict de busca no db
                print("administrador cadastrado !")
                print(seek_admin.head())
                
        else:
            print(f"Existe Administrador cadastrado com esse CNPJ {admin}")
            return None 
    
    def atualizar_admin(self):
        
        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()

        # Solicita ao usuario o cadastro do Fundo
        admin = input("informe o Cnpj do Administrador: ")
        
        while not admin.isnumeric() or len(admin) > 14 or len(admin) <= 13:
            admin = input("informe o Cnpj do Administrador: ")

        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia(db=db, coluns='ADMINISTRADORES', seek=[('cnpj_admin',admin)], header=[()]):
            obj_admin = self.cadastrar_admin(cnpj_admin=admin)

            
            dict_div = obj_admin.__dict__
            aux_dict = {}

            for inf in dict_div:
                if dict_div[inf] !='' and inf != 'cnpj_admin':
                    aux_dict.update({inf:dict_div[inf]})
 
            if len(aux_dict) != 0:   
                document = {key: value for key, value in aux_dict.items()}
                result = db["ADMINISTRADORES"].update_one({"cnpj_admin": admin},{'$set': document})
            
            if result.matched_count:
                # Recupera os dados do novo ticker criado transformando em um DataFrame
                seek_admin = self.mongo.recover_data(db=db, coluns="ADMINISTRADORES",seek=[('cnpj_admin',admin)], header=[()]) #erminar com dict de busca no db
                print("administrador cadastrado !")
                print(seek_admin.head())
            
            obj_admin.__delattr__
        else:
            print(f"O Cnpj {admin._cnpj} do Administrador informado não existe.")
            aux = input("deseja temtar novamente infrome S ou N: ")
            if aux.upper == 'S':
                self.atualizar_admin()
            return None 
      
    def deletar_admin(self):
        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()
        
        # Solicita ao usuario o cadastro do Fundo
        admin = input("informe o Cnpj do Administrador: ")
        
        while not admin.isnumeric() or 14 < len(admin) or 15 <= len(admin):
            admin = input("informe o Cnpj do Administrador: ")
        
        if not self.verifica_existencia(db=db, coluns='ADMINISTRADORES', seek=[('cnpj_admin',admin)], header=[()]): #Criar pesquisa 

            # Recupera os dados do fundo transformando em um DataFrame
            df_fundo = self.mongo.recover_data(db=db, coluns='FUNDOS', seek=[("cnpj_admin", admin)],  header=[()])
        
            if not self.verifica_existencia(db=db, coluns='FUNDOS', seek=[("ticker", df_fundo.ticker.values[0])], header=[("_id", 0),("ticker",1),("tipo_abbima",1)]):       #Criar pesquisa
                
                # Verificar se existe registro desse fundos na tabela cotações e dividendos
                if not self.verifica_existencia(db=db, coluns='COTACOES', seek=[("ticker", df_fundo.ticker.values[0])], header=[("_id", 0),("ticker",1)]) and not self.verifica_existencia(db=db, coluns='DIVIDENDOS', seek=[("ticker", df_fundo.ticker.values[0])] ,header=[("_id", 0),("ticker",1)]):
                
                    if "S" == input(f"Tem certezar que deseja excluir registro das cotações e dividandos desse fundo: {df_fundo.ticker.values[0]} ? S OU N").upper():
                        # Recupera os dados do COTACOES transformando em um DataFrame
                        df_cotas_fundo = self.mongo.recover_data(db=db, coluns='COTACOES', seek=[("ticker", df_fundo.ticker.values[0])], header=[])
                        # Recupera os dados do DIVIDENDOS transformando em um DataFrame
                        df_dividendos_fundos = self.mongo.recover_data(db=db, coluns='DIVIDENDOS', seek=[("ticker", df_fundo.ticker.values[0])], header=[])

                        
                        # deleta os registro da tebala COTACOES referente ao fundo 
                        result =  db["COTACOES"].delete_many({"ticker": df_cotas_fundo.ticker.values[0]})
                        print(str(result.deleted_count) + " deletado da cotações do ticker: "+ df_cotas_fundo.ticker.values[0])        
                        
                        # deleta os registro da tebala COTACOES referente ao fundo
                        result = db["DIVIDENDOS"].delete_many({"ticker": df_dividendos_fundos.ticker.values[0]})
                        print(str(result.deleted_count) + " deletado dividendos do ticker: "+ df_dividendos_fundos.ticker.values[0])        
                        
                    else:
                        print("Não é possivel exlcuir Fundo sem excluir a suas cotações e dividendos")
                else:
                    # Se não existir dados nas tabela  COTACOES e DIVIDENDOS o sistema vai perguntar se deseja exluir esse fundo.
                    if "S" == input(f"Tem certezar que deseja excluir fundo: {df_fundo.ticker.values[0]} ? S OU N ").upper():
                        
                        # deleta os registro da tebala fundos referente ao fundo 
                        result =  db["FUNDOS"].delete_many({"cnpj_admin": df_cotas_fundo.cnpj_admin.values[0]})
                        print(str(result.deleted_count) + " deletado da cotações do ticker: "+ df_cotas_fundo.cnpj_admin.values[0]) 

                    else: 
                        print("Não relaizar processo de exclução")
            else: 
                if "S" == input(f"Tem certezar que deseja excluir esse administrador do Cnpj : {admin} ? S OU N ").upper():
                        
                        # deleta os registro da tebala administradores referente ao fundo 
                        result =  db["FUNDOS"].delete_many({"cnpj_admin": admin})
                        print(str(result.deleted_count) + " deletado o administradores" ) 
                   
                else: 
                    print(f"processo de deletção abortado !")
        else:
            print("Não foi encontrado registro desse administrador")
                               
    def cadastrar_admin(self, cnpj_admin:str='') -> Administradores:
        
        admin = Administradores()

        if cnpj_admin == '' or not cnpj_admin.isnumeric():
        
            cnpj_admin = input("cnpj (Novo): ")
            while not cnpj_admin.isnumeric() or len(cnpj_admin) > 14 or len(cnpj_admin) <= 13:
                cnpj_admin = input("cnpj (Novo): ")
                
        admin.set_cnpj(cnpj_admin=cnpj_admin)
        admin.set_nome(nome = input("nome (Novo): "))
        admin.set_telefone(telefone = input("Telefone (Novo): "))
        admin.set_email(email = input("E-mail (Novo): "))
        admin.set_site(url_site = input("Site (Novo): "))
        
        return admin 
    

    def verifica_existencia(self,db, coluns:str=None, seek:list=(), header:list=()) -> bool:
        
        if len(header) > 1:
            aux_header = dict(header)
        else:
            aux_header = {}
        
        df_cliente = pd.DataFrame(db[coluns].find(dict(seek), aux_header))
        
        return df_cliente.empty