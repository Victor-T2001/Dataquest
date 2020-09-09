## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i, item in enumerate(ships):
    print(item)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i, item in enumerate(things):
    item.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled =[x*2 for x in apple_prices]
apple_prices_lowered = [x-100 for x in apple_prices]

## 5. Counting Female Names ##

name_counts = {}
for item in legislators:
    if item[3] == 'F' and item[7] > 1940:
        name  = item[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
for value in values:
    checks.append(value != None and value>30)
       

## 8. Highest Female Name Count ##

max_value =None
for key in name_counts:
    count = name_counts[key]
    if max_value == None or count>max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for item in plant_types.items():
    print(item[0])
    print(item[1])
    
for k, v in plant_types.items():
    print(k)
    print(v)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for k, v in name_counts.items():
    if v == 2:
        top_female_names.append(k)
        
top_female_names = [k for k, v in name_counts.items() if v == 2]

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts = {}
for item in legislators:
    if item[3] == 'M' and item[7] > 1940:
        name = item[1]
        if name in male_name_counts:
            male_name_counts[name] = male_name_counts[name] + 1
        else:
            male_name_counts[name] = 1
            
highest_male_count = 0
for k, v in male_name_counts.items():
    if v > highest_male_count:
        highest_male_count = v
        
for k, v in male_name_counts.items():
    if highest_male_count == v:
        top_male_names.append(k)