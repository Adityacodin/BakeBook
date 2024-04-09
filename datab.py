import sqlite3

conn = sqlite3.connect('C:/Users/33333333333333333333/gitdemo/BakeBook/trial.db')
c = conn.cursor()

c.execute('''
# INSERT INTO IMAGES (path) VALUES ('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake1.jpg'),
# ('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake2.jpg'),
# ('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake3.jpg'),
# ('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake4.jpg'),
# ('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake5.jpg'),
# ('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake6.jpg'),
# ('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake7.jpg'),
# ('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake8.jpg'),
# ('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake9.jpg'),
# ('C:/Users/33333333333333333333/gitdemo/BakeBook/usercakes/cake10.jpg');


# ''')

# c.execute('CREATE TABLE IMAGES(path TEXT);')
# print(c.fetchall())

conn.commit()
conn.close()
