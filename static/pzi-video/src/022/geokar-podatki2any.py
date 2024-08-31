#! /usr/bin/env python

import sys
import xml.etree.cElementTree as et
import sqlite3

def izpis_v_txt_datoteko(n, x, y):
    dat = open(sys.argv[1] + ".txt")

    dat.write("{}\n".format(n))
    for i in range(n):
        dat.write("{} {}\n".format(x[i], y[i]))

    dat.close()


def izpis_v_xml_datoteko(n, x, y):
    xml_prerez = et.Element("prerez")

    xml_tocke = et.SubElement(xml_prerez, "tocke")

    for i in range(n):
        xml_tocka = et.SubElement(xml_tocke, "tocka")
        xml_tocka.set("id", str(i + 1))

        xml_x = et.SubElement(xml_tocka, "x")
        xml_x.text = str(x[i])
        xml_y = et.SubElement(xml_tocka, "y")
        xml_y.text = str(y[i])

    xml_tree = et.ElementTree(xml_prerez)
    xml_tree.write(sys.argv[1] + ".xml", encoding='utf-8', xml_declaration=True)


def izpis_v_json_datoteko(n, x, y):
    pass


def izpis_v_sqlite_datoteko(n, x, y):
    # Ustvari SQLite bazo in določi tabelo
    db = sqlite3.connect(sys.argv[1] + ".sqlite")
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


def vnos_podatkov():
    # Vnos podatkov
    xml_tree = et.parse(sys.argv[1])

    xml_prerez = xml_tree.getroot()
    xml_tocke = xml_prerez.find("tocke")
    xml_tocke_seznam = xml_tocke.findall("tocka")

    n = len(xml_tocke_seznam)
    x = []
    y = []

    for xml_tocka in xml_tocke_seznam:
        x.append(float(xml_tocka.find("x").text))
        y.append(float(xml_tocka.find("y").text))

    x.append(x[0])
    y.append(y[0])

    return n, x, y


def main():
    # Vnos podatkov
    print("Vnos podatkov ...")
    n, x, y = vnos_podatkov()

    # Izpis podatkov
    izpis_v_txt_datoteko(n, x, y)
    izpis_v_xml_datoteko(n, x, y)
    izpis_v_json_datoteko(n, x, y)
    izpis_v_sqlite_datoteko(n, x, y)

if __name__ == "__main__": main()
