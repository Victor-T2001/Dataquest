## 2. Introduction to the Data ##

import csv
f = open('nfl_suspensions_data.csv')
nfl_suspensions = list(csv.reader(f))

nfl_suspensions = nfl_suspensions[1::]

years = {}  
for item in nfl_suspensions:
    name = item[5]
    if name in years:
        years[name] += 1
    else:
        years[name] = 1
        
print(years)
        
    

