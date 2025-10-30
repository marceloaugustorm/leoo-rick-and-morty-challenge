# Rick and Morty API - CSV Export

Este projeto é um script em Python que consome a [API de Rick and Morty] para coletar informações sobre personagens e salvar em um arquivo CSV. O objetivo é praticar requisições HTTP, manipulação de JSON, e exportação de dados para CSV.

## Funcionalidades
- Faz requisições à API de Rick and Morty.
- Coleta informações de 50 personagens (ou mais, ajustável).
- Salva os dados em um arquivo CSV com o delimitador `;`.
- Inclui os campos: `id`, `name`, `status`, `species`, `type`, `gender`.

## Tecnologias
- Python 3.x
- Módulo `requests` para requisições HTTP
- Módulo `csv` para exportação de dados

## Como usar
1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/leoo-rick-and-morty-challenge.git
```
2. Instale as dependências (se necessário):
```bash
pip install requests
```
3. Execute o script:
```bash
python api.py
```
4. O CSV será gerado no mesmo diretório com o nome `personagens.csv`.

## Estrutura do CSV
| id | name | status | species | type | gender |
|----|------|--------|---------|------|--------|
| 1  | Rick Sanchez | Alive | Human |  | Male |
| 2  | Morty Smith  | Alive | Human |  | Male |

  

