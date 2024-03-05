# coderhouse-de-entregable01

This repo contains the notebooks for the first homework of the course of data engineering at CoderHouse.

## Code

### 1-1-get-exchange-rates-from-api.ipynb and 1-get-exchange-rates-from-api.py

This Jupyter Notebook and python script contains functions for downloading data from an API. Here are the main functions:

- `get_target_currencies`:  Get a list of target currencies relative to the given base currency.
- `format_exchange_rates`: Format exchange rates from the API response.
- `get_currencies_from`: Get formatted exchange rates for a specific base currency and start date.

#### Example Usage

```python
currencies = get_currencies_from('MXN', '2024-02-01')
print(currencies)
```

### 2-create-table-in-database.ipynb and 2-create-table-in-database.py

This Jupyter Notebook and python script contains code for creating a table in a database. The code includes the use of functions like `sql.Identifier` for constructing SQL queries.

#### Execution Steps

1. **Load Configuration:** Reads database connection configuration from 'creds.json'.
2. **Connect to Database:** Establishes a connection to the PostgreSQL database using `psycopg2`.
3. **Define Schema and Table Names:** Specifies the schema and table names for the PostgreSQL database.
4. **Create Table Query:** Constructs an SQL query to create a table with specific columns if it does not already exist.
5. **Execute Table Creation:** Executes the create table query using the database cursor.
6. **Commit Changes and Close Connections:** Commits the changes to the database and closes the cursor and connection.

## Environment Configuration

### environment.yml

The `environment.yml` file contains the configuration necessary to recreate the project environment. You can use this file with conda to create a virtual environment with the required dependencies.

#### Recreate Environment

```bash
conda env create -f environment.yml
conda activate  coderhouse-de-01
```