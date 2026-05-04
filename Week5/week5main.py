# Week 5 CIS162 Michael Audi SQLite3 Assignment

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


def sql_table(con, data):
    cur = con.cursor()
    cur.execute(
        'CREATE TABLE Music_Artists( artist text, genre text, number_recordings integer)')
    cur.executemany("INSERT INTO Music_Artists VALUES(?, ?, ?)", data)
    con.commit()


def sql_print(con):
    cur = con.cursor()
    cur.execute("SELECT * FROM Music_Artists")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def sql_query(con, category, value):
    cur = con.cursor()
    cur.execute(f"SELECT * FROM Music_Artists WHERE {category} = '{value}'")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def main():
    con = sql_connection(Path(__file__).parent.resolve() / 'micycle.db')

    data = (
        ('Miley', 'Rock', 14),
        ('Dolly', 'Country', 123),
        ('Eminen', 'HipHop', 98),
        ('Brittany', 'Rock', 37)
    )
    sql_table(con, data)

    sql_print(con)
    print("**********************")
    sql_query(con, "genre", "Rock")
    print("**********************")

    con.close()


if __name__ == '__main__':
    main()
