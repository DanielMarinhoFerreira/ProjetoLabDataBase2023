from connection.mongo_queries import MongoQueries
import pandas as pd

class Relatorio:
    
    def __init__(self):
        pass
    

    def get_Cotacoes_por_fundos(self):
        # Relatorio cotações por funtos 
        mongo = MongoQueries()

        db = mongo.connect()

        query_result = db["FUNDOS"].find({},{
                                            "ticker": 1,
                                            "tipo_abbima": 1,
                                            "segmento": 1,
                                            "conta_emit": 1,
                                            "num_cotas": 1,
                                            "razao_social": 1,
                                            "cnpj": 1,
                                            "nome_pregao": 1,
                                            "prazo_duracao": 1,
                                            "tipo_gestao": 1,
                                            "cnpj_admin": 1,
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
                                        "segmento": 1,
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
                                            "localField": "cnpj_admin",
                                            "foreignField": "cnpj_admin",
                                            "as": "administrador"
                                            }
                                            },
                                            {
                                                "$unwind": "$administrador"
                                            },
                                            {
                                            "$match": {"ticker": { "$ne": "null" }}
                                            },
                                            {
                                            "$sort": {"ticker": 1}
                                            },
                                            {"$project": {
                                            "_id": "0",
                                            "ticker": "$ticker",
                                            "tipo_abbima": "$tipo_abbima",
                                            "segmento": "$segmento",
                                            "cnpj_admin": "$administrador.cnpj_admin",
                                            "nome_admin": "$administrador.nome"
                                                        }
                                            }])
        df_fundos_admin = pd.DataFrame(list(query_result))

        mongo.close()
        print(df_fundos_admin)
        print('')
        input("precione enter para sair do relatorio")

    def get_fundos(self):
        # relatorio funtos 
        mongo = MongoQueries()
        db = mongo.connect()

        query_result = db["FUNDOS"].find({},{
                                        "ticker": 1,
                                        "_id": 0
                                        })
        
        df_fundos = pd.DataFrame(list(query_result))
        mongo.close()
        print(df_fundos)
        print('')
        input("precione enter para sair do relatorio")

    def get_dividendos(self):
        mongo = MongoQueries()

        db = mongo.connect()
        """
        query_result = db["dividendos"].aggregate([{
                                                        "$match": {
                                                        "ticker": { "$ne: null" }
                                                        }
                                                    },
                                                    {
                                                        "$lookup": {
                                                        "from": "cotacoes",
                                                        "localfield": "ticker",
                                                        "foreignfield": "ticker",
                                                        "as": "cotacoes"
                                                        }
                                                        },
                                                        {
                                                            "$unwind": "$cotacoes"
                                                        },
                                                        {
                                                            "$match:" {
                                                                "cotacoes.p_vp": { "$ne": "null" }
                                                                }
                                                        },
                                                        {   "$group": {
                                                            "_id": {
                                                                "ticker": "$ticker",
                                                                "p_vp": "$cotacoes.p_vp"
                                                            },
                                                            "rendimento_total": { "$sum": "$rendimento" }
                                                            }
                                                            },
                                                            {   "$project": {
                                                                "_id": 0,
                                                                "ticker": "$_id.ticker",
                                                                "p_vp": "$_id.p_vp",
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