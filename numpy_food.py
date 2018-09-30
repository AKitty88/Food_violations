import sqlite3
from sqlite3 import Error
import numpy as np
import matplotlib.pyplot as plt

try:
    connection = sqlite3.connect("Food_violations.db")
    print("Food_violations.db connected")
except Error as e:
    connection.close()
    print(e)
  
cursor = connection.cursor()
    
# =============================================================================
# Task 1:
# cursor.execute("SELECT COUNT(*) FROM inspection WHERE activity_date >= '01/07/2015' AND activity_date <= '31/12/2017';")
# sum_viol = cursor.fetchall()
# print(sum_viol)
# =============================================================================

cursor.execute("SELECT facility_zip FROM inspection WHERE activity_date >= '01/07/2015' AND activity_date <= '31/12/2017';")
postcodes = cursor.fetchall()

# =============================================================================
# avg_viol= []
# max_viol_per_postc = 0.0001
# postcode_max_viol = ''
# 
# for postc in postcodes:
#     cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '01/07/2015' AND activity_date <= '31/12/2017') AND facility_zip=(?);", (postc[0],))
#     viols_per_postc = cursor.fetchall()
#     avg_viol.append((viols_per_postc[0][0] * 100) / sum_viol[0][0])
#
# Task 2:
#     if viols_per_postc[0][0] > max_viol_per_postc:
#         max_viol_per_postc = viols_per_postc[0][0]
#         postcode_max_viol = postc[0]                                        # POSTCODE with highest total violations
# print(postcode_max_viol)
# =============================================================================

# Task 3:
cursor.execute("SELECT outer.facility_zip, \
               (SELECT count(r2.facility_id) from inspection r2 WHERE outer.facility_zip=r2.facility_zip GROUP BY r2.facility_zip,strftime('%Y-%m',r2.activity_date) ORDER BY count(r2.facility_id) DESC)-(SELECT count(r2.facility_id) from inspection r2 WHERE outer.facility_zip=r2.facility_zip GROUP BY r2.facility_zip,r2.activity_date ORDER BY count(r2.facility_id) ASC) as viol_diff \
               FROM (SELECT r.facility_zip FROM inspection r GROUP BY r.facility_zip) as outer \
               ORDER BY viol_diff DESC \
               LIMIT 1;")

postcode_max_diff = cursor.fetchall()
print(postcode_max_diff[0][0])                      # 90045

# Task 4:


cursor.close()
connection.close()
















