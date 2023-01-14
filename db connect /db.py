import psycopg2

conn = psycopg2.connect(
   database="lambda", user='sabbir1021', password='sabbir1021', host='localhost', port= '5432'
)

cursor = conn.cursor()


# Table create
# cursor.execute('''
# 	CREATE TABLE users
# 	(
# 	    id integer,
# 	    username VARCHAR(30),
# 	    email VARCHAR(30),
# 	    phone VARCHAR(30),
# 	    password VARCHAR(30),
# 	    PRIMARY KEY (id)
# 	);
# ''') 



# GET REQUEST : 
# cursor.execute("""
#         SELECT id, name , codename 
#         FROM auth_permission
#     """)
# # for fetchall for all data, fetchone for single data
# data = cursor.fetchall()
# res = 0 
# for i in data:
#     a = i[0]
#     res = res + a
# print("Total Number: ", res)


#POST REQUEST



cursor.execute('''INSERT INTO users(id, username, email, phone, password) 
     VALUES (1, 'sabbir1021', 'sabbir@gmail.com', '01758514752', '123456')''')
conn.commit()


conn.close()
