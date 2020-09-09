## 1. Overview ##

f = open("movie_metadata.csv", 'r')
file = f.read()
rows = file.split('\n')
movie_data = []
for row in rows:
    split = row.split(',')
    movie_data.append(split)
print(movie_data[0:2])
print(rows[0:2])

## 3. Writing Our Own Functions ##

def movie(movie_data):
    alist = []
    for item in movie_data:
        alist.append(item[0])
    return alist
movie_names = movie(movie_data)
print(movie_names[0:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]
def is_usa(data):
    for item in data:
        if item == 'USA':
            return True
wonder_woman_usa = is_usa(wonder_woman)
    

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]
def index_equals_str(list, index, string):
    if list[index] == string:
        return True
    else:
        return False
wonder_woman_in_color = index_equals_str(string = 'Color', list = wonder_woman, index = 2)
print(wonder_woman_in_color)
    

## 6. Optional Arguments ##

def feature_counter(input_lst, index, input_str, header_row):
    counter=0
    if header_row==True:
        input_lst=input_lst[1:len(input_lst)]
    for element in input_lst:
        if element[index]==input_str:
            counter+=1
    return counter
print(feature_counter(movie_data, 6, 'USA', True))

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str):
    num = 0
    for each in input_lst:
        if each[index-1] == input_str:
            num = num + 1
    return num

def summary_statistics(movie_data):
    movie_data = movie_data[1:len(movie_data)]
    num_japan_films=feature_counter(movie_data, 7, 'Japan')
    num_color_films=feature_counter(movie_data, 3, 'Color')
    num_films_in_english=feature_counter(movie_data, 6, 'English')
    dictionary={'japan_films':num_japan_films, 'color_films':num_color_films, 'films_in_english':num_films_in_english}
    return dictionary

summary = summary_statistics(movie_data)