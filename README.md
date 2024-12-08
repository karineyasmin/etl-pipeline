# ETL Pipeline

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para coletar, transformar e carregar dados de artistas de uma página web para um banco de dados MySQL.

## Estrutura do Projeto

- `src/`
  - `main/`
    - `main_pipeline.py`: Contém a lógica principal do pipeline.
  - `stages/`
    - `extract/`
      - `extract_data.py`: Contém a lógica para extrair dados da web.
    - `transform/`
      - `transform_data.py`: Contém a lógica para transformar os dados extraídos.
    - `load/`
      - `load_data.py`: Contém a lógica para carregar os dados transformados no banco de dados.
  - `infra/`
    - `database_connector.py`: Contém a lógica para conectar ao banco de dados MySQL.
    - `database_repository.py`: Contém a lógica para interagir com o banco de dados.
  - `drivers/`
    - `http_requester.py`: Contém a lógica para fazer requisições HTTP.
    - `html_collector.py`: Contém a lógica para coletar informações essenciais do HTML.
  - `mocks/`
    - `http_requester_mock.py`: Contém mocks para testes.
    - `transform_contract_mock.py`: Contém mocks para testes.
  - `errors/`
    - `load_error.py`: Contém a definição de erros personalizados.

## Requisitos

- Python 3
- MySQL
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`
  - `mysql-connector-python`
  - `pytest`
  - `requests-mock`
  - `python-dotenv`

## Instalação

1. Clone o repositório:

```sh
git clone https://github.com/seu-usuario/etl_pipeline.git
cd etl_pipeline
```
2. Crie e ative um ambiente virtual 
```sh
python -m venv venv
source venv/bin/activate
```
3. Instale as dependências
```sh
pip install -r requirements.txt
```

4. Configure as varáveis de ambiente:

   Crie um arquivo ```.env``` na raiz do projeto e adicione as seguintes variáveis

```sh
DB_HOST=localhost
DB_PORT=3306
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```
____
### Uso 
Para executar o pipleine, execute o s eguinte comando:
```sh
python run.py
```
____

### Testes
Para executar os teste, use o seguinte comando:
```sh
pytest -s -v
```

____

### Estrutura do Banco de Dados

```sql
CREATE DATABASE pipeline_db;

USE pipeline_db;

CREATE TABLE artists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    nickname VARCHAR(255),
    artist_id VARCHAR(255),
    link TEXT,
    extraction_date DATE
);
```
___