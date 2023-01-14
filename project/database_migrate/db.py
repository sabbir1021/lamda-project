import psycopg2

conn = psycopg2.connect(
   database="lambda", user='sabbir1021', password='sabbir1021', host='localhost', port= '5432'
)

cursor = conn.cursor()

# User Table Create
try:
   cursor.execute("SELECT * FROM users;")

except:
   cursor.execute('''
      CREATE TABLE users
      (
         id integer,
         username VARCHAR(30),
         email VARCHAR(30),
         phone VARCHAR(30),
         password VARCHAR(30),
         PRIMARY KEY (id)
      );
   ''')




# Test Table Create
try:
   cursor.execute("SELECT * FROM orders;")

except:
   cursor.execute('''
      CREATE TABLE orders
      (
         id integer,
         name VARCHAR(30)
      );
   ''')

# Save
conn.commit()
conn.close()
