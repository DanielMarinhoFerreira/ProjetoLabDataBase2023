from datetime import time
from model.fundos import Fundos

############################################################
#Programa model.Cotacoes
#AUTOR.......: Daniel Marinho 
#DATA........: 18/10/2022 24/09/2023
#DESCRICAO...: class Cotacao  
############################################################

class Cotacoes():


    def __init__(self, ticker:str='', data_cota:str='', cota_atual:str='', rendimento_atual:str='', minimo_cota:str='', maximo_cota:str='' ,abertura:str='', volumes_cotas:str='', mes:str='',p_vp:int='') -> None:
        self.ticker = ticker
        self.data_conta = data_cota
        self.cota_atual = cota_atual
        self.rendimento_atual = rendimento_atual
        self.minimo_cota = minimo_cota
        self.maximo_cota = maximo_cota
        self.arbetura = abertura
        self.volume_cotas = volumes_cotas
        self.mes = mes
        self.p_vp = p_vp

    def get_ticker(self):
        return self.ticker

    def get_data_cota(self):
        return self.data_conta

    def get_cota_atual(self):
        return self.cota_atual

    def get_rendimento_atual(self):
        return self.rendimento_atual
    
    def get_minimo(self):
        return self.minimo_cota

    def get_maximo(self):
        return self.maximo_cota
    
    def get_abertura(self):
        return self.arbetura
    
    def get_volume_cotas(self):
        return self.volume_cotas

    def get_mes(self):
        return self.mes

    def get_p_vp(self):
        return self.p_vp
    
    def set_ticker(self, ticker):
        self.ticker = ticker

    def set_data_cota(self, data_atual):
        self.data_conta = data_atual

    def set_cota_atual(self, cota_atual):
         self.cota_atual = cota_atual

    def set_rendimento_atual(self, rendimento):
        self.rendimento_atual = rendimento
    
    def set_minimo(self, minimo_cota):
        self.minimo_cota = minimo_cota

    def set_maximo(self, maximo_cota):
        self.maximo_cota = maximo_cota
    
    def set_abertura(self, abertura):
        self.arbetura = abertura
    
    def set_volume_cotas(self, volume_cotas):
        self.volume_cotas = volume_cotas

    def set_mes(self, mes):
        self.mes = mes
    
    def set_p_vp(self, p_vp):
        self.p_vp = p_vp