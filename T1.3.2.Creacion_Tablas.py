import sqlite3

conn = sqlite3.connect('mydb')

#Create a cursor
cur = conn.cursor()
#Create a table
cur.execute(""" CREATE TABLE BDU (
Callid integer,
CC text,
Duracion REAL,
Motivo text,
Fecha blob
)
""")


##Commit our command
conn.commit()

#Close our Connection
conn.close()

cur.execute(""" CREATE TABLE Encuestas (
S integer,
Callid integer,
CC text,
Fecha blob,
NPS integer,
Satu integer,
Solucion integer
)
""")
##Commit our command
conn.commit()
#Close our Connection
conn.close()

