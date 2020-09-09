## 2. Parsing the File ##

weather_data = []
f = open("la_weather.csv", "r")
a = f.read()
a_list = a.split('\n')
for element  in a_list:
    split = element.split(',')
    weather_data.append(split)
print(a_list[1:5])
print(weather_data[1:5])

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for item in weather_data:
    value = item[1]
    weather.append(value)

## 4. Counting the Items in a List ##

count = 0
for item in weather:
    count += 1

## 5. Removing the Header ##

new_weather = weather[1:366]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = 'space_monster' in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for item in weather_types:
    value = item in new_weather
    weather_type_found.append(value)
     