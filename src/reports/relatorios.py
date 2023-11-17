from connection.mongo_queries import MongoQueries
import pandas as pd
#
# Implementar 
# Base montada 
# #
class Relatorio:
    
    def __init__(self):
        pass
    

    def get_Cotacoes_por_fundos(self):
        # Relatorio cotações por funtos 
        mongo = MongoQueries()

        db = mongo.connect()

        query_result = db["FUNDOS"].find({},{
                                            "TICKER": 1,
                                            "TIPO_ABBIMA": 1,
                                            "SEGMENTO": 1,
                                            "CONTA_EMIT": 1,
                                            "NUM_COTAS": 1,
                                            "RAZAO_SOCIAL": 1,
                                            "CNPJ": 1,
                                            "NOME_PREGAO": 1,
                                            "PRAZO_DURACAO": 1,
                                            "TIPO_GESTAO": 1,
                                            "CNPJ_ADMIN": 1,
                                            "_id": 0
                                        })
        cot_fundos = pd.DataFrame(list(query_result))
        mongo.close()
        print(cot_fundos,end='\n')
        input("Precione Enter para sair do Relatorio")


    def get_segmentos(self):
        # Relatorio cotações por funtos 
        mongo = MongoQueries()

        db = mongo.connect()

        query_result = db["FUNDOS"].find({},{
                                        "SEGMENTO": 1,
                                        "_id": 0
                                        })
        
        df_segmentos = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_segmentos)
        print('')
        input("Precione Enter para sair do Relatorio")

    def get_fundos_admin(self):
        mongo = MongoQueries()

        db = mongo.connect()

        query_result = db["FUNDOS"].aggregate([{
                                "$lookup": {"from": "ADMINISTRADORES",
                                            "localField": "CNPJ_ADMIN",
                                            "foreignField": "CNPJ_ADMIN",
                                            "as": "administrador"
                                            }
                                            },
                                            {
                                                "$unwind": "$administrador"
                                            },
                                            {
                                            "$match": {"TICKER": { "$ne": "null" }}
                                            },
                                            {
                                            "$sort": {"TICKER": 1}
                                            },
                                            {"$project": {
                                            "_id": "0",
                                            "TICKER": "$TICKER",
                                            "TIPO_ABBIMA": "$TIPO_ABBIMA",
                                            "SEGMENTO": "$SEGMENTO",
                                            "CNPJ_ADMIN": "$administrador.CNPJ_ADMIN",
                                            "NOME_ADMIN": "$administrador.NOME"
                                                        }
                                            }])
        df_fundos_admin = pd.DataFrame(list(query_result))

        mongo.close()
        print(df_fundos_admin)
        print('')
        input("Precione Enter para sair do Relatorio")

    def get_fundos(self):
        # Relatorio funtos 
        mongo = MongoQueries()

        db = mongo.connect()

        query_result = db["FUNDOS"].find({},{
                                        "Ticker": 1,
                                        "_id": 0
                                        })
        
        df_fundos = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_fundos)
        print('')
        input("Precione Enter para sair do Relatorio")

    def get_dividendos(self):
        mongo = MongoQueries()

        db = mongo.connect()
        """
        query_result = db["DIVIDENDOS"].aggregate([{
                                                        "$match": {
                                                        "TICKER": { "$ne: null" }
                                                        }
                                                    },
                                                    {
                                                        "$lookup": {
                                                        "from": "COTACOES",
                                                        "localField": "TICKER",
                                                        "foreignField": "TICKER",
                                                        "as": "cotacoes"
                                                        }
                                                        },
                                                        {
                                                            "$unwind": "$cotacoes"
                                                        },
                                                        {
                                                            "$match:" {
                                                                "cotacoes.P_VP": { "$ne": "null" }
                                                                }
                                                        },
                                                        {   "$group": {
                                                            "_id": {
                                                                "TICKER": "$TICKER",
                                                                "P_VP": "$cotacoes.P_VP"
                                                            },
                                                            "rendimento_total": { "$sum": "$RENDIMENTO" }
                                                            }
                                                            },
                                                            {   "$project": {
                                                                "_id": 0,
                                                                "TICKER": "$_id.TICKER",
                                                                "P_VP": "$_id.P_VP",
                                                                "rendimento_total": 1
                                                                }
                                                            }
                                                    ])
        df_dividendos = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_dividendos)
        print('')
        input("Precione Enter para sair do Relatorio")
        """