# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pypyodbc as odbc 
import pandas as pd

DRIVER_NAME = "SQL Server"
SERVER_NAME = "1SAL02\SQLEXPRESS "
DATABASE_NAME = "BD_urbvan"



  
conn = odbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server= localhost;'
                      'Database=BD urbvan;'
                      'Trusted_Connection=yes;')

script = """SELECT trip2.trip_id,departure_at,arrival_at,route_name,vehicle_capacity,reservation.seats, reservation.seats * trip2.seat_price AS Sold_Seats, reservation.seats * trip2.seat_price / trip2.vehicle_capacity * 100 AS Occupancy FROM trip2 INNER JOIN reservation ON trip2.trip_id = reservation.trip_id"""

df = pd.read_sql_query(script, conn)

df.to_excel('C:\\Users\\SSILVAA\\Desktop\\Urbvan.csv')
