import sqlite3
dbconnect = sqlite3.connect("my.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
cursor.execute('SELECT * FROM sensors where type = "door"');
for row in cursor:
        #if row['type'] == 'door':
	print(row['sensorID'],row['type'],row['zone']);
dbconnect.close();

