## 1. Fixed Bit Integers ##

import numpy as np
x = np.int8(100)
y = np.int8(28)
z = x+y
print(z)

## 2. Two's Complement Representation ##

x = -2
y = -6
z = 6

## 3. Range of Two's Complement ##

import numpy as np
print(numpy.binary_repr(-2147483648, width=32))
print(numpy.binary_repr(2147483647, width=32))

## 4. Why Two's Complement ##

import sys
num_bytes = sys.getsizeof(2147483647)
num_mb = 1000000000*32/1000000

## 5. Identifying the Number of Bits ##

def minimum_required_bits(list_of_integers):
    min_req_bits = 0 
    for value in list_of_integers:
        nb_bits = int.bit_length(value)
        min_req_bits = max(min_req_bits, nb_bits)
    return min_req_bits

with open("identifiers.txt") as file:
    list_of_strings = list(file)
    list_of_integers = [int(x) for x in list_of_strings]
    print(minimum_required_bits(list_of_integers))

## 6. Memory Consumption of Textual Data ##

import sys
s = "你"
size_s = sys.getsizeof(s)
size_ss = sys.getsizeof(s+s)

## 7. Python Internal String Representation ##

import sys
message = "I really like learning about Python! 🐍\n Me too! 😀😀\n I can't wait to see what we will learn in the next course 🙃\n"

message_latin_bytes = message.encode(encoding = 'Latin-1', errors='ignore')
cleaned_message = message_latin_bytes.decode(encoding = 'Latin-1')
message_size = sys.getsizeof(message)
cleaned_message_size = sys.getsizeof(cleaned_message)

## 8. Disk Consumption of Textual Data ##

import os
messages = "I really like learning about Python! 🐍\n Me too! 😀😀\n I can't wait to see what we will learn in the next course 🙃\n"

with open('utf8.txt', encoding = 'utf8', mode='w') as file:
    file.write(messages)
    
size_utf8 = os.path.getsize('utf8.txt')

with open('utf32.txt', encoding = 'utf32', mode='w') as file:
    file.write(messages)
    
size_utf32 = os.path.getsize('utf32.txt')

## 9. Estimating the Disk Requirements ##

num_days_in_a_year = 356
num_years = 20
bytes_per_char = 32 / 8
num_transactions = 1000000
username_size = 20
product_name_size = 50

num_gb = (num_years*num_days_in_a_year*num_transactions*(product_name_size+2*username_size)*bytes_per_char)/10**9