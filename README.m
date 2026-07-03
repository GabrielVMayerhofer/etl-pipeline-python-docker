# ETL Pipeline: Processamento de Dados com Python, Pandas e Docker

Um projeto prático de Engenharia de Dados focado em construir um pipeline ETL (Extract, Transform, Load) completo e modularizado. O sistema extrai dados de diferentes fontes em formato JSON, aplica regras de negócio e limpeza de dados via Pandas, e carrega os dados processados em um banco PostgreSQL conteinerizado com Docker.

## Sobre o Projeto

Este projeto demonstra como estruturar fluxos de dados de forma modular. O pipeline consome dados brutos (como personagens da API do Rick and Morty, Posts e Clima), salva em uma camada intermediária (CSV) e carrega o resultado final de forma idempotente em um banco de dados relacional.

### Arquitetura do ETL

A lógica do pipeline foi dividida em três scripts distintos para garantir o princípio de responsabilidade única:
*   **[E] Extract (`extract.py`):** Responsável por coletar os dados originais e salvá-los na camada `data/raw/` em formato `.json`.
*   **[T] Transform (`transform.py`):** Consome os dados brutos, aplica limpeza (desaninhamento de colunas, tratamento de nulos, formatação de datas) com `pandas` e salva o resultado intermediário na camada `data/processed/` em formato `.csv`.
*   **[L] Load (`load.py`):** Lê os arquivos processados, estabelece conexão com o banco **PostgreSQL** rodando via **Docker Compose** e realiza a ingestão dos dados utilizando `sqlalchemy`.

## Tecnologias Utilizadas

*   **Python 3** - Linguagem principal
*   **Pandas** - Manipulação e transformação dos dados
*   **SQLAlchemy / Psycopg2** - ORM e driver de conexão com o banco de dados
*   **PostgreSQL** - Banco de dados relacional
*   **Docker & Docker Compose** - Orquestração e conteinerização da infraestrutura de dados

## Estrutura do Projeto

Abaixo está a organização dos arquivos e pastas do repositório:

```text
├── data/
│   ├── processed/           # Camada de dados limpos e intermediários
│   │   ├── processed_posts.csv
│   │   └── processed_rnm.csv
│   └── raw/                 # Camada de dados originais (JSON)
│       ├── raw_clima.json
│       ├── raw_posts.json
│       └── raw_rnm.json
├── scripts/                 # Scripts do Pipeline ETL
│   ├── extract.py           # Lógica de extração
│   ├── transform.py         # Regras de limpeza e transformação (Pandas)
│   └── load.py              # Lógica de carga no PostgreSQL
├── docker-compose.yml       # Configuração da infra do PostgreSQL via Docker
├── README.md                # Documentação do projeto
└── .gitignore               # Ignora caches e arquivos indesejados
```
## How to Run

### 1. Pré-requisitos
Certifique-se de ter instalado em sua máquina:
* **Python 3**
* **Docker** e **Docker Compose**
* **Git**

### 2. Clonando o Repositório
Abra o terminal e clone o projeto para a sua máquina local:
```bash
git clone https://github.com/GabrielVMayerhofer/etl-pipeline-python-docker.git
cd etl-pipeline-python-docker
```
### 3. Configurando o Ambiente Virtual
Crie e ative um ambiente virtual para instalar as dependências do projeto:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 4. Instalando Dependências
Instale as bibliotecas necessárias utilizando o `pip`:
```bash
pip install pandas sqlalchemy psycopg2-binary
```
### 5. Iniciando o Banco de Dados com Docker
Certifique-se de que o Docker está em execução e inicie o serviço do PostgreSQL:
```bash
docker compose up -d
```
### 6. Executando o Pipeline ETL
Agora você pode executar os scripts do pipeline na ordem correta:
1. Extract:
```bash
python scripts/extract.py
```
2. Transform:
```bash
python scripts/transform.py
```
3. Load:
```bash
python scripts/load.py
```