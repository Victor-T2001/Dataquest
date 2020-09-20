## 2. Introduction To The Data ##

import pandas 
unrate = pandas.read_csv('unrate.csv')
unrate['DATE'] = pandas.to_datetime(unrate['DATE'])
print(unrate.head(12))

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt
plt.plot()
plt.show()

## 7. Adding Data ##

unrate1 = unrate[:12]
unrate2 = unrate1
plt.plot(unrate1['DATE'], unrate2['VALUE'])
plt.show
  

## 8. Fixing Axis Ticks ##

unrate1 = unrate[:12]
unrate2 = unrate1
plt.plot(unrate1['DATE'], unrate2['VALUE'])
plt.xticks(rotation = 90)
plt.show()

## 9. Adding Axis Labels And A Title ##

unrate1 = unrate[:12]
unrate2 = unrate1
plt.plot(unrate1['DATE'], unrate2['VALUE'])
plt.xticks(rotation = 90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()