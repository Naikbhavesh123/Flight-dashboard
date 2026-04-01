import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="flight_db",
        user="postgres",
        password="password",  # 🔥 replace this
        port="5432"
    )
    return conn