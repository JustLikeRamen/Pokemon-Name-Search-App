"""
A pokemon data search flask app.
Data is stored in a SQLite database that looks something like the following:

+--------------+------------------+--------------+------------------+-----------+
| Name         | Dex Entry #      | Abilities    | Additional Forms | Types     |
+==============+==================+==============+==================+===========+
| Clefairy     | 35               | Friend Guard | Clefairy         | Fairy     |
+--------------+------------------+--------------+------------------+-----------+

This can be created with the following SQL (see bottom of this file):

    create table pokemon (name text, entryDex integer, abilities text, forms text, types text);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'pokemon.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from pokemon")
        except sqlite3.OperationalError:
            cursor.execute("create table pokemon (entryDex integer, name text, abilities text, forms text, sprite text, types text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: entryDex, name, abilities, forms, sprite, types
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pokemon")
        return cursor.fetchall()

    def insert(self, entryDex, name, abilities, forms, sprite, types):
        """
        Inserts pokemon into database
        :param entryDex: Integer
        :param name: String
        :param abilities: String
        :param forms: String
        :param sprite: String
        :param types: String
        :raises: Database errors on connection and insertion
        """
        params = {'entryDex':entryDex, 'name':name, 'abilities':abilities, 'forms':forms, 'sprite':sprite, 'types':types}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into pokemon (entryDex, name, abilities, forms, sprite, types) VALUES (:entryDex, :name, :abilities, :forms, :sprite, :types", params)

        connection.commit()
        cursor.close()
        return True
