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
#   username TEXT PRIMARY KEY REFERENCES users(username),
#   cake INTEGER,
#   pastry INTEGER,
#   breads INTEGER
# );
# ''')
# c.execute('''
# CREATE TABLE users (
#   username TEXT PRIMARY KEY UNIQUE,
#   password TEXT
# );

# ''')
# print(c.fetchall())

c.execute('''

''')
conn.commit()
conn.close()
