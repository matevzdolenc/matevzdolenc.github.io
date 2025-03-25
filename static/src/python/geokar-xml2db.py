#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import geometrijske_karakteristike as geokar
import xml.etree.cElementTree as et
import sys

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

# Vnos podatkov, branje podatkov iz datoteke
xml_tree = et.parse(sys.argv[1])
xml_prerez = xml_tree.getroot()
xml_naslov = xml_prerez.find("naslov")
xml_tocke = xml_prerez.find("tocke")
xml_tocke_seznam = xml_tocke.findall("tocka")

i = 0
for xml_tocka in xml_tocke_seznam:
    format_str = """INSERT INTO tocke (id, x, y) VALUES ("{id}", "{x}", "{y}");"""
    sql_command = format_str.format(id=i, x=float(xml_tocka.find("x").text), y=float(xml_tocka.find("y").text))
    cursor.execute(sql_command)
    i = i + 1
    db.commit()

db.close()


