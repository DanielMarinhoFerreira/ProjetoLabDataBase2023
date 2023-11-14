from model.fundos import Fundos
from model.Administradores import Administradores
from connection.mongo_queries import MongoQueries
from time import sleep

class Controller_Fundos:
    
    def __init__(self):
        self.mongo = MongoQueries()
        pass

    def inserir_fundos(self) -> None:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        lRet = [True, '']
        contin = ''
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()
        
        # Solicita ao usuario o cadastro do Fundo
        #fundo = self.cadastro_fundo_teste() #"""teste"""
        fundo = self.cadastro_fundo()

        if self.verifica_existencia(coluns='FUNDOS', seek={}): #Verificar se exista no banco na tabela fondos 
            
            if not self.verifica_existencia(coluns="ADMINISTRADORES", seek={}):
                #Inserir o cadastro do Fundo
                self.mongo.db.fundos.insert_one({})
                
                # Recupera os dados do novo ticker criado transformando em um DataFrame
                df_fundo = self.mongo.recover_data(coluns='FUNDOS', seek={})
                #df_fundo = oracle.sqlToDataFrame(f"select ticker, TIPO_ABBIMA from FUNDOS where ticker = '{fundo.get_Ticker()}'")
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
                    admin.set_cnpj(fundo.get_cnpl_admin())
                    admin.set_nome(nome = input("nome (Novo): "))
                    admin.set_telefone(telefone = input("Telefone (Novo): "))
                    admin.set_email(email = input("E-mail (Novo): "))
                    admin.set_site(site = input("Site (Novo): "))

                    self.mongo.db.administradores.insert_one({})
                    
                    # Recupera os dados do novo ticker criado transformando em um DataFrame
                    df_admin = self.mongo.recover_data(coluns='ADMINISTRADORES', seek={})
                    #df_admin = oracle.sqlToDataFrame(f"select CNPJ_ADMIN, NOME from ADMINISTRADORES where CNPJ_ADMIN = '{admin.get_cnpj()}'")
                    print("administrador do CNPJ: "+ str(df_admin.cnpj_admin.values[0]) +" : "+ df_admin.nome.values[0] +" Cadastrdo !")
                    
                    self.mongo.db.fundos.insert_one()
                    #oracle.write(fundo.set_insert())
                
                    # Recupera os dados do novo ticker criado transformando em um DataFrame
                    df_fundo = self.mongo.recover_data(coluns='FUNDOS', seek={})
                    #df_fundo = oracle.sqlToDataFrame(f"select ticker, TIPO_ABBIMA from FUNDOS where ticker = '{fundo.get_Ticker()}'")
                    print("Ticker: "+ df_fundo.ticker.values[0] +" : "+ df_fundo.tipo_abbima.values[0] +" Cadastrdo !")

                else:
                    print("ocorreu algum erro. Solicite verificação do TI")
        else:
            print(f"O ticker: {fundo.get_Ticker()} desse fundo já está cadastrado.")
            return None 
        
    def atualizar_fundos(self) -> None:
        # Cria uma nova conexão com o banco que permite alteração
        
        self.mongo.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")

        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia(coluns='FUNDOS',seek={}):
            # Solicita a nova descrição do cliente
            novo_segmento = input("Segmento (Novo): ")
            # Atualiza o nome do cliente existente
            self.mongo.recover_data(coluns='FUNDOS', seek={})
            #oracle.write(f"UPDATE FUNDOS SET SEGMENTO ='{novo_segmento}' WHERE TICKER ='{ticker}'")
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_fundos = oracle.sqlToDataFrame(f" SELECT TICKER, SEGMENTO FROM FUNDOS WHERE TICKER = '{ticker}'")
            # Cria um novo objeto cliente
            print(df_fundos.ticker.values[0], df_fundos.segmento.values[0])
            ticker.__delattr__
        else:
            print(f"O ticker {ticker} informado não existe.")
            return None
    
    def excluir_fundos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        
        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia(oracle, ticker, tabela='FUNDOS',coluna=['ticker', 'ticker']):            
            # Recupera os dados do fundo transformando em um DataFrame
            df_fundo = oracle.sqlToDataFrame(f"SELECT TICKER, CNPJ_ADMIN FROM FUNDOS WHERE TICKER ='{ticker}'")
            # Verificar se existe registro desse fundos na tabela cotações e dividendos
            if not self.verifica_existencia(oracle, df_fundo.ticker.values[0], tabela='COTACOES',coluna=['ticker', 'id']) and not self.verifica_existencia(oracle, df_fundo.ticker.values[0], tabela='DIVIDENDOS',coluna=['ticker', 'id']):
                if "S" == input(f"Tem certezar que deseja excluir registro das cotações e dividandos desse fundo: {df_fundo.ticker.values[0]} ? S OU N").upper():
                    # Recupera os dados do COTACOES transformando em um DataFrame
                    df_cotas_fundo = oracle.sqlToDataFrame(f"SELECT ticker, id FROM COTACOES WHERE TICKER ='{ticker}'")
                    # Recupera os dados do DIVIDENDOS transformando em um DataFrame
                    df_dividendos_fundos = oracle.sqlToDataFrame(f"SELECT ticker, id FROM DIVIDENDOS WHERE TICKER ='{ticker}'")

                    for cota in df_cotas_fundo.size():
                        # deleta os registro da tebala COTACOES referente ao fundo 
                        ret = oracle.write(f"delete from COTACOES WHERE ID ='{cota.id.values()}'")
                        print(ret)        
                    for dividendo in df_dividendos_fundos.size():
                        # deleta os registro da tebala COTACOES referente ao fundo 
                        ret = oracle.write(f"delete from DIVIDENDOS WHERE ID ='{dividendo.id.values()}'")         
                else:
                    print("Não é possivel exlcuir Fundo sem excluir a suas cotações e dividendos")
            else:
                # Se não existir dados nas tabela  COTACOES e DIVIDENDOS o sistema vai perguntar se deseja exluir esse fundo.
                if "S" == input(f"Tem certezar que deseja excluir fundo: {df_fundo.ticker.values[0]} ? S OU N").upper():
                    oracle.write(f"delete from FUNDOS WHERE TICKER ='{df_fundo.ticker.values[0]}'")
                else: 
                    print("Não relaizar processo de exclução")
        else: 
            print("Não foi encontrardo o ticker informado para deleção")     

    def cadastro_fundo_teste(sekf) ->Fundos:
        ticker = 'HGFF11'
        tipo_abbima = 'HIBRIDO'
        segmento = 'papel'
        conta_emit = 300000
        num_cotas = 300000
        razao_social = 'TESTE'
        cnpj = '32784989000122'
        nome_pregao = 'FIAGRO SUNO'
        prazo_doracao = 'Indeterminado'
        tipo_gestao = 'Ativa'
        cnpj_admin = '806535000154'
        
        fundos = Fundos(ticker=ticker, tipo_abbima=tipo_abbima, segmento=segmento, conta_emit=conta_emit,num_cotas=num_cotas ,razao_social=razao_social, cnpj=cnpj, 
                                nome_pregao= nome_pregao, prazo_doracao=prazo_doracao, tipo_gestao=tipo_gestao, cnpj_admin=cnpj_admin)
            
        return fundos
    
    def cadastro_fundo(self) -> Fundos:
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
    
    def verifica_existencia(self, coluns:str=None, seek:dict={}) -> bool:
        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_cliente = pd.DataFrame(self.mongo.db[coluns].find(seek))
       
        return df_cliente.empty
    
    