import sqlite3

def list_movies():
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    list = cursor.execute('SELECT * FROM movies')

    return list
