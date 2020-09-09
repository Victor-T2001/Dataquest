## 2. Sets ##

gender = []
for item in legislators:
    gender.append(item[3])
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

party= []
for item in legislators:
    party.append(item[6])
party = set(party)
print(party)
print(legislators[0:3])

## 4. Missing Values ##

gender =[]
for item in legislators:
    if item[3] == "":
        item[3] = "M"
    gender.append(item[3])
        

## 5. Parsing Birth Years ##

birth_years = []
for item in legislators:
    parts = item[2].split("-")
    birth_years.append(parts[0])

## 6. Try/except Blocks ##

try:
    float('hello')
except:
    print("Error converting to float.")

## 7. Exception Instances ##

try:
    int(" ")
except Exception as exp:
    print(type(exp))
    print(str(exp))
    

## 8. The Pass Keyword ##

converted_years = []
for year in birth_years:
    try:
        int_year = int(year)
        converted_years.append(int_year)
    except:
        pass

## 9. Convert Birth Years to Integers ##

for item in legislators:
    birthday = item[2]
    birth_year = birthday.split("-")[0]
    try:
        birth_year = int(birth_year)
    except:
        birth_year = 0
    item.append(birth_year)
print(legislators[0:3])

## 10. Fill in Years Without a Value ##

last_value = 1
for item in legislators:
    if item[7] == 0:
        item[7] = last_value
    last_value = item[7]