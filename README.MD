# Projeto ETL com Apache Airflow

Este projeto consiste em uma pipeline de ETL (Extract, Transform, Load) implementada usando Apache Airflow para automatizar o fluxo de dados entre fontes de dados, transformações e destino final.

## Visão Geral

A pipeline ETL é projetada para extrair dados de várias fontes, aplicar transformações definidas e carregar os dados resultantes em um destino específico. O Apache Airflow é utilizado para agendar e orquestrar o fluxo de trabalho da pipeline, permitindo uma execução confiável e escalável.

## Funcionalidades Principais

- Orquestração de tarefas ETL usando Apache Airflow.
- Suporte para múltiplas fontes e destinos de dados.
- Monitoramento e agendamento de fluxos de trabalho.

## Requisitos

- Python 3.10
- Apache Airflow
- Dependências adicionais conforme definido nos DAGs (Directed Acyclic Graphs) específicos.
- PostgreSQL

## Instalação

1. Instale o Apache Airflow conforme as instruções oficiais: [link](https://airflow.apache.org/docs/apache-airflow/stable/start/index.html)
2. Clone este repositório: 
    ```
    git clone https://github.com/seu-usuario/projeto-etl-airflow.git
    ```
3. Instale as dependências necessárias:
    ```
    pip install -r requirements.txt
4. Copie a pasta dags para dentro da sua pasta do airflow

## Uso

1. Inicie o servidor do Airflow:
    ```
    airflow webserver -p 8080
    airflow scheduler
    ```
2. Acesse a interface do Airflow em `http://localhost:8080`.
3. Na aba Admin, entre em Connections e crie uma conexão com id 'psql' para seu banco de dados postgreSQL
4. Ative os DAGs relevantes na interface do Airflow.
5. Os fluxos de trabalho ETL serão executados automaticamente conforme agendado.

## Contribuição

- Se deseja contribuir com o projeto, por favor, abra uma issue ou envie um pull request seguindo as diretrizes de contribuição.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

## Autores

- [Renato Avellar](https://github.com/renato-avellar)

