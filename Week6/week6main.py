# Week 6 CIS162 Michael Audi SQLite3 Assignment

import sqlite3
from sqlite3 import Error
from pathlib import Path


def sql_connection(dbname: str):
    try:
        con = sqlite3.connect(dbname)
        print("Connection is established: Database is created in workspace")
        return con
    except Error:
        print(Error)


def sql_table(con, name, columnvalues, columnum, data):
    cur = con.cursor()
    cur.execute(
        f'CREATE TABLE IF NOT EXISTS {name}( {columnvalues})')
    cur.executemany(
        f"INSERT OR IGNORE INTO {name} VALUES({', '.join(['?'] * columnum)})", data)

    con.commit()


def sql_print_table(con, table_name):
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def sql_query_table(con, table_name, category, value):
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table_name} WHERE {category} = '{value}'")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def sql_genre_match(con):
    cur = con.cursor()
    cur.execute(
        f"SELECT Music_Artists.* FROM Music_Artists INNER JOIN Genres ON Music_Artists.genre = Genres.genre"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)


def sql_artist_query(con, query):
    cur = con.cursor()
    cur.execute(
        f"SELECT Music_Artists.artist, Music_Artists.genre, Music_Artists.number_recordings, Genres.city, Cities.population FROM Music_Artists INNER JOIN Genres ON Music_Artists.genre = Genres.genre INNER JOIN Cities on Genres.city = Cities.city WHERE Music_Artists.artist = '{query}'"
    )
    rows = cur.fetchall()
    if rows != []:
        return f"{rows[0][1]} artist {rows[0][0]} has {rows[0][2]} recordings and is most popular in {rows[0][3]} with a population of {rows[0][4]:,}"
    else:
        cur.execute(
            f"SELECT Music_Artists.artist, Music_Artists.genre, Music_Artists.number_recordings FROM Music_Artists WHERE Music_Artists.artist = '{query}'"
        )
        rows = cur.fetchall()
        if rows != []:
            return f"{rows[0][1]} artist {rows[0][0]} has {rows[0][2]} recordings and is popular everywhere."
        else:
            return f"The artist, {query}, was not found in the database."


def main():
    con = sql_connection(Path(__file__).parent.resolve() / 'micycle.db')

    artistdata = (
        ('Miley Cyrus', 'Rock', 14),
        ('Dolly Parton', 'Country', 123),
        ('Eminem', 'HipHop', 98),
        ('Brittany Howard', 'Rock', 37),
        ('Noah Kahan', 'Folk-Pop', 87),
        ('Teminite', 'Dubstep', 147),
        ('Juice WRLD', 'HipHop', 200)
    )
    sql_table(con, "Music_Artists",
              "artist text PRIMARY KEY, genre text, number_recordings integer, FOREIGN KEY (genre) REFERENCES Genres (genre)", 3, artistdata)
    print("**********************\nMusic Artists")
    sql_print_table(con, "Music_Artists")

    genredata = (
        ('Rock', 'Los Angeles'),
        ('Hippie', 'Eugene'),
        ('Opera', 'Florence'),
        ('Folk-Pop', 'New York City'),
        ('Dubstep', 'London')
    )
    sql_table(con, "Genres",
              "genre text PRIMARY KEY, city text, FOREIGN KEY (city) REFERENCES Cities (city)", 2, genredata)

    print("**********************\nGenres")

    sql_print_table(con, "Genres")

    print("**********************\nGenres and Artists")

    sql_genre_match(con)

    print("**********************\nCities")
    citydata = (
        ('Los Angeles', 'CA', 66666, 10000000),
        ('Eugene', 'OR', 55555, 80000),
        ('Nashville', 'TN', 11111, 1500000),
        ('New York City', 'NY', 10001, 8470000)
    )

    sql_table(con, "Cities",
              "city text PRIMARY KEY, state text, zipcode integer, population integer", 4, citydata)
    sql_print_table(con, "Cities")
    print("**********************")

    userask = input("Which artist would you like to learn more about? ")
    print(sql_artist_query(con, userask))
    con.close()


if __name__ == '__main__':
    main()
