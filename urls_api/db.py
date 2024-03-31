import psycopg2

def connect_db():
    connection = psycopg2.connect(
        dbname='urls_db', 
        user='postgres', 
        password='postgres', 
        host='localhost', 
        port='5432'
    )
    return connection