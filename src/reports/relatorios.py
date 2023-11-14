from connection.oracle_queries import OracleQueries
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

            oracle = OracleQueries()
            oracle.connect()
            data = oracle.sqlToDataFrame(self.query_relatorio)
            print(data.head())
            return 
        else: 
            return None