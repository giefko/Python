import csv
import cx_Oracle
con = cx_Oracle.connect('hr/hrpsw@localhost/orcl')
cursor = con.cursor()
csv_file = open("locations.csv", "w")
writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
r = cursor.execute("SELECT * FROM locations")
for row in cursor:
    writer.writerow(row)

cursor.close()
con.close()
csv_file.close()