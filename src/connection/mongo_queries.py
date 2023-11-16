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

        my_collection = mongo.db[collection_name]
        total_documentos = my_collection.count_documents({})
        self.close()
        df = pd.DataFrame({f"total_{collection_name}": [total_documentos]})
        return df
    
    def reports(self, collection_name) -> pd.DataFrame:

        mongo = self.connect()
        collection = collection_name.replace("\n", '')
        my_Collection = mongo.db[collection]

        data_fd = pd.DataFrame(my_Collection)

        return data_fd

    def recover_data(self, coluns:str=None, external:bool=False, seek:dict={}) -> pd.DataFrame:
        """
        @param: coluns -> coluna de busca dos dados
        @param: external -> permite uma nova conexão com o banco que permite alteração
        @param: seek -> dicionario contendo a informação de busca ou de insert exe.: {"cpf": 1, "nome": 1, "_id": 0}
        """       
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        if not coluns and not seek:
            df_data = pd.DataFrame(list(self.mongo.db[coluns].find(seek)))
        else:
            return None
        
        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_data