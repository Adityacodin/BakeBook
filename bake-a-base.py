import sqlite3

conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')

# c = conn.cursor()

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

# c.execute("INSERT INTO user_baked_goods (username,cake,cake_name,pastry,patry_name,breads,bread_name) VALUES ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry.jpg',' ',' ',' ',' ',' ');")
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake3.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake4.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake5.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake6.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake7.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake8.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake9.jpg',' ',' ',' ',' ',' '),
# ('aditya','C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake10.jpg',' ',' ',' ',' ',' ');

# ''')
# conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')
# c = conn.cursor()
# cakes=['Red Velvet','Chocolate','Devil\'s Delight','Truffle Drip','Birthday Treat','Chocolate Mousse','Purple Haze','Wedding Cake','Chip Saga','Black Forest']
# j = 0
# path = ['C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake2.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake3.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake4.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake5.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake6.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake7.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake8.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake9.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry0.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry.jpg']
# pastry = ['C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry1.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry2.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry3.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry4.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry5.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry6.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry7.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry8.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry9.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry10.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry11.jpg']


# for p in pastry:
#     c.execute('''
#     UPDATE user_baked_goods
#     set pastry = ?
#     WHERE username = 'aditya';
#     ''',(p,))
#     conn.commit()

# for cake in cakes:
#     c.execute('''
#     UPDATE user_baked_goods 
#     SET cake_name = ? 
#     WHERE cake = ? 
#     ''',(cake,path[j]))
#     j+=1

# c.execute("select * from user_baked_goods")
# print(c.fetchall())
# c.execute('ALTER TABLE user_baked_goods ADD COLUMN id INTEGER PRIMARY KEY AUTOINCREMENT;')
# conn.commit()
# conn.close()
# c.execute("drop table users;")
# c.execute('SELECT * FROM user_baked_goods')
# print(c.fetchall())

c = conn.cursor()


# c.execute('''
# CREATE TABLE user_baked_goods (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,  
#   username TEXT REFERENCES users(username),
#   cake text,
#   cake_name text,
#   pastry text,
#   patry_name text,
#   breads text,
#   bread_name text,
#     c_qaunt integer,
#     p_quant integer,
#     b_quant_integer
# );
# ''')
# c.execute("DROP TABLE user_baked_goods;")
# c.execute('''
# ALTER TABLE user_baked_goods add b_quant text;
# ''')


# c.execute('''
# SELECT * FROM users;
# ''')
# print(c.fetchall())
# c.execute('SELECT cake_name FROM user_baked_goods;')
# print(c.fetchall())
# 
# 
# 
# c_name = ['Black Forest','Red Velvet','Chocolate Cake','Truffle Drizzle','Vanilla Drip','Birthday Treat','Chococlate Cheesecake','Purple Haze','Wedding Cake','Chip Saga']

# # c.execute('ALTER TABLE user_baked_goods MODIFY c_quant INTEGER;')
# for i in range (7):
# #     # c.execute('''
# #     # INSERT INTO user_baked_goods VALUES (?,'aditya',?,?,?,?,?,?,0,0,0)
# #     # ''',(i,cakes[i],c_name[i],pastries[i],p_name[i],breads[i],b_name[i]))
#     c.execute(f'''
#     UPDATE user_baked_goods 
#     SET b_quant_integer = 10
#     WHERE bread_name = '{b_name[i]}';
#     ''')

# c.execute("update user_baked_goods set patry_name = 'Devils delight' where pastry='C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry7.jpg' ")
# c.execute(f'''
#     UPDATE user_baked_goods 
#     SET c_quant = 10
#     WHERE cake_name = {c_name[0]};
#     ''')

# c.execute('''CREATE TABLE cakes(
#     user TEXT REFERENCES users(username),
#     cake_name TEXT,
#     cake_img TEXT,
#     c_quant INTEGER
# );''')

# c.execute('''CREATE TABLE pastries(
#     user TEXT REFERENCES users(username),
#     pastry_name TEXT,
#     pastry_img TEXT,
#     p_quant  INTEGER
# );''')

# c.execute('''CREATE TABLE breads(
#     user TEXT REFERENCES users(username),
#     bread_name TEXT,
#     bread_img TEXT,
#     b_quant INTEGER
# );''')

# cakes = ['C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake1.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake2.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake3.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake4.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake5.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake6.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake7.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake8.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake9.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake10.jpg',
# ]

# pastries = ['C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry1.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry2.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry3.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry4.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry5.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry6.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry7.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry8.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry9.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry10.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/pastry11.jpg',
# ]

# breads = ['C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/b1.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/b2.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/b3.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/b4.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/b5.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/b6.jpg',
# 'C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/b7.jpg',]

# b_name = ['Brown cookies','Chocolate cookies','Loaf of Bread','Long Bread','Milk Rusk','Butter Rusk','Whole Grain bread']


# p_name= ['Pinapple Peace','Red Star','White Sea','Hazel Bite','Forest White','Trufflesome','Devils delight','Velvet Bliss','Almond & Hazel','Pink rizz','Sweet Three']

# i =0
# c_name = ['Black Forest','Red Velvet','Chocolate Cake','Truffle Drizzle','Vanilla Drip','Birthday Treat','Chococlate Cheesecake','Purple Haze','Wedding Cake','Chip Saga']
# c_price = [500,650,400,780,370,560,400,680,700,900]
# p_price = [50,80,50,70,80,50,40,60,40,80,70]
# b_price = [250,300,40,50,30,40,50]
# for bread in breads:
#     c.execute("INSERT INTO breads VALUES ('aditya',?,?,0,?)",(b_name[i],bread,b_price[i]))
#     i+=1
#     conn.commit()

# c.execute("UPDATE cakes SET cake_img= ? WHERE user = 'aditya' AND cake_name = 'Brown Bad'",('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/c.jpg'))

# c.execute("DELETE FROM pastries WHERE pastry_name = 'Little fusion'")

# new table
# c.execute('DROP TABLE cakes')
# c.execute('DROP TABLE pastries')
# conn.commit()
# c.execute('DROP TABLE breads')

# c.execute('''CREATE TABLE cakes(
#     user TEXT REFERENCES users(username),
#     cake_name TEXT,
#     cake_img TEXT,
#     c_quant INTEGER,
#     price INTEGER
# );''')

# c.execute('''CREATE TABLE pastries(
#     user TEXT REFERENCES users(username),
#     pastry_name TEXT,
#     pastry_img TEXT,
#     p_quant  INTEGER,
#     price INTEGER
# );''')

# c.execute('''CREATE TABLE breads(
#     user TEXT REFERENCES users(username),
#     bread_name TEXT,
#     bread_img TEXT,
#     b_quant INTEGER,
#     price INTEGER
# );''')

# conn.commit()
c.execute('CREATE TABLE orders(order INTEGER PRIMARY KEY,date TEXT, time TEXT)')
conn.close()