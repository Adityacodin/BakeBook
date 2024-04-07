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
c.execute("SELECT * FROM Baker")
print(c.fetchall())
conn.commit()
conn.close()
