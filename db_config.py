import psycopg2
import psycopg2.extras
from credentials import Credentials

creds = Credentials()

host = creds.get_host()
port = creds.get_port()
user = creds.get_user()
password = creds.get_password()
db_name = creds.get_db_name()


def get_connection():
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            dbname=db_name,
            client_encoding='UTF8'
        )
        with conn.cursor() as cursor:
            cursor.execute("SET search_path TO osint;")
        print("Conexão estabelecida com sucesso.")
        return conn
    except psycopg2.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def testar_conn():
    get_connection()

import psycopg2.extras  # Certifique-se de importar isso para usar o DictCursor

def get_user_by_email(email):
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:  # Usando DictCursor para dicionários
            cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
            user = cursor.fetchone() 
            print(user)
            return user
    except UnicodeDecodeError as e:
        print(f"Erro de decodificação: {e}")
        return None
    finally:
        if conn:
            conn.close()



