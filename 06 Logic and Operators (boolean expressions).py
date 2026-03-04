## BOOLEAN EXPRESSIONS

## VALUE

# True, False
print(True)
print(False)
print(type(True))
print(type(False))


## FUNCTIONS

# bool(value)
print(bool(123))
print(bool("hi"))
print(bool())
print(bool(0))
print(bool(None))

# any(), all()
email = ""
phone = "7981524920"
name = " "
print(any([email, phone, name]))
print(all([email, phone, name]))

email = ""
phone = ""
name = ""
print(any([email, phone, name]))
print(all([email, phone, name]))

email = "name@gmail.com"
phone = "7981524920"
name = "Teja"
print(any([email, phone, name]))
print(all([email, phone, name]))

# isinstance(value, type)
print(isinstance(1223, int))
print(isinstance(True, str))


## COMPARISON OPERATORS

# ==  ## equal to
print(1 == 2)
print(1 == 1)
print("A" == "a")
print(" " == "")

# !=   ## not equal
print(1 != 3)
print(1 != 1)
print("A" != "a")
print("a" != "")

# <   ## less than
print(1 < 4)
print(1 < 3 < 5)
print(4 < 1)

# <=   ## less than or equal
print(1 <= 1)
print(1 <= 4 <= 4)
print(3 <= 3 <= 6)

# >   ## greater than
print(4 > 2)
print(4 > 3 > 4)
print(7 > 5 > 3 > 1)

# >=   ## greater than or equal
print(1 >= 1)
print(7 >= 4 >= 4)
print(7 >= 7 >= 7)
print(4 >= 5 >= 5)


## LOGICAL OPERATORS

# and
print(3 < 1 and 5 > 1)
print(3 > 1 and 5 > 1)

# or
print(3 > 1 or 5 > 1)
print(3 > 1 or 5 < 1)
print(3 < 1 or 5 < 1)

# not
print(not 3 > 2)
print(not True)
print(not False)


## MEMBERSHIP OPERATORS

# in AND not in 
print("m" in "python")
print("m" not in "python")
print(4 in [1,2,3,4])
print(3 not in [1,2,3,4])


## IDENTITY OPERATORS

# is AND is not
x = ["a", "b", "c"]
y = ["a", "b", "c"]
print(x == y)
print(x is y)
print(x is not y)

x = 10
y = 10
print(x == y)
print(x is y)
print(x is not y)