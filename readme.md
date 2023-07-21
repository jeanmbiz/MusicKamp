# MusicKamp
#### Descrição: MusicKamp é um projeto CRUD em Django Rest Framework que permite aos usuários catalogarem seus álbuns favoritos com base nos gêneros musicais.

## Instalação
### Para executar o projeto localmente, siga as etapas abaixo:

#### 1. Clone o repositório do MusicKamp:
```
git clone git@github.com:jeanmbiz/MusicKamp.git
```

#### 2. Acesse o diretório do projeto: 

##### Crie e ative um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
```

##### No Windows:
```
venv\Scripts\activate
```

##### No macOS ou Linux:
```
source venv/bin/activate
```

#### 3. Instale as dependências do projeto usando o gerenciador de pacotes pip:
```
pip install -r requirements.txt
```
Copy code

#### 4. Configuração do banco de dados conforme arquivo .env.example:

#### 5. Execute as migrações para criar as tabelas do banco de dados:
```
python manage.py migrate
```

#### 6. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```

#### 7. Acesse o servidor local em seu navegador:
```
http://localhost:8000/
```

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
