import sqlite3
connection = sqlite3.connect('movies-database.db')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS 
movies(mov_id INTEGER PRIMARY KEY, mov_title TEXT, actor_name TEXT,
 year INTEGER, dir_name TEXT)"""

cursor.execute(command1)
cursor.execute("INSERT INTO movies VALUES(1,'3-idiots','Amir khan',2009,'Rajkumar hirani')")
cursor.execute("INSERT INTO movies VALUES(2,'Kirik party','Rakshit shetty',2016,'Rishab shetty')")
cursor.execute("INSERT INTO movies VALUES(3,'KGF','Yash',2022,'Prashanth Neel')")

cursor.execute("SELECT * FROM movies")
results = cursor.fetchall()

print(results)
print('Details of the movie in which  Yash was the lead actor')
cursor.execute("SELECT * FROM movies WHERE actor_name='Yash'")
res = cursor.fetchall()
print(res)