from os import getenv
import pymssql


if __name__ == "__main__":

    server = getenv("SQL_HOST")
    user = getenv("SQL_USERNAME")
    password = getenv("SQL_PASSWORD")
    db = "PCKasse"

    conn = pymssql.connect(server, user, password, db)
    cursor = conn.cursor()
    cursor.execute("USE PCKasse")

    # you must call commit() to persist your data if you don't set autocommit to True
    conn.commit()

    cursor.execute("SELECT TOP(5) * FROM Articles")

    row = cursor.fetchall()
    while row:
        print("ID=%d, Name=%s" % (row[0], row[1]))
        row = cursor.fetchone()

    conn.close()

