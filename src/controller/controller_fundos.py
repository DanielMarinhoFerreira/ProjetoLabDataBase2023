from model.fundos import Fundos
from model.Administradores import Administradores
from connection.mongo_queries import MongoQueries
from time import sleep
import pandas as pd
import json

class Controller_Fundos:
    
    def __init__(self):
        self.mongo = MongoQueries()
        pass

    def inserir_fundos(self) -> None:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        lRet = [True, '']
        contin = ''
        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()
        
        # Solicita ao usuario o cadastro do Fundo
        #fundo = self.cadastro_fundo_teste() #"""teste"""
        ticker = input("Fundos (Novo): ")

        while not self.verifica_existencia(db=db,coluns='FUNDOS', seek=[("ticker",ticker)], header=[("_id", 0),("ticker",1)]):
            ticker = input("Fundos (Novo): ")

        
        fundo = self.cadastro_fundo(db=db, ticker=ticker) 
            
        if not self.verifica_existencia(db=db, coluns="ADMINISTRADORES", seek=[("cnpj_admin",fundo.get_cnpj_admin())], header=[("_id", 0), ("cnpj_admin",1)]):
            
            #Inserir o cadastro do Fundo
            result = db["FUNDOS"].insert_one({
                                    "ticker": fundo.get_Ticker(),
                                    "tipo_abbima": fundo.get_tipo_abbima(),
                                    "segmento": fundo.get_segmento(),
                                    "conta_emit": fundo.get_conta_emit(),
                                    "num_cotas": fundo.get_num_cota(),
                                    "razao_social": fundo.get_razao_social(),
                                    "cnpj": fundo.get_cnpj(),
                                    "nome_pregao": fundo.get_nome_pregao(),
                                    "prazo_duracao": fundo.get_prazo_doracao(),
                                    "tipo_gestao": fundo.get_tipo_gestao(),
                                    "cnpj_admin": fundo.get_cnpj_admin()
                                    })
            
            if result.inserted_id !='':   
                # Recupera os dados do novo ticker criado transformando em um DataFrame
                df_fundo = self.mongo.recover_data(db=db, coluns='FUNDOS', seek=[("ticker", fundo.get_Ticker())],  header=[("_id", 0),("ticker",1),("tipo_abbima",1)])
                
                print("Ticker: "+ df_fundo.ticker.values[0] +" : "+ df_fundo.tipo_abbima.values[0] +" Cadastrdo !")
        else:
            contin = input("Administrador não cadastrado, deseja cadastrar administrador ? Digite S ou N ")
                
            while lRet[0] != False and not lRet[1]:

                if contin.upper() == 'S':
                    lRet[0] = True
                    lRet[1] = contin.upper()
                elif contin.upper() == 'N':
                    lRet[0] = False
                    lRet[1] = contin.upper()
                else:
                    contin = input("Informe um valor valido. Digite S ou N : ")

            # caso valor for falso   
            if not lRet[0] and lRet[1] == 'N':
                print("serar finalizado sem realizar o cadastro do fundo")
                return None
            elif lRet[0] and lRet[1] == 'S':
                admin = Administradores()
                admin.set_cnpj(fundo.get_cnpj_admin())
                admin.set_nome(nome = input("nome (Novo): "))
                admin.set_telefone(telefone = input("Telefone (Novo): "))
                admin.set_email(email = input("E-mail (Novo): "))
                admin.set_site(site = input("Site (Novo): "))

                db["ADMINISTRADORES"].insert_one({
                                            "nome": admin.get_nome(),
                                            "telefone": admin.get_telefone(),
                                            "email": admin.get_email(),
                                            "url_site": admin.get_url_site(),
                                            "cnpj_admin": admin.get_cnpj_admin()
                                            })
                    
                # Recupera os dados do novo ticker criado transformando em um DataFrame
                df_admin = self.mongo.recover_data(db=db, coluns='ADMINISTRADORES', seek=[("cnpj_admin",admin.get_cnpj_admin())], header=[("_id", 0),("cnpj_admin",1),("nome",1)])
                
                print("administrador do CNPJ: "+ str(df_admin.cnpj_admin.values[0]) +" : "+ df_admin.nome.values[0] +" Cadastrdo !")
                    
                db["FUNDOS"].insert_one({
                                    "ticker": fundo.get_Ticker(),
                                    "tipo_abbima": fundo.get_tipo_abbima(),
                                    "segmento": fundo.get_segmento(),
                                    "conta_emit": fundo.get_conta_emit(),
                                    "num_cotas": fundo.get_num_cota(),
                                    "razao_social": fundo.get_razao_social(),
                                    "cnpj": fundo.get_cnpj(),
                                    "nome_pregao": fundo.get_nome_pregao(),
                                    "prazo_duracao": fundo.get_prazo_doracao(),
                                    "tipo_gestao": fundo.get_tipo_gestao(),
                                    "cnpj_admin": fundo.get_cnpj_admin()
                                    })
                
                # Recupera os dados do novo ticker criado transformando em um DataFrame
                df_fundo = self.mongo.recover_data(db=db, coluns='FUNDOS', seek=[("ticker", fundo.get_Ticker())],  header=[("_id", 0),("ticker",1),("tipo_abbima",1)])
                
                print("Ticker: "+ df_fundo.ticker.values[0] +" : "+ df_fundo.tipo_abbima.values[0] +" Cadastrdo !")
            else:
                print("ocorreu algum erro. Solicite verificação do TI")

    def atualizar_fundos(self) -> None:
        # Cria uma nova conexão com o banco que permite alteração
        
        db = self.mongo.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")

        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia(db=db, coluns='FUNDOS', seek=[("ticker", ticker)], header=[("_id", 0),("ticker",1),("tipo_abbima",1)]):
            # Solicita a nova descrição do cliente
            novo_segmento = input("Segmento (Novo): ")
            
            # Atualiza o nome do cliente existente
            result = db["FUNDOS"].update_one({"ticker": ticker}, {"$set": {"segmento": novo_segmento}})
            if result.matched_count > 0:
                # Recupera os dados do novo cliente criado transformando em um DataFrame
                df_fundo = self.mongo.recover_data(db=db, coluns='FUNDOS', seek=[("ticker", ticker)], header=[("_id", 0),("ticker",1),("segmento",1)])
            
                # Cria um novo objeto cliente
                print(df_fundo.ticker.values[0], df_fundo.segmento.values[0])
            ticker.__delattr__
        else:
            print(f"O ticker {ticker} informado não existe.")
            return None
    
    def excluir_fundos(self):
        # Cria uma nova conexão com o banco que permite alteração
        db = self.mongo.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        
        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia(db=db, coluns='FUNDOS', seek=[("ticker", ticker)],  header=[("_id", 0),("ticker",1),("tipo_abbima",1)]):            
            # Recupera os dados do fundo transformando em um DataFrame
            df_fundo = self.mongo.recover_data(db=db, coluns='FUNDOS', seek=[("ticker", ticker)],  header=[()])
            # Verificar se existe registro desse fundos na tabela cotações e dividendos
            if not self.verifica_existencia(db=db,coluns='COTACOES', seek=[("ticker", df_fundo.ticker.values[0])], header=[()]) and not self.verifica_existencia(coluns='DIVIDENDOS', seek=[("ticker", df_fundo.ticker.values[0])], header=[()]):
                if "S" == input(f"Tem certezar que deseja excluir registro das cotações e dividandos desse fundo: {df_fundo.ticker.values[0]} ? S OU N").upper():
                    # Recupera os dados do COTACOES transformando em um DataFrame
                    result = db["COTACOES"].delete_many({"ticker": df_fundo.ticker.values[0]})
                    print("quantidade de cotações "+df_fundo.ticker.values[0]+" deletadas do: "+ str(result.deleted_count))
                    
                    # Recupera os dados do DIVIDENDOS transformando em um DataFrame
                    result = db["DIVIDENDOS"].delete_many({"ticker": df_fundo.ticker.values[0]})
                    print("quantidade de dividendos "+df_fundo.ticker.values[0]+" deletados do: "+ str(result.deleted_count))  
                else:
                    print("Não é possivel exlcuir Fundo sem excluir a suas cotações e dividendos")
            else:
                # Se não existir dados nas tabela  COTACOES e DIVIDENDOS o sistema vai perguntar se deseja exluir esse fundo.
                if "S" == input(f"Tem certezar que deseja excluir fundo: {df_fundo.ticker.values[0]} ? S OU N").upper():
                    result = db["FUNDOS"].delete_many({"ticker": df_fundo.ticker.values[0]})
                    if result.deleted_count > 0:
                        print("fundo "+df_fundo.ticker.values[0]+" deletado !")    
                else: 
                    print("Não relaizar processo de exclução")
        else: 
            print("Não foi encontrardo o ticker informado para deleção")
    
    def cadastro_fundo(self, db ,ticker) -> Fundos:
            
            if ticker == '':
                ticker = input("Fundos (Novo): ")

                while not self.verifica_existencia(db=db, coluns='FUNDOS', seek={ "_id": 0, "ticker":ticker}):
                    ticker = input("Fundos (Novo): ")

            tipo_abbima = input("tipo_abbima (Novo): ")
            segmento = input("segmento (Novo): ")
            conta_emit = input("conta emitidas (Novo): ")
            num_cotas = input("Numero de cotistas (Novo): ")
            razao_social = input("razão social (Novo): ")
            
            sleep(1) #ms
            cnpj = input("cnpj (Novo): ")
            while not cnpj.isnumeric() or 14 < len(cnpj) or 15 <= len(cnpj):
                cnpj = input("cnpj (Novo): ")
                
            nome_pregao = input("nome pregão (Novo): ")
            prazo_doracao = input("prazo doracao (Novo): ")
            tipo_gestao = input("tipo gestao (Novo): ")
            cnpj_admin = input("cnpj administrador do fundo (Novo): ")
            
            fundos = Fundos(ticker=ticker, tipo_abbima=tipo_abbima, segmento=segmento, conta_emit=conta_emit,num_cotas=num_cotas,razao_social=razao_social, cnpj=cnpj, 
                                nome_pregao= nome_pregao, prazo_doracao=prazo_doracao, tipo_gestao=tipo_gestao, cnpj_admin=cnpj_admin)
            
            return fundos
    
    def verifica_existencia(self,db, coluns:str=None, seek:list=(), header:list=()) -> bool:
        
        if len(header) > 1:
            aux_header = dict(header)
        else:
            aux_header = {}
        
        df_cliente = pd.DataFrame(db[coluns].find(dict(seek), aux_header))
        
        return df_cliente.empty
    
