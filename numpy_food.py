import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as plt
import re

try:
    connection = sqlite3.connect("Food_violations.db")
    print("Food_violations.db connected")
except Error as e:
    connection.close()
    print(e)
  
cursor = connection.cursor()
    
# Task 1:
cursor.execute("SELECT COUNT(*) FROM inspection WHERE activity_date >= '2015-07-01' AND activity_date <= '2017-12-31';")
sum_viol = cursor.fetchall()
print(sum_viol)                                                               # 191.371

cursor.execute("SELECT facility_zip FROM inspection WHERE activity_date >= '2015-07-01' AND activity_date <= '2017-12-31';")
postcodes = cursor.fetchall()

avg_viol_postc= []
max_viol_per_postc = 0.0001
postcode_max_viol = ''

for postc in postcodes:
    cursor.execute("SELECT COUNT(*) FROM inspection WHERE (activity_date >= '2015-07-01' AND activity_date <= '2017-12-31') AND facility_zip=(?);", (postc[0],))
    viols_per_postc = cursor.fetchall()
    avg_viol_postc.append((viols_per_postc[0][0] * 100) / sum_viol[0][0])     # 5.753 values in avg_viol_postc around 0.40

# Task 2: Postcode with highest total violations
    
    if viols_per_postc[0][0] > max_viol_per_postc:
        max_viol_per_postc = viols_per_postc[0][0]
        postcode_max_viol = postc[0]                                          # 90012

cursor.execute("SELECT substr(activity_date,1,7) AS date, count(*) AS number_of_violence \
                FROM inspection \
                WHERE (datetime(activity_date) BETWEEN datetime('2015-07-01') AND datetime('2017-12-31')) AND facility_zip=(?) \
                GROUP BY substr(datetime(activity_date),1,7);", (postcode_max_viol,))
number_viol_highest_viol = cursor.fetchall()

months = []
numb_of_viol = []

for (m,c) in number_viol_highest_viol:
    months.append(m)
    numb_of_viol.append(c)

plt.figure()
plt.plot(months, numb_of_viol)
plt.title("Monthly violations for the postcode with highest total violations") 
plt.ylabel("Number of violations") 
plt.xlabel("Year")
plt.show()

# Task 3: postcode with the greatest variance

cursor.execute("SELECT outer.facility_zip, \
               (SELECT count(i.facility_id) from inspection i WHERE outer.facility_zip=i.facility_zip AND (datetime(activity_date) BETWEEN datetime('2015-07-01') AND datetime('2017-12-31')) GROUP BY i.facility_zip, strftime('%Y-%m',i.activity_date) ORDER BY count(i.facility_id) DESC) \
               - (SELECT count(i.facility_id) from inspection i WHERE outer.facility_zip=i.facility_zip AND (datetime(activity_date) BETWEEN datetime('2015-07-01') AND datetime('2017-12-31')) GROUP BY i.facility_zip, i.activity_date ORDER BY count(i.facility_id) ASC) as viol_diff \
               FROM (SELECT ins.facility_zip FROM inspection ins GROUP BY ins.facility_zip) as outer \
               ORDER BY viol_diff DESC \
               LIMIT 1;")
 
postcode_max_diff = cursor.fetchall()
#print(postcode_max_diff[0][0])                                                # 90045 

cursor.execute("SELECT substr(activity_date,1,7) AS date, count(*) AS number_of_violence \
                FROM inspection \
                WHERE (datetime(activity_date) BETWEEN datetime('2015-07-01') AND datetime('2017-12-31')) AND facility_zip=(?) \
                GROUP BY substr(datetime(activity_date),1,7);", (postcode_max_diff[0][0],))
number_viol_grea_var = cursor.fetchall()

months = []
numb_of_viol = []

for (m,c) in number_viol_grea_var:
    months.append(m)
    numb_of_viol.append(c)

plt.figure()
plt.plot(months, numb_of_viol)
plt.title("Monthly violations for the postcode with the greatest variance") 
plt.ylabel("Number of violations") 
plt.xlabel("Year")
plt.show()

# Task 4: average violations per months
cursor.execute("SELECT substr(activity_date,1,7) AS date, count(*) AS number_of_violence \
               FROM inspection \
               WHERE datetime(activity_date) BETWEEN datetime('2015-07-01') AND datetime('2017-12-31') \
               GROUP BY substr(datetime(activity_date),1,7);")
viols_per_months = cursor.fetchall()                                                        # around 6000

months = []
numb_of_viol = []
avg_viol = []

for (m,c) in viols_per_months:
    months.append(m)
    avg_viol.append(int(c * 100) / int(sum_viol[0][0]))

plt.figure()
plt.plot(months, avg_viol)
plt.title("Monthly average violations for all the postcodes") 
plt.ylabel("Number of violations") 
plt.xlabel("Year")
plt.show()

# Task 5:
cursor.execute("SELECT DISTINCT violation_code, violation_description FROM violation;")
viol_code_descr = cursor.fetchall()

# Task 6:
for word in viol_code_descr:
    for wo in word:
        prog = re.compile("food")
        food_words = prog.search(wo)
        
        if food_words:
            print(wo)
            print (word[0])
            print()

cursor.close()
connection.close()
















