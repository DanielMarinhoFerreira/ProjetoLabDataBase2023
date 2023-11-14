############################################################
#Programa model.Administradores
#AUTOR.......: Daniel Marinho 
#DATA........: 24/09/2023
#DESCRICAO...: class Administradores  
############################################################


class Administradores:
    
    def __init__(self, nome:str='', telefone:str='', email:str='', url_site:str='', cnpj_admin:str=''):
        self.nome = nome 
        self.telefone = telefone
        self.email = email
        self.url_site = url_site
        self.cnpj_admin = cnpj_admin
    
    def get_nome(self):
        return self.nome
    
    def get_telefone(self):
        return self.telefone
    
    def get_email(self):
        return self.email
        
    def get_url_site(self):
        return self.url_site
    
    def get_cnpj_admin(self):
        return self.cnpj_admin
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_telefone(self,telefone):
        self.telefone = telefone
    
    def set_email(self,  email):
        self.email = email
        
    def set_site(self, url_site):
        self.url_site = url_site 
    
    def set_cnpj(self, cnpj_admin):
        self.cnpj_admin = cnpj_admin            
            