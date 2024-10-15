# db_config.py
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
        print("Dados Atualizados.")
        return conn
    except psycopg2.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def get_user_by_email(email):
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
            user = cursor.fetchone()
            return user
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
        return None
    finally:
        if conn:
            conn.close()
