############################################################
#Programa model.Fundos
#AUTOR.......: Daniel Marinho 
#DATA........: 18/10/2022 as 24/09/2023
#DESCRICAO...: class Fundo  
############################################################

class Fundos:
    
    
    def __init__(self, ticker:str, tipo_abbima:str, segmento:str,num_cotas:int ,conta_emit:int, razao_social:str, cnpj, nome_pregao:str, prazo_doracao:str, tipo_gestao:str, cnpj_admin) -> None:
        self.ticker = ticker        
        self.tipo_abbima = tipo_abbima
        self.segmento = segmento
        self.conta_emit = conta_emit
        self.num_cota = num_cotas
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.nome_pregao = nome_pregao
        self.prazo_doracao = prazo_doracao
        self.tipo_gestao = tipo_gestao
        self.cnpj_admin = cnpj_admin
    
    def __delattr__(self) -> None:
        pass
    
    def get_Ticker(self):
        return self.ticker

    def get_tipo_abbima(self):
        return self.tipo_abbima
    
    def get_segmento(self):
        return self.segmento
    
    def get_num_cota(self):
        return self.num_cota
    
    def get_conta_emit(self):
        return self.conta_emit
    
    def get_razao_social(self):
        return self.razao_social
    
    def get_cnpj(self):
        return self.cnpj
    
    def get_nome_pregao(self):
        return self.nome_pregao

    def get_prazo_doracao(self):
        return self.prazo_doracao
    
    def get_tipo_gestao(self):
        return self.tipo_gestao
    
    def get_cnpj_admin(self):
        return self.cnpj_admin
    
    def set_cnpl_admin(self, cnpj):
        self.cnpj_admin = cnpj

    