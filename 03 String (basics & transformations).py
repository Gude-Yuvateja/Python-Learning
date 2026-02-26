## TYPES

# type(value)
name = "teja"
print(type(name))

age =  23
print(type(age))


# str(value)
age = 23
print(type(age))
print("Your age is :" + str(age))
print(age + 5)



## MATH

# len(value)
password = "Yuvi"
print(len(password))

if len(password) < 8 :
    print("Your password is to short!")

password = "Yuvi@1870"
print(len(password))

if len(password) < 8 :
    print("Your password is to short!")


# count(substring)
text = """"
Python is easy to learn.
Python is powerful.
Many people love Python.
"""
print(text.count("Python"))



## TRANSFORMATIONS

# replace(old, new)
price = "1234,56"
print(price.replace(",", "."))
print(type(price))

phone = "798-152-4920"
print(phone.replace("-", "/"))

phone = "798-152-4920"
print(phone.replace("-", ""))

price = "$1,234.56"
print(price.replace("$", "").replace(",", ""))

# task
phone = "+49 (176) 123-4567"  # Answer : 00491761234567
print(phone.replace("+", "00").replace(" ", "").replace("-", "").replace("(", "").replace(")",""))


# 'string' + 'string' ##(joins)
First_Name = "Yuva"
Last_Name =  "Teja"
Full_Name = First_Name + " " + Last_Name
print(Full_Name)

folder = "c:/Users/teja/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)


# f{} ## f-string
name ="teja"
age = "23"
is_student = False
# print(My name is name , I am age years old, and student status is is_student.)
print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + ".") # str method
print(f"my name is {name}, I am {age} years old, and student status is {is_student}.")  # f-string

print(f"2 + 4 = {2 + 4}")

print(f"{{this is me}}")


# split(separator)
stamp = "2026-02-26 06:52"
print(stamp.split(" "))

stamp = "2026-02-26"
print(stamp.split("-"))

csv_file = "1234,Max,USA,2026-02-26,M"
print(csv_file.split(","))


# 'string' * number ## string repetation
print("ha" * 3)
print("=" * 20)


# Index  ## Extraction
text = "python"

# Extract the first character
print(text[0])
print(text[-6])

# Extract the last character
print(text[5])
print(text[-1])

# Extract h
print(text[3])
print(text[-3])


# slicing ## Extraction
date = "2026-02-26"

# Extract the year
print(date[0:4])
print(date[:4])

# Extract the month
print(date[5:7])

# Extract the day
print(date[8:10])
print(date[8:])