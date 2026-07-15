import sqlite3

DATABASE_PATH = "app/database/database.db"

def get_connection():
    """
    Create and return a SQLite database connection.
    """
    connection = sqlite3.connect(DATABASE_PATH)

    # Return rows like dictionaries
    connection.row_factory = sqlite3.Row

    return connection
def get_cursor():
    """
    Returns a database cursor.
    """

    connection = get_connection()

    cursor = connection.cursor()

    return connection, cursor
def close_connection(connection):
    """
    Safely close the database connection.
    """

    if connection:
        connection.close()