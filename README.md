# Banco de Dados MongoDB

## Descrição

O projeto foi desenvolvido para demonstrar a utilização de um banco de dados MongoDB, utilizando a linguagem de programação Python e a biblioteca pymongo.

## Video de apresentação do código

https://www.youtube.com/watch?v=GIT5S-AXp24

## Video de demonstração da aplicação
https://youtu.be/omtGcWLug7A

## Pré-requisitos

Para executar o projeto, você precisará instalado e configurado em sua máquina. Você também precisará ter o Python 3 instalado e a biblioteca pymongo instalada.

## Instalação

Para instalar o projeto, clone o repositório para sua máquina local e execute o seguinte comando:

```
pip install -r requirements.txt
```

## Configuração

Para configurar o projeto, você precisará criar um arquivo de configuração chamado `config.ini`. O arquivo de configuração deve conter as seguintes informações:

```
[mongodb]
host = localhost
port = 27017
service_name = labdatabase
user = labdatabase
password = labDatabase2022
```

## Uso

Para usar o projeto, execute o seguinte comando:

```
python run.py
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
