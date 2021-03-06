## 2. Reading CSV files with NumPy Continued ##

taxi = np.genfromtxt('nyc_taxis.csv', delimiter = ',', skip_header = 1)

## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])
a_bool = (a < 3)
b_bool = (b == "blue")
c_bool = (c > 100.0)

## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

march_bool = pickup_month == 3
march = pickup_month[march_bool]
march_rides = march.shape[0]

## 5. Boolean Indexing with 2D ndarrays ##

tip_amount = taxi[:,12]
tip_bool = tip_amount > 50
top_tips = taxi[tip_bool, 5:14]

## 6. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
print(taxi_modified)
taxi_modified[28214, 5] = 1
taxi_modified[:, 0] = 16
taxi_modified[[1800, 1801], 7] = taxi_modified[:, 7].mean()
print(taxi_modified)


## 8. Assignment Using Boolean Arrays Continued ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()

# create a new column filled with `0`.
zeros = np.zeros([taxi_modified.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)

taxi_modified[taxi_modified[:, 5] == 2, 15] = 1
taxi_modified[taxi_modified[:, 5] == 3, 15] = 1
taxi_modified[taxi_modified[:, 5] == 5, 15] = 1

## 9. Challenge: Which is the most popular airport? ##

'''My first real data project'''
jfk = taxi[taxi[:, 6] == 2, :]
jfk_count = jfk.shape[0]

laguardia = taxi[taxi[:, 6] == 3, :]
laguardia_count = laguardia.shape[0]

newark = taxi[taxi[:, 6] == 5, :]
newark_count = newark.shape[0]


## 10. Challenge: Calculating Statistics for Trips on Clean Data ##

trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
cleaned_taxi = taxi[trip_mph < 100, :]
mean_distance = cleaned_taxi[:, 7].mean() 
mean_length = cleaned_taxi[:, 8].mean() 
mean_total_amount = cleaned_taxi[:, 13].mean() 
mean_mph = trip_mph[trip_mph <= 100].mean()