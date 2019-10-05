import sqlite3
dbconnect = sqlite3.connect("my.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
cursor.execute('''insert into sensors values (1,'door','kitchen')''');
cursor.execute('''insert into sensors values (2,'temperature','kitchen')''');
cursor.execute('''insert into sensors values (3,'door','garage')''');
cursor.execute('''insert into sensors values (4,'motion','garage')''');
cursor.execute('''insert into sensors values (5,'temperature','garage')''');
dbconnect.commit();
cursor.execute('SELECT * FROM sensors');
for row in cursor:
	print(row['sensorID'],row['type'],row['zone']);
dbconnect.close();
