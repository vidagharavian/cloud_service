import psycopg2


conn = psycopg2.connect(host="localhost", port = 5432, database="CloudManagement", user="postgres", password="1235698")
cur = conn.cursor()


print("print successfully :)))))")