import sqlite3

##ONLY USE IF YOU DELETE DATABASE.DB !

## Creating a basic task list
task = [
    'Eat Breakfast',
    'Attend Meeting',
    'Walk Dog',
    'Feed Dog',
    'Go to Gym',
    'Eat lunch',
    'Relax',
    'Read',
    'Take a Break',
    'Go Jogging',
    'Go Swimming',
    'Play Guitar',
    'Listen To Music',
    'Go To Sleep'
]

## Sorting list for easier read
task = sorted(task)

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

## Table Creating and task inserting
cursor.execute("create table task (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(task)):
	cursor.execute("insert into task (name) values (?)",[task[i]])
	print("added ", task[i])

cursor.execute("insert into task (name) values ('This task is new')") ## This is for testing purposes
	
connection.commit()
connection.close()