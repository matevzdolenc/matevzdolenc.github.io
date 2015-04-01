#! /usr/bin/env python

import sys
import sqlite3

def vnos_podatkov():
    # Vnos podatkov
    dat = open(sys.argv[1], "r")

    n = int(dat.readline())

    x = []
    y = []
    for i in range(n):
        vrstica = dat.readline()
        besede = vrstica.split()
        x.append(float(besede[0]))
        y.append(float(besede[1]))

    x.append(x[0])
    y.append(y[0])

    dat.close()

    return n, x, y

def izpis_v_sqlite_datoteko(n, x, y):
    # Ustvari SQLite bazo in določi tabelo
    db = sqlite3.connect(sys.argv[2])
    cursor = db.cursor()
    sql_command = """
    CREATE TABLE IF NOT EXISTS tocke (
    id INTEGER PRIMARY KEY,
    x DOUBLE,
    y DOUBLE);"""
    cursor.execute(sql_command)
    db.commit()

    for i in range(n):
        # format_str = """INSERT INTO tocke (id, x, y) VALUES ("{id}", "{x_sql}", "{y_sql}");"""
        # sql_command = format_str.format(id=i+1, x_sql=x[i], y_sql=y[i])
        sql_command = """INSERT INTO tocke (id, x, y) VALUES ("{}", "{}", "{}");""".format(i+1, x[i], y[i])
        cursor.execute(sql_command)
        db.commit()

    db.close()


def main():
    # Vnos podatkov
    print("Vnos podatkov ...")
    n, x, y = vnos_podatkov()

    # Izpis podatkov v XML datoteko
    print("Izpis v SQLite ...")
    izpis_v_sqlite_datoteko(n, x, y)


if __name__ == "__main__": main()
