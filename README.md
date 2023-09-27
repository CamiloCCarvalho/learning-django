# LEARNING DJANGO
learning-django


## CRIANDO PROJETO
Na pasta do projeto pelo terminal:
    > django-admin startproject nome_projeto

## CONFIGURANDO PROJETO
No arquivo settings.py no diretório principal do projeto, escolher LANGUAGE_CODE adequado, assim como TOME_ZONE no Brasil por exemplo:
    > LANGUAGE_CODE: 'pt-br' e TIME_ZONE: 'America/Sao_Paulo'


## ATIVAR O AMBIENTE DO DJANGO (VENV)
No terminal ja na pasta do projeto:
    > workon django

## CRIANDO AS TABELAS BASICAS COM FUNÇÃO ADMIN DO DJANGO
Cria tabelas basicas, função admin, ja com banco de dados, usando o set do arquivo settings:
    > python manage.py migrate

## STARTAR SERVER LOCAL PARA DESENVOLVIMENTO
    > python manage.py runserver

## CRIANDO SUPERUSUARIO PARA USAR COMO ADMIN 
    > python manage.py createsuperuser

Ai precisa configurar Nome de Usuario, Email (pode ser em branco), Senha, confirmar Senha. Confirmar processo. No painel é possivel gerenciar grupos e usuarios.

## MODULAR

Django é modular, o projeto basico começa apenas com as configurações padrão, e a partir disso você cria modulos para gerenciar, cadastros, usuarios, templates, podendo organizar da melhor forma.

    > python manage.py startpp nome_do_app_ou_modulo

## ARQUITETURA MVT
Django trablaha com arquitetura MVT (Model, View, Template):
    - Requisição vai para as URLs do projeto
    - Então acessa os APPs(Modulos) para conferir grupos de URLs
    - Retorna para Views  se comunica com os Templates e com os Models
    - os Models por sua vez se comunica com o DB
    - após a View estar "montada" devolve a resposta a requisição

## COM AS MODELS FEITAS
Para o Django conferir se no DB já tem as tabelas criadas a partir das models:
 > python manage.py makemigrations

Com isso é criado o script das migrations para poder criar no banco, porem ainda não foi criado
para criar:
 > python manage.py migrate

Neste ponto o DB cria as tabelas e é possivel conferir.


