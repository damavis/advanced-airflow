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

## Customizing your image

If you need to install extra software on your image, please, use the
[Dockerfile](Dockerfile) to extend the official image. Also, you can
add your requirements in [requirements.txt](requirements.txt).

## Start/Stop Airflow

To start and stop Airflow platform, please, use the following scripts,
their will ensure to run it using your current user to avoid permission
changes. It will also build your Airflow image.

```bash
./airflow-start.sh
./airflow-stop.sh
```

## Access Airflow UI

In order to access Airflow Webserver, follow this link:
[http://localhost:8080](http://localhost:8080). Default credentials are:

```
Username: airflow
Password: airflow
```

You can change this credentials setting the following envvars:

```
_AIRFLOW_WWW_USER_USERNAME
_AIRFLOW_WWW_USER_PASSWORD
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
