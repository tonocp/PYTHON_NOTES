import mysql.connector


def connect():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="python_notes",
        port=3306
    )
    cursor = database.cursor(buffered=True)
    return [database, cursor]
