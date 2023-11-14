############################################################
#Programa model.dividendos
#AUTOR.......: Daniel Marinho 
#DATA........:  24/09/2023
#DESCRICAO...: class dividendos  
############################################################


class Dividendos:
    
    
    def __init__(self, ticker:str='', data_pag:str='', cota_base:str='', ult_divid:str='', rendimento:str='', div_yield:str=''):
        self.ticker = ticker
        self.data_pag = data_pag
        self.cota_base = cota_base
        self.ult_divid = ult_divid
        self.rendimento = rendimento
        self.div_yield = div_yield
      
    def get_ticker(self):
        return self.ticker

    def get_data_pag(self):
        return self.data_pag

    def get_cota_base(self):
        return self.cota_base

    def get_ult_divid(self):
        return self.ult_divid

    def get_rendimento(self):
        return self.rendimento

    def get_div_yield(self):
        return self.div_yield   

    def set_ticker(self, ticker):
        self.ticker = ticker

    def set_data_pag(self, data_pag):
        self.data_pag = data_pag

    def set_cota_base(self, cota_base):
        self.cota_base = cota_base

    def set_ult_divid(self, ult_divid):
        self.ult_divid = ult_divid

    def set_rendimento(self, rendimento):
        self.rendimento = rendimento

    def set_div_yield(self, div_yield):
        self.div_yield = div_yield
        