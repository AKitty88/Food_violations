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
cursor.execute("SELECT COUNT(*) FROM inspection WHERE activity_date >= '01/07/2015' AND activity_date <= '31/12/2017';")
sum_viol = cursor.fetchall()
print(sum_viol)

cursor.execute("SELECT facility_zip FROM inspection WHERE activity_date >= '01/07/2015' AND activity_date <= '31/12/2017';")
postcodes = cursor.fetchall()

avg_viol= []
max_viol_per_postc = 0.0001
postcode_max_viol = ''

for postc in postcodes:
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '01/07/2015' AND activity_date <= '31/12/2017') AND facility_zip=(?);", (postc[0],))
    viols_per_postc = cursor.fetchall()
    avg_viol.append((viols_per_postc[0][0] * 100) / sum_viol[0][0])
    
    if viols_per_postc[0][0] > max_viol_per_postc:
        max_viol_per_postc = viols_per_postc[0][0]
        postcode_max_viol = postc[0]                                        # POSTCODE with highest total violations
        

print(postcode_max_viol)

potcode_big_diff = ''

for postc in postcodes:
    max_viol_per_month = 0
    min_viol_per_month = 9999
    
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2015-07-01' AND activity_date <= '2015-07-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_1 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_1[0][0]:
        max_viol_per_month = viols_per_month_1[0][0]
        
    if min_viol_per_month > viols_per_month_1[0][0]:
        min_viol_per_month = viols_per_month_1[0][0]
        
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2015-08-01' AND activity_date <= '2015-08-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_2 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_2[0][0]:
        max_viol_per_month = viols_per_month_2[0][0]
        
    if min_viol_per_month > viols_per_month_2[0][0]:
        min_viol_per_month = viols_per_month_2[0][0]
        
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2015-09-01' AND activity_date <= '2015-09-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_3 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_3[0][0]:
        max_viol_per_month = viols_per_month_3[0][0]
        
    if min_viol_per_month > viols_per_month_3[0][0]:
        min_viol_per_month = viols_per_month_3[0][0]
        
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2015-10-01' AND activity_date <= '2015-10-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_4 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_4[0][0]:
        max_viol_per_month = viols_per_month_4[0][0]
        
    if min_viol_per_month > viols_per_month_4[0][0]:
        min_viol_per_month = viols_per_month_4[0][0]
        
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2015-11-01' AND activity_date <= '2015-11-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_5 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_5[0][0]:
        max_viol_per_month = viols_per_month_5[0][0]
        
    if min_viol_per_month > viols_per_month_5[0][0]:
        min_viol_per_month = viols_per_month_5[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2015-12-01' AND activity_date <= '2015-12-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_6 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_6[0][0]:
        max_viol_per_month = viols_per_month_6[0][0]
        
    if min_viol_per_month > viols_per_month_6[0][0]:
        min_viol_per_month = viols_per_month_6[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-01-01' AND activity_date <= '2016-01-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_7 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_7[0][0]:
        max_viol_per_month = viols_per_month_7[0][0]
        
    if min_viol_per_month > viols_per_month_7[0][0]:
        min_viol_per_month = viols_per_month_7[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-02-01' AND activity_date <= '2016-02-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_8 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_8[0][0]:
        max_viol_per_month = viols_per_month_8[0][0]
        
    if min_viol_per_month > viols_per_month_8[0][0]:
        min_viol_per_month = viols_per_month_8[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-03-01' AND activity_date <= '2016-03-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_9 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_9[0][0]:
        max_viol_per_month = viols_per_month_9[0][0]
        
    if min_viol_per_month > viols_per_month_9[0][0]:
        min_viol_per_month = viols_per_month_9[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-04-01' AND activity_date <= '2016-04-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_10 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_10[0][0]:
        max_viol_per_month = viols_per_month_10[0][0]
        
    if min_viol_per_month > viols_per_month_10[0][0]:
        min_viol_per_month = viols_per_month_10[0][0] 
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-05-01' AND activity_date <= '2016-05-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_11 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_11[0][0]:
        max_viol_per_month = viols_per_month_11[0][0]
        
    if min_viol_per_month > viols_per_month_11[0][0]:
        min_viol_per_month = viols_per_month_11[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-06-01' AND activity_date <= '2016-06-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_12 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_12[0][0]:
        max_viol_per_month = viols_per_month_12[0][0]
        
    if min_viol_per_month > viols_per_month_12[0][0]:
        min_viol_per_month = viols_per_month_12[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-07-01' AND activity_date <= '2016-07-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_13 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_13[0][0]:
        max_viol_per_month = viols_per_month_13[0][0]
        
    if min_viol_per_month > viols_per_month_13[0][0]:
        min_viol_per_month = viols_per_month_13[0][0]    
              
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-08-01' AND activity_date <= '2016-08-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_14 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_14[0][0]:
        max_viol_per_month = viols_per_month_14[0][0]
        
    if min_viol_per_month > viols_per_month_14[0][0]:
        min_viol_per_month = viols_per_month_14[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-09-01' AND activity_date <= '2016-09-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_15 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_15[0][0]:
        max_viol_per_month = viols_per_month_15[0][0]
        
    if min_viol_per_month > viols_per_month_15[0][0]:
        min_viol_per_month = viols_per_month_15[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-10-01' AND activity_date <= '2016-10-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_16 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_16[0][0]:
        max_viol_per_month = viols_per_month_16[0][0]
        
    if min_viol_per_month > viols_per_month_16[0][0]:
        min_viol_per_month = viols_per_month_16[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-11-01' AND activity_date <= '2016-11-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_17 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_17[0][0]:
        max_viol_per_month = viols_per_month_17[0][0]
        
    if min_viol_per_month > viols_per_month_17[0][0]:
        min_viol_per_month = viols_per_month_17[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2016-12-01' AND activity_date <= '2016-12-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_18 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_18[0][0]:
        max_viol_per_month = viols_per_month_18[0][0]
        
    if min_viol_per_month > viols_per_month_18[0][0]:
        min_viol_per_month = viols_per_month_18[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-01-01' AND activity_date <= '2017-01-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_19 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_19[0][0]:
        max_viol_per_month = viols_per_month_19[0][0]
        
    if min_viol_per_month > viols_per_month_19[0][0]:
        min_viol_per_month = viols_per_month_19[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-02-01' AND activity_date <= '2017-02-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_20 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_20[0][0]:
        max_viol_per_month = viols_per_month_20[0][0]
        
    if min_viol_per_month > viols_per_month_20[0][0]:
        min_viol_per_month = viols_per_month_20[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-03-01' AND activity_date <= '2017-03-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_21 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_21[0][0]:
        max_viol_per_month = viols_per_month_21[0][0]
        
    if min_viol_per_month > viols_per_month_21[0][0]:
        min_viol_per_month = viols_per_month_21[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-04-01' AND activity_date <= '2017-04-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_22 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_22[0][0]:
        max_viol_per_month = viols_per_month_22[0][0]
        
    if min_viol_per_month > viols_per_month_22[0][0]:
        min_viol_per_month = viols_per_month_22[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-05-01' AND activity_date <= '2017-05-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_23 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_23[0][0]:
        max_viol_per_month = viols_per_month_23[0][0]
        
    if min_viol_per_month > viols_per_month_23[0][0]:
        min_viol_per_month = viols_per_month_23[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-06-01' AND activity_date <= '2017-06-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_24 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_24[0][0]:
        max_viol_per_month = viols_per_month_24[0][0]
        
    if min_viol_per_month > viols_per_month_24[0][0]:
        min_viol_per_month = viols_per_month_24[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-07-01' AND activity_date <= '2017-07-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_25 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_25[0][0]:
        max_viol_per_month = viols_per_month_25[0][0]
        
    if min_viol_per_month > viols_per_month_25[0][0]:
        min_viol_per_month = viols_per_month_25[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-08-01' AND activity_date <= '2017-08-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_26 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_26[0][0]:
        max_viol_per_month = viols_per_month_26[0][0]
        
    if min_viol_per_month > viols_per_month_26[0][0]:
        min_viol_per_month = viols_per_month_26[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-09-01' AND activity_date <= '2017-09-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_27 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_27[0][0]:
        max_viol_per_month = viols_per_month_27[0][0]
        
    if min_viol_per_month > viols_per_month_27[0][0]:
        min_viol_per_month = viols_per_month_27[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-10-01' AND activity_date <= '2017-10-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_28 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_28[0][0]:
        max_viol_per_month = viols_per_month_28[0][0]
        
    if min_viol_per_month > viols_per_month_28[0][0]:
        min_viol_per_month = viols_per_month_28[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-11-01' AND activity_date <= '2017-11-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_29 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_29[0][0]:
        max_viol_per_month = viols_per_month_29[0][0]
        
    if min_viol_per_month > viols_per_month_29[0][0]:
        min_viol_per_month = viols_per_month_29[0][0]
                
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2017-12-01' AND activity_date <= '2017-12-31') AND facility_zip=(?);", (postc[0],))
    viols_per_month_30 = cursor.fetchall()
    
    if max_viol_per_month < viols_per_month_30[0][0]:
        max_viol_per_month = viols_per_month_30[0][0]
        
    if min_viol_per_month > viols_per_month_30[0][0]:
        min_viol_per_month = viols_per_month_30[0][0]
    
    print(max_viol_per_month)
    print(min_viol_per_month)
    print("----------------")
    
print(max_viol_per_month)
print(min_viol_per_month)
cursor.close()
connection.close()
















