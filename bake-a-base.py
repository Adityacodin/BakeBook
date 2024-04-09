import sqlite3

conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')

c = conn.cursor()

# c.execute('''
# CREATE TABLE Baker(
#     U_NAME text,
#     PASSKEY text
# )
# ''')

# c.execute("DROP TABLE Baker")
# string = '576t8*&&'
# c.execute(f"INSERT INTO Baker VALUES ('ais&*&&^h','{string}')")
# c.execute("SELECT * FROM user_details")
# print(c.fetchall())
# c.execute('''
# CREATE TABLE user_details (
#   id integer,
#   U_NAME text NOT NULL,
#   PASSKEY text NOT NULL,  -- This is not secure, consider hashing passwords
#   img_path text,
#   FOREIGN KEY (U_NAME) REFERENCES Baker(U_NAME)  -- Assuming username is unique in the user table
# );''')

# c.execute('''
# CREATE TABLE user_baked_goods (
#   username TEXT REFERENCES users(username),
#   cake text,
#   cake_name text,
#   pastry text,
#   patry_name text,
#   breads text,
#   bread_name text
# );
# ''')
# c.execute('''
# CREATE TABLE users (
#   username TEXT ,
#   password TEXT PRIMARY KEY
# );
# ''')
# c.execute('ALTER TABLE user_baked_goods MODIFY username TEXT')
# c.execute('''DROP TABLE user_baked_goods;''')
# ''')
# print(c.fetchall())

c.execute("INSERT INTO user_baked_goods (username,cake,cake_name,pastry,patry_name,breads,bread_name) VALUES ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake1.jpg',' ',' ',' ',' ',' ');")
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake3.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake4.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake5.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake6.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake7.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake8.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake9.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake10.jpg',' ',' ',' ',' ',' ');

# ''')
# c.execute("drop table users;")
# c.execute('SELECT * FROM user_baked_goods')
# print(c.fetchall())
conn.commit()
conn.close()
