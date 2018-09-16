import re
import openpyxl
import sqlite3
from sqlite3 import Error
import numpy as np
import matplotlib.pyplot as plt

wb_ins = openpyxl.load_workbook("inspections.xlsx")
sheet_ins = wb_ins['inspections']

 #wb_viol = openpyxl.load_workbook("violations.xlsx")
 #sheet_viol = wb_viol['violations']

try:
    connection = sqlite3.connect("Food_violations.db")                  # creating a new database file (if it doesn't exist already)
    print("Food_violations.db created")    
except Error as e:
    print(e)

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS inspection")
        
sql = """CREATE TABLE inspection (
    activity_date Date,
    employee_id char(10),    
    facility_address char(50),
    facility_city char(30),
    facility_id char(14) PRIMARY KEY,
    facility_name char(50),
    facility_state char(2),
    facility_zip char(14),
    grade char(1),
    owner_id char(15),
    owner_name char(50),
    pe_description char(50),
    program_element_pe number(4),
    program_name char(50),
    program_status char(10),
    record_id char(14), 
    score number(3),
    serial_number char(15),
    service_code number(3),
    service_description char(30));"""

cursor.execute(sql)

 #file = open("food_viol_schema.sql")
 #cursor.execute(file.read())

for row in sheet_ins.iter_rows(min_row=2, max_row=5):               # delete max_row=5 !!! TEST
    activity_date = row[0].value
    employee_id = row[1].value
    facility_address = row[2].value
    facility_city = row[3].value
    facility_id = row[4].value
    facility_name = row[5].value
    facility_state = row[6].value
    facility_zip = row[7].value
    grade = row[8].value
    owner_id = row[9].value
    owner_name = row[10].value
    pe_description = row[11].value
    program_element_pe = row[12].value
    program_name = row[13].value
    program_status = row[14].value
    record_id = row[15].value
    score = row[16].value
    serial_number = row[17].value
    service_code = row[18].value
    service_description = row[19].value
    
    cursor.execute("INSERT INTO inspection VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (activity_date, employee_id, facility_address, facility_city, facility_id, facility_name, facility_state, facility_zip, grade, owner_id, owner_name, pe_description, program_element_pe, program_name,  program_status, record_id, score, serial_number, service_code, service_description))
    
cursor.execute("SELECT activity_date FROM inspection")
activity_date_db = cursor.fetchall()
print(activity_date_db)
    
    
#cursor.execute("SELECT program_element_pe FROM inspection")
#program_element_pe_db = cursor.fetchall()

#cursor.execute("SELECT service_code FROM inspection")
#service_code_db = cursor.fetchall()

#plt.plot(program_element_pe_db, service_code_db)





























