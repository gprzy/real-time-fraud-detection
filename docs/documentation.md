## `data_source`

Para disponibilizar o endpoint contendo a base bruta de dados, execute, no diretório raíz do projeto:

```bash
python3 data_source/app.py
```

## `etl`

### Extract

```bash
python3 .\etl\airflow\scripts\extract.py
```

### Transform

```bash
python3 .\etl\airflow\scripts\transform.py
```

### Load

```bash
python3 .\etl\airflow\scripts\load.py
```

## `fraud_detection`

```bash
python3 fraud_detection/app.py
```

## `online_payments`

```bash
python3 online_payments/app.py
```

```bash
pre-commit install
```