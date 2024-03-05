import json
import psycopg2
from psycopg2 import sql

def create_exchange_rates_table():
    try:
        # Load database connection configuration from 'creds.json' file
        with open('creds.json', 'r') as file:
            config = json.load(file)

        # Construct a connection string using database configuration
        conn_str = ("dbname={database} user={user} " +
                    "password={password} host={host} port={port}") \
                    .format(database=config['database'],
                            user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'])

        # Connect to the PostgreSQL database using the connection string
        conn = psycopg2.connect(conn_str)

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Define the schema and table names for the PostgreSQL database
        schema_name = "javier_santibanez_coderhouse"
        table_name = "exchange_rates_mxn"

        # Define the SQL query to create the table if it does not exist
        create_table_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS {}.{} (
                id INTEGER IDENTITY(1,1) PRIMARY KEY,
                currency VARCHAR(10),
                rate_date DATE,
                rate DECIMAL(15, 5),
                update_date DATE
            )
        """).format(
            sql.Identifier(schema_name),
            sql.Identifier(table_name)
        )

        # Execute the create table query
        cursor.execute(create_table_query)

        # Commit the changes to the database
        conn.commit()

        # Print success message
        print(f"Table '{table_name}' created successfully.")

    except psycopg2.Error as e:
        # Print error message if an exception occurs
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection in the 'finally' block to ensure it's done regardless of success or failure
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # Execute the create_exchange_rates_table function when the script is run
    create_exchange_rates_table()