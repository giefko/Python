import cx_Oracle
import csv

con = cx_Oracle.connect('hr/hrpsw@localhost/orcl')
cur = con.cursor()
with open("locations_wheader.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter='|')
    for lines in csv_reader:
        cur.execute(
            "insert into new_locations (LOCATION_ID, STREET_ADDRESS, POSTAL_CODE,"
            " CITY, STATE_PROVINCE, COUNTRY_ID) values (:1, :2, :3, :4, :5, :6)",
            (lines['LOCATION_ID'], lines['STREET_ADDRESS'], lines['POSTAL_CODE'],
             lines['CITY'], lines['STATE_PROVINCE'], lines['COUNTRY_ID']))

cur.close()
con.commit()
con.close()