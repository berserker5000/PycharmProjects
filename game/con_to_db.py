__author__ = 'kud'
import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

'''
import csv

with open('Book1.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for q in reader:
        print len(q)
        for i in range(0,len(q)):
            print(q[i])
'''
def build_dicts(table):
    dictionary={}
    with con:
        cur.execute("SELECT * FROM " + str(table))
        rows = cur.fetchall()
        for row in rows:
            dictionary[row[0]]=row[1]
        return dictionary

def print_from_db(table):
    with con:
        cur.execute("SELECT * FROM " + str(table))
        rows = cur.fetchall()
        row = [row[1] for row in rows]
        return row


def create_table(table):
        try:
            cur.execute("CREATE TABLE IF NOT EXISTS '"+table+"' (id INTEGER PRIMARY KEY AUTOINCREMENT, text CHAR UNIQUE)")
            con.commit()
        except sqlite3.OperationalError:
            pass


def insert_to_table(table, data):
    for i in data:
        try:
            cur.execute("INSERT INTO " + table + " (text) VALUES ('" + str(i) + "')")
        except sqlite3.IntegrityError:
            pass
    con.commit()


# d=[]
# for i in range(100,5000,2):
#     d.append(i)
# insert_to_table("incorrect",d)