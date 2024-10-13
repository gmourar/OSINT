import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='seu_usuario',
        password='sua_senha',
        db='osint_db'
    )

def get_user_by_user(user):
    conn = get_connection()
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM usuarios WHERE user=%s", (user,))
        return cursor.fetchone()
