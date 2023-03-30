# Sandbox Starkbank
Integração Sandbox para gerenciamento de fatura


## Documentação da API

```http
  GET /docs
```

```http
  GET /redoc
```


## Pré requisito

- [Pyenv](https://realpython.com/intro-to-pyenv/#installing-pyenv)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

- Instalar pacotes essenciais (Ubuntu/Debian)
  ```bash
    sudo apt-get update && apt-get install -y make curl build-essential
  ```


## Rodando em ambiente de desenvolvimento

Clone o projeto

```bash
  git clone https://github.com/anaplopes/sandbox-starkbank.git
```

Entre no diretório do projeto

```bash
  cd sandbox-starkbank
```

Preparando o ambiente

```bash
  make prepare
```

Instale as dependências

```bash
  make install
```

Gerar chaves pública e privada

```bash
  make keys
```

Criar um projeto no [Sandbox](https://web.sandbox.starkbank.com/)
    - Acesse Menu > Integrações
    - Clique no botão "Novo Projeto"
    - Insira o nome do seu projeto e carregue a chave pública que você criou `file/keys/`

Adicione as variaveis de ambiente no arquivo `.env.dev`
  - DB_URI: "postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"
  - SB_PROJECT_ID: identificação do projeto no sandbox Starkbank
  - PRIVATE_KEY: chave privada para credencial

Inicie os containers db, redis, dashboard

```bash
  make up-infra
```

Inicie a api

```bash
  make run-server
```

Inicie o worker

```bash
  make run-worker
```

Para rodar os testes, rode o seguinte comando

```bash
  make test
```


## Rodando no docker

Adicione as variaveis de ambiente no arquivo `.env`

  - Obrigatório
    - DB_URI: "postgresql://{DB_USER}:{DB_PASSWORD}@db:5432/{DB_NAME}"
    - SB_PROJECT_ID: identificação do projeto no sandbox Starkbank
    - PRIVATE_KEY: chave privada para credencial

  - Opcional (***Essa mudança afetará a configuração DB_URI nos arquivos `.env*`)
    - DB_USER: usuario do banco de dados
    - DB_PASSWORD: senha do banco de dados
    - DB_NAME: nome do banco de dados
    - CELERY_BROKER_URL: 
    - CELERY_RESULT_BACKEND: 

Inicie todos os containers

```bash
  make up
```

Parar os containers

```bash
  make down
```

Limpar o docker

```bash
  make clean
```
