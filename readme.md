# MusicKamp
#### MusicKamp é um projeto CRUD em Django Rest Framework que permite aos usuários catalogarem seus álbuns favoritos com base nos gêneros musicais.


## Tecnologias Utilizadas
### As principais tecnologias utilizadas neste projeto são:
- Django 4.0.7
- Django Rest Framework 3.14.0
- Django Rest Framework SimpleJWT 5.2.2
- DRF Spectacular 0.25.1
- PostgreSQL (Banco de Dados)
- Python 3.x


## Endpoints da API
- Listar, criar e editar álbuns: http://localhost:8000/albums/
- Detalhes de um álbum específico: http://localhost:8000/albums/idAlbum/
- Listar, criar e editar músicas de um álbum: http://localhost:8000/albums/idAlbum/songs/
- Listar, criar e editar usuários: http://localhost:8000/users/
- Detalhes de um usuário específico: http://localhost:8000/users/idUser/
- Login de usuário e obtenção de token JWT: http://localhost:8000/users/login/
- Documentação da API: http://localhost:8000/api/docs/


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
##### Ative o Ambiente Virtual no Windows:
```
source venv/Scripts/activate
```
##### Ative o Ambiente Virtual no macOS ou Linux:
```
source venv/bin/activate
```


#### 4. Instale as dependências do projeto usando o gerenciador de pacotes pip:
```
pip install -r requirements.txt
```


#### 5. Configure o banco de dados criando arquivo .env com base no arquivo .env.example:


#### 6. Execute as migrações para criar as tabelas do banco de dados:
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