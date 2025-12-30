from flask import Flask, render_template, request, redirect, url_for, flash
from insert_movie import insert_movie
from list_movie import list_movies
from remove_movie import remove_movie
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    movies_list = list_movies()

    return render_template('home.html', movies = movies_list)

@app.route('/addMovie',methods=['GET', 'POST'])
def addMovie():
    if request.method == 'POST':
        movieTitle = request.form.get('title')
        movieYear = request.form.get('year')
        movieActors = request.form.get('actors')

        if not movieTitle or not movieYear or not movieActors:
            flash("All fields must be filled in!", "error")
            return redirect(url_for('addMovie'))

        try:
            insert_movie(movieTitle, movieYear, movieActors)
        except Exception as e:
            flash(f"An error occurred while adding the movie: {e}", "error")
            return redirect(url_for('addMovie'))

        flash("Movie added successfully!", "success")
        return redirect(url_for('home'))

    return render_template('add.html')

@app.route('/movieToRemove',methods=['POST'])
def movieToRemove():

    movies_to_remove_ids = request.form.getlist('movieToRemove')

    if movies_to_remove_ids:
        remove_movie(movies_to_remove_ids)

    flash("Movie deleted from your collection!", "success")

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
