## DATA STRUCTURE

## list []

## BASICS

## how to create?

# create lists
empty = []
print(empty)
print(type(empty))

letters = ['a', 'b', 'c']
print(letters)
print(type(letters))

numbers = [1, 2, 3]
print(numbers)
print(type(numbers))

mixed = ['a', 1, True, None]
print(mixed)
print(type(mixed))

# list(value)
empty = list()
print(empty)

letters = list('python')
print(letters)

numbers = list(range(5))
print(numbers)

# nested list matrix 
matrix = [['a', 'b', 'c'],
          ['d', 'e', 'f']]
print(matrix)
print(type(matrix))

mixed_matrix = [['a', 'b', 'c'],
          [1, 2, 3],
          [True]]
print(mixed_matrix)
print(type(mixed_matrix))


## how to access and read?

# access and read
# indexing
lst = ['a', 'b', 'c', 'd']
print(lst)

lst = ['a', 'b', 'c', 'd']
print(lst[0])
print(lst[-1])
print(lst[2])

# nested list matrix 
matrix = [['a', 'b', 'c'],
          ['d', 'e', 'f'],
          ['g', 'h', 'i']]
print(matrix)
print(matrix[1])
print(matrix[1][-1])
print(matrix[1][1])
print(matrix[1][0])

# slicing
lst = ['a', 'b', 'c', 'd']
print(lst[:2])
print(lst[2:-1])
print(lst[1:2])

# nested list matrix 
matrix = [['a', 'b', 'c'],
          ['d', 'e', 'f'],
          ['g', 'h', 'i']]
print(matrix[:2])
print(matrix[1:2])
print(matrix[2][1:3])
print(matrix[2][1:2])


## how to unpack?

# unpacking lists
person = ['Teja', 23, 'Data Engineer', 'India']
name, age, role, country = person
print(role)
print(name)
print(age)
print(country)

# asterisk *
person = ['Teja', 23, 'Data Engineer', 'India']
name, *details, country = person
print(details)
print(name)
print(country)

person = ['Teja', 23, 'Data Engineer', 'India']
name, *details = person
print(name)
print(details)

# skipping items using underscore "_"
person = ['Teja', 23, 'Data Engineer', 'India']
name, _, role, _ = person 
print( name)
print(role)

person = ['Teja', 23, 'Data Engineer', 'India']
name, *_, country = person 
print( name)
print(country)


## how to explore and analyze?

# Analyze
numbers = [1, 5, 3, 7, 2, 9]
print("Max :", max(numbers))    # Max()
print("Min :", min(numbers))    # Min()
print("Sum :", sum(numbers))    # Sum()
print("length :", len(numbers))

# completeness of existence check
# all()
print("All :", all(numbers))
print("All :", all([1, 2, 3]))
print("All :", all([3, 0, 5]))
print("All :", all(['']))
print("All :", all([' ']))

# any
print("Any :", any(numbers))
print("Any :", any([1, 2, 3]))
print("Any :", any([3, 0, 5]))
print("Any :", any(['']))
print("Any :", any([' ']))

# search and count
numbers = [1, 5, 5, 4, 5, 3]
print("Count :", numbers.count(5))
print("Index :", numbers.index(5))
print("Index :", numbers.index(4))

# membership and identity
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
print(4 in x)
print(4 in y)
print(5 in x)
print(x is y)

# comparsion
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
print(x == y)
print(x > y)


## how to change?

# adding items
# .append()
letters = ['A', 'B', 'C', 'D']
letters.append('X')
letters.append('Y')
print(letters)

# .insert()
letters = ['A', 'B', 'C', 'D']
letters.insert(0,'F')
letters.insert(3,'G')
print(letters)

# matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrix.append([10, 11, 12])
print(matrix)
matrix.insert(1,[3, 4, 5])
print(matrix)

# removing items 
# .clear()
letters = ['A', 'B', 'C', 'D']
letters.clear()
print(letters)

# .remove()
letters = ['A', 'B', 'C', 'A']
letters.remove('A')
print(letters)

# .pop()
letters = ['A', 'B', 'C', 'C']
letters.pop(2)
print(letters)

# matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrix.remove([1, 2, 3])
matrix[1].remove(7)
matrix[-2].remove(5)
print(matrix)

# updating items
letters = ['a', 'b', 'c']
letters[0] = 'x'
letters[1] = 'y'
print(letters)
print(type(letters)) 

# matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
matrix[1] = [5, 6, 7]
matrix[0][0] = '-'
matrix[1][1] = 'e'
print(matrix)


## how to sort?

# sorting
# .sort()
letters = ['d', 'a', 'e', 'b', 'c']
letters.sort()
print(letters)

# .sort(reverse = True)
letters = ['d', 'a', 'e', 'b', 'c']
letters.sort(reverse = True)
print(letters)

# matrix
letters = [['d', 'e', 'f'],
           ['a', 'b', 'c'],
           ['g', 'h', 'i']]
letters.sort()
print(letters)
letters.sort(reverse = True)
print(letters)

# .reverse()
letters = ['d', 'a', 'e', 'b', 'c']
letters.reverse()
print(letters)


## how to copy?

# copying
# assignement =
letters = ['a', 'd', 'c', 'e', 'b']
copy_letters = letters
copy_letters.append('z')
letters.pop()
print('orginal =', letters)
print('copy =', copy_letters)

# .copy()        # shadow copy
letters = ['a', 'd', 'c', 'e', 'b']
copy_letters = letters.copy()
letters.pop()
copy_letters.append('z')
print('orginal =', letters)
print('copy =', copy_letters)

# copy.deepcopy()
import copy
letters = [['a', 'd'], 
           ['c', 'e']]
copy_letters = copy.deepcopy(letters)
letters.pop()
copy_letters[0].append('z')
print('orginal =', letters)
print('copy =', copy_letters)


## how to combine?

# combining lists
# new list
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
comb = letters + numbers
print(comb)

# new nested list
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
comb = [letters, numbers]
print(comb) 

# .extend()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
numbers.extend(letters)
print(letters)
print(numbers) 

# zip()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
comb = list(zip(letters, numbers))
print(comb)


## ADAVANCED

## iterator

## how to iterate?

# iterable
letters = ['a', 'b', 'c']
for l in letters :
    print(l)    
    print(l.upper())
# using for loop to add new list
letters = ['a', 'b', 'c']
new_list =[]
for l in letters :  
    new_list.append(l.upper())
    print(new_list)

# enumerate()
letters = ['a', 'b', 'c']
print(list(enumerate(letters)))
print(list(enumerate(letters, start = 1)))
# using for loop
for index, value in enumerate(letters) :
    print(index, value)

# reversed()
letters = ['a', 'b', 'c']
print(list(reversed(letters)))
# using for loop 
for l in reversed(letters) :
    print(l)

# zip()
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
print(list(zip(letters, numbers)))
# using for loop
for l, n in zip(letters, numbers) :
    print(l, n)


## how to transform?

# transformation
# map()
letters = ['a', 'b', 'c']
print(list(map(str.upper, letters)))

numbers = ['1', '2', '3']
print(list(map(int, numbers)))

names = [' Teja', '   Yuva    ', 'Sai             ']
print(list(map(str.strip, names)))
# using for loop
for n in map(str.strip, names) :
    print(n)


## how to filter?

# filter
letters = ['a', '', 'b', None, 'c', False, 'd']
print(list(filter(None, letters)))
print(list(filter(bool, letters)))

items = ['sql', '123', 'python', '3245', 'Excel']
print(list(filter(str.isalpha, items)))
# using fot loop
for i in filter(str.isalpha, items) :
    print(i)


## Lambda function 
# basics
multiple = lambda x : x*2
print(multiple(2))

add = lambda x, y : x + y
print(add(11, 33))

check = lambda i : i in "python"
print(check('z'))
print(check('o'))
print(check('py'))

# lambda + map
prices = ['$12.50', '$9.99', '$100.00']
print(list(map(lambda p : float(p.replace('$', '')), prices)))
# using for loop
for p in map(lambda p : float(p.replace('$', '')), prices) :
    print(p)

# lambda + filter
prices = [120, 30, 300, 40, 80]
print(list(filter(lambda p : p >= 100, prices)))
## TASK
students = [['Teja', 80],
            ['Sai', 70],
            ['Arun', 60]]
print(list(filter(lambda row : row[1] >= 70, students)))
 

## list comprehension?

# data tranformation, loop and filter
domains = ['www.google.com',
          'openai.com',
          'localhost',
          'www.YUVATEJA.com']
cleaned = [
    d.lower().replace('www.', '')
    for d in domains
    if '.' in d
]
print(cleaned)