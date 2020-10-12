## 1. Complexity Zoo ##

# proposed complexities
constant_complexity  = "O(1)"
linear_complexity    = "O(N)"
quadratic_complexity = "O(N^2)"
cubic_complexity     = "O(N^3)"

# functions
def function1(N):
    for i in range(N):
        print(i)
answer1 = linear_complexity
def function2(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                print(i, j, k)
answer2 = cubic_complexity
def function3(N):
    for i in range(10000):
        print(i)
answer3 = constant_complexity
def function4(N):
    for i in range(N):
        for j in range(N):
            for k in range(10):
                print(i, j, k)
answer4 = quadratic_complexity           
def function5(N):
    for i in range(N):
        for j in range(10000):
            print(i, j)
answer5 = linear_complexity
# Add your answers below

## 2. Finding an Element in a List ##

ask(32)
ask(16)
ask(24)
ask(20)
ask(22)
ask(21)
answer(21)

## 3. Excluding Index Ranges ##

ask(10)
ask(50)
ask(30)
ask(45)
range_start = 31
range_end = 44

## 4. Binary Search ##

def binary_search(target):
    range_start = 0
    range_end = 63
    while range_start < range_end:
        range_middle = (range_end + range_start) // 2
        value = ask(range_middle)
        if value == target:
            return range_middle
        elif value < target:
            # Discard the first half of the range
            range_start = range_middle + 1
        else:
            # Discard the second half of the range
            range_end = range_middle - 1
    # At this point range_start = range_end
    return range_start 

# Add your code bellow
index_32 = binary_search(32)
answer(index_32)

## 5. Binary Search Algorithm ##

def binary_search(values, target):                     # First change
    range_start = 0
    range_end = len(values) - 1                        # Second change
    while range_start < range_end:
        range_middle = (range_end + range_start) // 2
        value = values[range_middle]                   # Third change
        if value == target:
            return range_middle
        elif value < target:
            range_start = range_middle + 1
        else:
            range_end = range_middle - 1
    if values[range_start] == target:
        return range_start
    else:
        return -1

values = [1, 2, 4, 5, 8, 10, 13, 15, 17, 20, 23, 24, 25, 26, 30, 31, 32, 36, 37, 38, 41, 42, 43, 44, 45, 47, 50, 52, 54, 55, 56, 57, 58, 59, 61, 62, 64, 66, 67, 69, 70, 73, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 90, 91, 92, 94, 95, 96, 97, 98, 99, 100]
binary_search(values, 3)

## 6. Binary Search Analysis ##

import matplotlib.pyplot as plt

def plot_list(values):
    plt.plot(values)
    plt.ylabel('number of divisions to reach 1')
    plt.xlabel('N')
    plt.margins(x=0.1, y=0.1)
    plt.show()
    
def num_div_to_reach_1(N):
    div_count = 0
    while N > 1:
        N /= 2
        div_count += 1
    return div_count

# Add your code below
num_div = []
for N in range(1000):
    num_div.append(num_div_to_reach_1(N))
plot_list(num_div)

## 8. Binary Search in Practice ##

# read the data from the CSV
import csv
with open('netflix2019.csv', mode='r') as f:
    reader = csv.reader(f)
    next(reader)
    titles = [row[1] for row in list(reader)]

# read target titles into a list
with open('target_titles.txt') as f:
    target_titles = [line.strip() for line in f.readlines()]
    
# linear search algorithm
def linear_lookup(titles, target_title):
    for title in titles:
        if title == target_title:
            return True
    return None

# binary search algorithm modified to return True or False
def binsearch_lookup(titles, target_title):
    range_start = 0                                   
    range_end = len(sorted_titles) - 1                       
    while range_start < range_end:
        range_middle = (range_end + range_start) // 2  
        title = sorted_titles[range_middle]
        if title == target_title:                            
            return True                        
        elif title < target_title:                           
            range_start = range_middle + 1             
        else:                                          
            range_end = range_middle - 1               
    if sorted_titles[range_start] != target_title:                  
        return False                                      
    return True
    
# add your code below
# titles is the list of all titles available on the CSV
# target_titles contains 5,000 titles that we want to lookup
import time

start = time.time()
for title in target_titles:
    linear_lookup(titles, title)
end = time.time()
time_linear = end - start

start = time.time()
sorted_titles = sorted(titles)
for title in target_titles:
    binsearch_lookup(sorted_titles, title)
end = time.time()
time_binsearch = end - start

print(time_linear)
print(time_binsearch)