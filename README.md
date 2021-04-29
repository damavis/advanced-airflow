# Advanced Airflow

A collection of Apache Airflow DAGs to illustrate advanced use cases
and strategies. It's also a sample development environment, allowing
devs to develop and test their DAGs implementation on their local
environments easily.

## Requirements

The [docker-compose.yaml](docker-compose.yaml) file is extracted
directly from Airflow documentation. Before you begin, follow this
steps to install the necessary tools:

* [Install Docker](https://docs.docker.com/engine/install/)
* [Install Compose](https://docs.docker.com/compose/install/)

## Start/Stop Airflow

To start and stop Airflow platform, please, use the following scripts,
their will ensure to run it using your current user to avoid permission
changes.

```bash
./airflow-start.sh
./airflow-stop.sh
```

## Contributing

If you want to contribute, you will need to install some dependencies
and set up your environment before.

```bash
pip install -r requirements-dev.txt
pre-commit install
```

Please, make sure that your commit is passing all `pre-commit`
checks  before opening any PR.

```bash
pre-commit run --all-files
```
