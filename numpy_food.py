import sqlite3
from sqlite3 import Error
import numpy as np
import matplotlib.pyplot as plt
#import datetime
import re

try:
    connection = sqlite3.connect("Food_violations.db")
    print("Food_violations.db connected")
except Error as e:
    connection.close()
    print(e)
  
cursor = connection.cursor()
    
# =============================================================================
# # Task 1:
# cursor.execute("SELECT COUNT(*) FROM inspection WHERE activity_date >= '2015-07-01' AND activity_date <= '2017-12-31';")
# sum_viol = cursor.fetchall()
# print(sum_viol)                                                               # 44.031
# 
# cursor.execute("SELECT facility_zip FROM inspection WHERE activity_date >= '2015-07-01' AND activity_date <= '2017-12-31';")
# postcodes = cursor.fetchall()
# 
# avg_viol_postc= []
# max_viol_per_postc = 0.0001
# postcode_max_viol = ''
# 
# for postc in postcodes:
#     cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2015-07-01' AND activity_date <= '2017-12-31') AND facility_zip=(?);", (postc[0],))
#     viols_per_postc = cursor.fetchall()
#     avg_viol_postc.append((viols_per_postc[0][0] * 100) / sum_viol[0][0])       # 44.031 values in avg_viol_postc around 0.40
# =============================================================================

# =============================================================================
# # Task 2:
#     if viols_per_postc[0][0] > max_viol_per_postc:
#         max_viol_per_postc = viols_per_postc[0][0]
#         postcode_max_viol = postc[0]                                          # POSTCODE with highest total violations: 91748
# print(postcode_max_viol)
# =============================================================================

# =============================================================================
# # Task 3:
# cursor.execute("SELECT outer.facility_zip, \
#                (SELECT count(i.facility_id) from inspection i WHERE outer.facility_zip=i.facility_zip AND (datetime(activity_date) BETWEEN datetime('2015-07-01') AND datetime('2017-12-31')) GROUP BY i.facility_zip, strftime('%Y-%m',i.activity_date) ORDER BY count(i.facility_id) DESC) \
#                - (SELECT count(i.facility_id) from inspection i WHERE outer.facility_zip=i.facility_zip AND (datetime(activity_date) BETWEEN datetime('2015-07-01') AND datetime('2017-12-31')) GROUP BY i.facility_zip, i.activity_date ORDER BY count(i.facility_id) ASC) as viol_diff \
#                FROM (SELECT ins.facility_zip FROM inspection ins GROUP BY ins.facility_zip) as outer \
#                ORDER BY viol_diff DESC \
#                LIMIT 1;")
# 
# postcode_max_diff = cursor.fetchall()
# print(postcode_max_diff[0][0])                                                # 90045 
# =============================================================================

# =============================================================================
# # Task 4:
# cursor.execute("SELECT substr(activity_date,1,7) AS date, count(*) AS number_of_violence \
#                FROM inspection \
#                WHERE datetime(activity_date) BETWEEN datetime('2015-07-01') AND datetime('2017-12-31') \
#                GROUP BY substr(datetime(activity_date),1,7);")
# viols_per_months = cursor.fetchall()                                                        # around 1500
# =============================================================================

# Task 5:
cursor.execute("SELECT DISTINCT violation_code, violation_description FROM violation;")
viol_code_descr = cursor.fetchall()

# Task 6:
#food_words = re.search("food", viol_code_descr)

for word in viol_code_descr:
    for wo in word:
        prog = re.compile("food")
        food_words = prog.search(wo)
    
    if food_words:
        print(food_words)

cursor.close()
connection.close()
















