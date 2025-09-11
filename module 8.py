import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='albaraae',
         password='1234',
         autocommit=True
         )
ICAO_code = input('What is the ICAO code of the airport?: ')
cursor = connection.cursor()
cursor.execute(f"select name, municipality from airport where ident = '{ICAO_code}' ")
info = cursor.fetchall()
for airport_name, town_name in info:
    print('The airport is:' , airport_name)
    print('The town is:', town_name)


import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='albaraae',
         password='1234',
         autocommit=True
         )
area_code = input('What is the area code?: ')
cursor = connection.cursor()
cursor.execute(f"select type, count(*) from airport where iso_country = '{area_code}' group by type")
airports_sorted_by_type = cursor.fetchall()
for airport_type, number in airports_sorted_by_type:
    print(f'The country has: {number} {airport_type} ')


import mysql.connector
from geopy.distance import geodesic
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='albaraae',
         password='1234',
         autocommit=True
         )
ICAO1, ICAO2 = input('Enter the ICAO code of the airports: ').split()
cursor = connection.cursor()
cursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{ICAO1}'")
p1 = cursor.fetchall()
cursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{ICAO2}'")
p2 = cursor.fetchall()
if p1 and p2:
    coord1 = (p1[0][0], p1[0][1])
    coord2 = (p2[0][0], p2[0][1])
    distance = geodesic(coord1, coord2).kilometers
    print(f"Distance between {ICAO1} and {ICAO2} is: {distance} km")







