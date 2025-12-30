import sqlite3

def insert_movie(title: str, year: str, actors: str):
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()

    cursor.execute(
        'INSERT INTO movies (title, year, actors) VALUES (?, ?, ?)',
        (title, year, actors)
    )

    db.commit()
    db.close()

    return
