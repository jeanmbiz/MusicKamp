# MusicKamp
#### MusicKamp é um projeto CRUD em Django Rest Framework que permite aos usuários catalogarem seus álbuns de músicas favoritos.


## Tecnologias Utilizadas
### As principais tecnologias utilizadas neste projeto são:
- Django 4.0.7
- Django Rest Framework 3.14.0
- Django Rest Framework SimpleJWT 5.2.2
- DRF Spectacular 0.25.1
- PostgreSQL (Banco de Dados)
- Python 3.x

## Diagrama do Projeto
![diagrama](/diagrama.jpg)

## Instalação
### Para executar o projeto localmente, siga as etapas abaixo:


#### 1. Clone o repositório do MusicKamp:
```
git clone git@github.com:jeanmbiz/MusicKamp.git
```


#### 2. Acesse o diretório do projeto: 


#### 3. Crie um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
```
#### 3.1. Ative o Ambiente Virtual no Windows:
```
source venv/Scripts/activate
```
#### 3.2. Ative o Ambiente Virtual no macOS ou Linux:
```
source venv/bin/activate
```


#### 4. Instale as dependências do projeto utilizando o gerenciador de pacotes pip:
```
pip install -r requirements.txt
```


#### 5. Configure o banco de dados criando arquivo .env com base no arquivo .env.example:


#### 6. Execute as migrações para criar as tabelas no banco de dados:
```
python manage.py migrate
```


#### 7. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```


#### 8. Acesse o servidor local em seu navegador:
```
http://localhost:8000/
```

## Endpoints da API
- Usuários:
  - Criar Usuário: http://localhost:8000/api/users/
  - Buscar, Editar, Deletar Usuário por ID: http://localhost:8000/api/users/<id>/

- Login: http://localhost:8000/api/users/login/

- Albums: 
  - Criar Album: http://localhost:8000/api/albums/
  - Buscar Album: http://localhost:8000/api/albums/idAlbum/songs/

- Músicas: 
  - Criar Músicas: http://localhost:8000/api/albums/idAlbum/songs/
