import pymongo
import pandas as pd

class MongoQueries:
    def __init__(self):
        self.host = "localhost"
        self.port = 27017
        self.service_name = 'labdatabase'

        with open("src/connection/passPhrase/authentication.mongo", "r") as f:
            self.user, self.passwd = f.read().split(',')

    def __del__(self):
        if hasattr(self, "mongo_client"):
            self.close()

    def connect(self):
        self.mongo_client = pymongo.MongoClient(f"mongodb://{self.user}:{self.passwd}@localhost:27017/")
        self.db = self.mongo_client["labdatabase"]
        return self.db

    def close(self):
        self.mongo_client.close()

    # Consulta de contagem de registros por tabela
    def query_count(self, collection_name):

        mongo = self.connect()

        my_collection = mongo[collection_name]
        total_documentos = my_collection.count_documents({})
        self.close()
        df = pd.DataFrame({f"total_{collection_name}": [total_documentos]})
        return df

    # Recupera os dados da coleção do MongoDB e retorna como Dataframe
    def recover_data(self, db ,coluns:str=None, seek:list=(), header:list=()) -> pd.DataFrame:
        """
        @param: coluns -> coluna de busca dos dados
        @param: external -> permite uma nova conexão com o banco que permite alteração
        @param: seek -> informação de busca ex.: [("cpf", 12058236528)]
        @param: header -> Informação de retorno da busca ex.: [("nome", 1),("_id", 0)]
        """ 

        if len(header) > 1:
            aux_header = dict(header)
        else:
            aux_header = {}
        # Recupera os dados do novo cliente criado transformando em um DataFrame
        if coluns != '' and len(seek) > 0:
            df_data = pd.DataFrame(list(db[coluns].find(dict(seek), aux_header)))
        else:
            return None

        return df_data