# Data type

a = 10      # int

b = 3.14    # float

c = "Hello" # Str
d = 'Hi'    # str 
e = "123"   # str 

f = True    # bool
g = False   # bool

h = None    # Nonetype

i = ""      # str - Blank
j = " "     # str - Empty space



text = "hi"
number = 50

# Print()
print(text)
print(number)

# type()
print(type(text))
print(type(number))

# len()
print(len(text))
# print(len(number))  its not work because len is in number

# upper() 
print(text.upper())
# print(number.upper())  its not work because number is no upper case

# lower() 
print(text.lower())
# print(number.lower())  its not work because number is no lower case

# bit_length()
# print(text.bit_length())  its not work because its not a number
print(number.bit_length())