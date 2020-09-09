## 1. Opening Files ##

f = open("crime_rates.csv", "r")

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()

## 3. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:6])

## 5. Practice - Loops ##

ten_rows = rows[0:10]
for i in range(0, 10):
    print(rows[i])

## 6. List of Lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

## 7. Practice - Splitting Elements in a List ##

final_data = []
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_list = row.split(',')
    final_data.append(split_list)
print(final_data[0:5])

## 8. Accessing Elements in a List of Lists: The Manual Way ##

n = 0
cities_list = []
print(five_elements)
for i in range (0, 5):
    #n = n + 2*i
    cities_list.append(five_elements[i][0])

## 9. Looping Through a List of Lists ##

cities_list = []

for row in final_data:
    # row is a list variable, not a string.
    cities = row[0]
    # crime_rate is a string, the crime rate of the city.
    cities_list.append(cities)

## 10. Challenge ##

int_crime_rates = []
data = []
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split = row.split(',')
    int_crime_rates.append(int(split[1]))
    
    
