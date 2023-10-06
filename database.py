import psycopg2

conn = psycopg2.connect(dbname="metanit", user="postgres", password="000", host="127.0.0.1")
cursor = conn.cursor()

# получаем все данные из таблицы users
cursor.execute("SELECT * FROM users")
users_data_from_db = cursor.fetchall()
# будет вывыодить кортеж ()

# получаем все данные из таблицы users
cursor.execute("SELECT * FROM categories")
categories_data_from_db = cursor.fetchall()

# получаем все данные из таблицы articles
cursor.execute("SELECT * FROM articles")
articles_data_from_db = cursor.fetchall()

cursor.close()
conn.close()