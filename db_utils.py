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


def list_movies():
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    list = cursor.execute('SELECT * FROM movies')

    return list


def remove_movie(movie_ids):
    if not movie_ids:
        return

    db = sqlite3.connect('movies.db')
    cursor = db.cursor()

    movie_ids = [int(movie_id) for movie_id in movie_ids]
    placeholders = ",".join("?" for _ in movie_ids)

    query = f"DELETE FROM movies WHERE id IN ({placeholders})"
    cursor.execute(query, movie_ids)

    db.commit()
    db.close()

    return
