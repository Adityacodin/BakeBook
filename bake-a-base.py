import sqlite3

conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/bakebase.db')

c = conn.cursor()

# c.execute('''
# CREATE TABLE USER(
#     U_NAME text,
#     PASSKEY integer
# )
# ''')
# c.execute("INSERT INTO USER VALUES ('aish',3434)")/
c.execute("SELECT * FROM USER")
print(c.fetchall())
conn.commit()
conn.close()
