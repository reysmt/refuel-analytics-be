from sqlalchemy import create_engine, text, URL
from sqlalchemy.exc import SQLAlchemyError

url_object = URL.create(
    drivername="postgresql+psycopg2",
    username="db",
    password="password",  # Caratteri speciali gestiti automaticamente
    host="host",
    port=28639,
    database="db"
)
engine = create_engine(url_object, pool_pre_ping=True)

def connect_db():
    try:
        # Tenta la connessione ed esegue una query semplice
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Connected to DB!")
    except SQLAlchemyError as e:
        print(f"Something has gone wrong on DB connection: {e}")

def disconnect_db():
    try:
        with engine.connect() as connection:
            connection.close()
            print("Disconnected from DB!")
    except SQLAlchemyError as e:
        print(f"Something has gone wrong on DB connection: {e}")
