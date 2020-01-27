
import psycopg2


conn = psycopg2.connect(host="localhost", port = 5432, database="cloudManagment", user="postgres", password="پسورد postgres")
cur = conn.cursor()
print("print successfully :)))))")

