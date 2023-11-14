from model.Administradores import Administradores 
from connection.mongo_queries import MongoQueries
from time import sleep
import pandas as pd

class Controller_Admin():
    
    def __init__(self):
        self.mongo = MongoQueries()
       

    def inserir_admin(self) -> None:

        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()
        
       
        # Solicita CNPJ do administrador 
        admin = input("informe o Cnpj do Administrador: ")
            
        while not admin.isnumeric() or len(admin) > 14 or len(admin) <= 13:
            admin = input("informe o Cnpj do Administrador: ")
       

        if self.verifica_existencia(coluns="Administradores", seek={"CNPJ_ADMIN": admin}): #Verificar se exista no banco na tabela fondos 
            # solicita o restante do cadastro 
            admin = self.cadastrar_admin(cnpj_admin=admin)
            
            # Inserir o cadastro do Fundo
            #self.mongo.db.update_one({"CNPJ_ADMIN": admin},{"$set":{}}, upsert=True)) #Terminar com dict de insert no db
            
            # Recupera os dados do novo ticker criado transformando em um DataFrame
            seek_admin = self.mongo.recover_data(coluns="Administradores",seek={}) #erminar com dict de busca no db
            new_admin = Administradores(nome=seek_admin.nome.values[0], 
                                        telefone=seek_admin.telefone.values[0], 
                                        email=seek_admin.email.values[0],
                                        url_site=seek_admin.url_site.values[0],
                                        cnpj_admin=seek_admin.cnpj_admin.values[0])
            print(new_admin.to_string())
            self.mongo.close()
            return new_admin
        else:
            print(f"Existe Administrador cadastrado com esse CNPJ {admin}")
            return None 
    
    def atualizar_admin(self):
        
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuario o cadastro do Fundo
        admin = input("informe o Cnpj do Administrador: ")
        
        while not admin.isnumeric() or len(admin) > 14 or len(admin) <= 13:
            admin = input("informe o Cnpj do Administrador: ")


        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia(admin=admin):
            obj_admin = self.cadastrar_admin(cnpj_admin=admin)

            
            dict_div = obj_admin.__dict__
            aux_dict = {}

            for inf in dict_div:
                if dict_div[inf] !='' and inf != 'cnpj_admin':
                    aux_dict.update({inf:dict_div[inf]})
 
            if len(aux_dict) != 0:   
                document = {key: value for key, value in aux_dict.items()}
                self.mongo.db.administradores.update_one({"CNPJ_ADMIN": admin},{"$set": document}, upsert=True)
            
            seek_admin = self.mongo.recover_data(coluns="Administradores",seek={}) #terminar com dict de busca no db
            new_admin = Administradores(nome=seek_admin.nome.values[0], 
                                        telefone=seek_admin.telefone.values[0], 
                                        email=seek_admin.email.values[0],
                                        url_site=seek_admin.url_site.values[0],
                                        cnpj_admin=seek_admin.cnpj_admin.values[0])
            print(new_admin.to_string())
            self.mongo.close()
            
            admin.__delattr__
        else:
            print(f"O Cnpj {admin._cnpj} do Administrador informado não existe.")
            return None 
      
    def deletar_admin(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()
        
        # Solicita ao usuario o cadastro do Fundo
        admin = input("informe o Cnpj do Administrador: ")
        
        while not admin.isnumeric() or 14 < len(admin) or 15 <= len(admin):
            admin = input("informe o Cnpj do Administrador: ")
        
        if not self.verifica_existencia(coluns="Administradores", seek={}): #Criar pesquisa 
        
            if not self.verifica_existencia(coluns='FUNDOS',seek={}):       #Criar pesquisa
                # Recupera os dados do fundo transformando em um DataFrame
                df_fundo = self.mongo.recover_data(coluns="FUNDOS", seek={}) # Montar busca
                # Verificar se existe registro desse fundos na tabela cotações e dividendos
                if not self.verifica_existencia(coluns='COTACOES',seek={}) and not self.verifica_existencia(coluns='DIVIDENDOS', seek={}):
                
                    if "S" == input(f"Tem certezar que deseja excluir registro das cotações e dividandos desse fundo: {df_fundo.ticker.values[0]} ? S OU N").upper():
                        # Recupera os dados do COTACOES transformando em um DataFrame
                        df_cotas_fundo = self.mongo.recover_data(coluns='COTACOES', seek={})
                        # Recupera os dados do DIVIDENDOS transformando em um DataFrame
                        df_dividendos_fundos = self.mongo.recover_data(coluns='DIVIDENDOS', seek={})

                        for cota in df_cotas_fundo.size():
                            # deleta os registro da tebala COTACOES referente ao fundo 
                            ret =  self.mongo.recover_data(coluns="COTACOES" ,seek={}, external=True)
                            print(ret)        
                        for dividendo in df_dividendos_fundos.size():
                            # deleta os registro da tebala COTACOES referente ao fundo
                            ret = self.mongo.recover_data(coluns="DIVIDENDOS", seek={}, external=True)
                        
                        self.mongo.recover_data(coluns='ADMINISTRADORES', seek={}, external=True)
                    else:
                        print("Não é possivel exlcuir Fundo sem excluir a suas cotações e dividendos")
                else:
                    # Se não existir dados nas tabela  COTACOES e DIVIDENDOS o sistema vai perguntar se deseja exluir esse fundo.
                    if "S" == input(f"Tem certezar que deseja excluir fundo: {df_fundo.ticker.values[0]} ? S OU N ").upper():
                        self.mongo.recover_data(coluns='FUNDOS', seek={}, external=True)
                    
                        self.mongo.recover_data(coluns='ADMINISTRADORES', seek={}, external=True)
                       
                    else: 
                        print("Não relaizar processo de exclução")
            else: 
                if "S" == input(f"Tem certezar que deseja excluir esse administrador do Cnpj : {admin} ? S OU N ").upper():
                   self.mongo.recover_data(coluns='ADMINISTRADORES', seek={}, external=True)
                   
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
    

    def verifica_existencia(self, coluns:str=None, seek:dict={}) -> bool:
        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_cliente = pd.DataFrame(self.mongo.db[coluns].find(seek))
       
        return df_cliente.empty