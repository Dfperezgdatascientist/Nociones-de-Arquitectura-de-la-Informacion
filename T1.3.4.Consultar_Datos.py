#### ENCUESTAS TABLE DATA LOAD

cur.executemany("INSERT INTO Encuestas VALUES (?,?,?,?,?,?,?)",Encuestas_data)

##VERIFYING BDU DATA LOAD WITH PRINT STATEMENT
cur.execute("SELECT * FROM BDU")
items  = cur.fetchall()
for item in items:
  print(item)
##VERIFYING ENCUESTAS DATA LOAD WITH PRINT STATEMENT
cur.execute("SELECT * FROM Encuestas")
items  = cur.fetchall()
for item in items:
  print(item)

###BDU LONGEST CALL DURATION RECORD
cur.execute("SELECT * FROM BDU ORDER BY Duracion DESC")
col_name_list = [tuple[0] for tuple in cur.description]
print("Longest call duration record","\n")
print(col_name_list)
print(cur.fetchone(),"\n","\n")

###BDU SHORTEST CALL DURATION RECORD
cur.execute("SELECT * FROM BDU ORDER BY Duracion ASC")
col_name_list = [tuple[0] for tuple in cur.description]
print("Shortest call duration record","\n")
print(col_name_list)
print(cur.fetchone(),"\n","\n")

###AVERAGE DURATION BY CALL REASON
cur.execute("SELECT Motivo,AVG(duracion)*60 FROM BDU GROUP BY Motivo ORDER BY AVG(Duracion)")
print("Average duration by call reason","\n")
print("Motivo","\t\t","Duracion")
items = cur.fetchall()
for item in items:
  print(item[0],",",item[1])

###AVERAGE NPS IN POLL

cur.execute("SELECT avg(NPS) FROM Encuestas")
print("Average NPS:",cur.fetchall()[0][0],"\n\n")


###AVG NPS BY CALL REASON - BDU and ENCUESTAS TABLE JOIN
cur.execute("""SELECT Motivo,AVG(NPS)  
FROM BDU INNER JOIN Encuestas On Encuestas.Callid=BDU.callid
GROUP BY Motivo ORDER BY AVG(NPS) DESC""")

print("Average NPS by call reason: \n\n")
print("Motivo","\t","NPS","\n")
items = cur.fetchall()
for item in items:
  print(item[0],",",item[1])