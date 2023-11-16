from connection.mongo_queries import MongoQueries
#
# Implementar 
# Base montada 
# #
class Relatorio:
    
    def __init__(self):
        pass
    
    def get_relatorio(self, relatorio:str=''):

        if relatorio !='':
            with open("src/sql/"+relatorio) as f:
                self.query_relatorio = f.read()
        else:
            return None  
        if self.query_relatorio !='':

            mongo = MongoQueries()
            data = mongo.reports(self.query_relatorio)
            print(data.head())
            return 
        else: 
            return None