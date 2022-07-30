from sqlalchemy import create_engine
from configparser import ConfigParser

file = 'config.ini'

config = ConfigParser()
config.read(file)

USER_BASE = config['database']['user']
PASSWORD_BASE = config['database']['passw']
DATABASE = config['database']['db']
PORT = config['database']['port']
HOST = config['database']['host']

def db_connection():
    
    create_connection = f'postgresql+psycopg2://{USER_BASE}:{PASSWORD_BASE}@{HOST}:{PORT}/{DATABASE}'
    connection = create_engine(create_connection)
    return connection
