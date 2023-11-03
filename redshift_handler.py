import os
from flask.cli import load_dotenv
from sqlalchemy import create_engine

def create_redshift_table():
    engine = create_engine(get_redshift_connection_string())
    with engine.connect() as connection:
        connection.execute(open("create_table.sql", "r").read())

def get_redshift_connection_string():
    load_dotenv(".env")
    redshift_host = os.environ.get("REDSHIFT_HOST")
    redshift_port = os.environ.get("REDSHIFT_PORT")
    redshift_db = os.environ.get("REDSHIFT_DB")
    redshift_user = os.environ.get("REDSHIFT_USER")
    redshift_password = os.environ.get("REDSHIFT_PASSWORD")
    
    return f'postgresql://{redshift_user}:{redshift_password}@{redshift_host}:{redshift_port}/{redshift_db}'

def upload_to_redshift(data, table_name):
    engine = create_engine(get_redshift_connection_string())
    data.to_sql(table_name, engine, if_exists='replace', index=False)
