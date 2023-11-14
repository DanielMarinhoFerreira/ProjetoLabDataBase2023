from connection.mongo_queries import MongoQueries

class SplashScreen:

    def __init__(self):
        self.created_by = 'DANIEL MARINHO FERREIRA DE SOUZA,EMANUEL SIQUEIRA LANNES' 
        self.created_by2 = 'ERICK ANTONIO PIMENTEL MERCADO, GABRIEL VASCONCELOS SANTOS e VITOR DORNELA MASCARENHAS'
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"
        self.mongo = MongoQueries()

    def get_documents_count(self, collection_name):
        # Retorna o total de registros computado pela query
        df = self.mongo.query_count(collection_name=collection_name)
        return df[f"total_{collection_name}"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - : Administradores : {str(self.get_documents_count(collection_name="Administradores")).rjust(5)}
        #      2 - : Cotacoes : {str(self.get_documents_count("Cotacoes")).rjust(5)}
        #      3 - : Dividendos : {str(self.get_documents_count("Dividendos")).rjust(5)}
        #      4 - : Fundos : {str(self.get_documents_count("Fundos")).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #               {self.created_by2}
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """