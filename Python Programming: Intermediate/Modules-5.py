## 1. Introduction to Modules ##

import math
root = math.sqrt(99)
flr = math.floor(89.9)

## 2. Importing Using An Alias ##

import math as m 
root = m.sqrt(33)

## 3. Importing A Specific Object ##

from math import *
root = sqrt(1001)

## 4. Variables Within Modules ##

from math import *
a = sqrt(pi)
b = ceil(pi)
c = floor(pi)