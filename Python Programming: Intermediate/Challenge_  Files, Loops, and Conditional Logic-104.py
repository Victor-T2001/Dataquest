## 3. Read the File Into a String ##

s = open("dq_unisex_names.csv", 'r')
names = s.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = []
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
comma_list = []
for i in range(0, len(names_list)):
    c = names_list[i].split(",")
    comma_list.append(c)
for i in range(0, len(comma_list)):
    nested_list.append(comma_list[i])
print(nested_list)


## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list = []
for i in range(0, len(nested_list)):
    a = nested_list[i][0] 
    b = float(nested_list[i][1])
    beta_list = []
    beta_list.append(a)
    beta_list.append(b)
    numerical_list.append(beta_list)
print(numerical_list[0:5])

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for i in range(0, len(numerical_list)):
    if numerical_list[i][1] >= 1000:
        thousand_or_greater.append(numerical_list[i][0])
print(thousand_or_greater[0:10])