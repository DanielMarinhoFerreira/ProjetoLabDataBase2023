 # WKSP - Banco de Dados Oracle

## Descrição

O WKSP - Banco de Dados Oracle é um projeto desenvolvido para demonstrar o uso do banco de dados Oracle. O projeto foi desenvolvido utilizando a linguagem de programação Python e a biblioteca cx_Oracle.

## Pré-requisitos

Para executar o projeto, você precisará ter o Oracle Database instalado e configurado em sua máquina. Você também precisará ter o Python 3 instalado e a biblioteca cx_Oracle instalada.

## Instalação

Para instalar o projeto, clone o repositório para sua máquina local e execute o seguinte comando:

```
pip install -r requirements.txt
```

## Configuração

Para configurar o projeto, você precisará criar um arquivo de configuração chamado `config.ini`. O arquivo de configuração deve conter as seguintes informações:

```
[oracle]
host = localhost
port = 1521
service_name = XEPDB1
user = labdatabase
password = labDatabase2022
```

## Uso

Para usar o projeto, execute o seguinte comando:

```
python main.py
```

O projeto irá exibir um menu principal com as seguintes opções:

* Relatórios
* Inserir Registros
* Atualizar Registros
* Remover Registros
* Sair

## Relatórios

A opção Relatórios permite que você gere relatórios sobre os dados do banco de dados. Os relatórios disponíveis são:

* Relatório de Fundos
* Relatório de Empreendimentos
* Relatório de Cotações Gerais
* Relatório de Cotações Por Fundos
* Relatório de Endereços
* Relatório de Endereços por Segmentos

## Inserir Registros

A opção Inserir Registros permite que você insira novos registros no banco de dados. Os registros que podem ser inseridos são:

* Fundos
* Empreendimentos
* Cotações
* Endereços

## Atualizar Registros

A opção Atualizar Registros permite que você atualize os registros existentes no banco de dados. Os registros que podem ser atualizados são:

* Fundos
* Empreendimentos
* Cotações
* Endereços

## Remover Registros

A opção Remover Registros permite que você remova os registros existentes no banco de dados. Os registros que podem ser removidos são:

* Fundos
* Empreendimentos