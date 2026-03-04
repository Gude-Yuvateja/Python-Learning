## TYPES

# type(value)
x = 5
y = 1.5
z = 1+3j
print(type(x))
print(type(y))
print(type(z))

# int(value)
x = "23"
x = int(x)
print(type(x))
print(x * 4)

# float(value)
x = 3
print(float(x))

x = "3"
print(float(x))

# complex(real, img)
x = 4 # real 
y = 5 # imaginary
print(complex(x,y))


## MATH OPERATORS

# addition  ## +
print(3 + 4)

x = 3
x += 4
print(x)       ## shortcuts of operators

# subbraction  ## -
print(3 - 4)

x = 3
x -= 4
print(x)      ## shortcuts of operators

# multipication  ## *
print(3 * 4)       

x = 3
x *= 4
print(x)      ## shortcuts of operators

# division  ## /
print(3 / 4)

x = 3
x /= 4
print(x)      ## shortcuts of operators

# floor division  ## //
print(3 // 4)

x = 3
x //= 4
print(x)     ## shortcuts of operators

# remainder  ## %
print(3 % 4)

x = 3
x %= 4
print(x)     ## shortcuts of operators

# exponentiation  ## **
print(3 ** 4)

x = 3
x **= 4
print(x)    ## shortcuts of operators


## ROUNDING

# abs(value)
print(abs(3-7))

# round(value)
price = 36.5457
print(round(price)) 
print(round(price,2))
print(round(price,4))


## MATH 

# floor(), ceil(), trunc()
import math
price = 36.5457
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))

## ADVANCED MATH

# sqrt(), sin(), cos(), log()
import math
number = 100
print(math.sqrt(number))
print(math.sin(number))
print(math.cos(number))
print(math.log(number))


## RANDOM

# random(), randint()
import random
print(random.random())
print(random.randint(1,8))


## VALIDATION

# is_integer()
x = 8.0
y = 9.40
print(x.is_integer())
print(y.is_integer())

# isinstance(value,type)
x = 7
y = 7.1
print(isinstance(x, int))
print(isinstance(y, int))
print(isinstance(y, float))