import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="password")

cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
conn.commit()
