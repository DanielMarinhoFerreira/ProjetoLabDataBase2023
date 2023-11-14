from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_admin import Controller_Admin
from controller.controller_cotacoes import Controller_Cotacoes
from controller.controller_dividendos import Controller_Dividendos
from controller.controller_fundos import Controller_Fundos
from time import sleep
from utils import config


tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_admin = Controller_Admin()
ctrl_contacoes = Controller_Cotacoes()
ctrl_dividendos = Controller_Dividendos()
ctrl_fundos = Controller_Fundos()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio('Relatorio_fundos.sql')       
        sleep(5)     
    elif opcao_relatorio == 2:
        relatorio.get_relatorio('Relatorio_fundos_adm.sql')
        sleep(5)
    elif opcao_relatorio == 3:
        relatorio.get_relatorio('Relatorio_Cotacoes_por_fundos.sql')
        sleep(5)
    elif opcao_relatorio == 4:
        relatorio.get_relatorio('Relatorio_de_Segmentos.sql')
        sleep(5)
    elif opcao_relatorio == 5:
        relatorio.get_relatorio('Rolatorio_dividendos.sql')
        sleep(5)
        
def inserir(opcao_inserir:int=0):
    
    if opcao_inserir == 1:
        ctrl_fundos.inserir_fundos()
        sleep(5)
    elif opcao_inserir == 2:
        ctrl_admin.inserir_admin()
        sleep(5)
    elif opcao_inserir == 3:
        ctrl_contacoes.inserir_cotacoes()
        sleep(5)
    elif opcao_inserir == 4:
        ctrl_dividendos.inserir_Dividendos()
        sleep(5)

def atualizar(opcao_atualizar:int=0):
    
    if opcao_atualizar == 1:
        ctrl_fundos.atualizar_fundos()
        sleep(5)
    elif opcao_atualizar == 2:
        ctrl_admin.atualizar_admin()
        sleep(5)
    elif opcao_atualizar == 3:
        ctrl_contacoes.atualizar_cotacoes()
        sleep(5)
    elif opcao_atualizar == 4:
        ctrl_dividendos.atualizar_Dividendos()
        sleep(5)


def excluir(opcao_excluir:int=0):
    
    if opcao_excluir == 1:
        ctrl_fundos.excluir_fundos()
        sleep(5)
    elif opcao_excluir == 2:
        ctrl_admin.deletar_admin()
        sleep(5)
    elif opcao_excluir == 3:
        ctrl_contacoes.deletar_cotacoes()
        sleep(5)
    elif opcao_excluir == 4:
        ctrl_dividendos.deletar_Dividendos()
        sleep(5)


def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-6]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()