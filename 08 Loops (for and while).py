## LOOPS

##  for loop (basic) 

# using with tuple
for i in (1,2,3,4,5) :
    print(f"Round : {i}")

items = (1,2,3,4,5)
for item in items :
    print(f"Round : {item}")

# using with list
for i in [1,2,3,4,5,"hi"] :
    print(i)

for i in [1,2,3,4,5,"hi"] :
    print(f"Round : {i}")

items = [1,2,3,4,5,"Hi"]
for item in items :
    print(f"Round : {item}")

# using with string
for i in "Python" :
    print(i)

for i in "python" :
    print(f"Round : {i}")

items = " python"
for item in items :
    print(f"Round : {item}")

# using with range
for i in range(4) :
    print(i)

for i in range(5) :
    print(f"Round : {i}")

items = range(6)
for item in items :
    print(f"Round : {item}")

items = range(5,9)
for item in items :
    print(f"Round : {item}")

items = range(1,12,3)
for item in items :
    print(f"Round : {item}")


# aggregation (like : sum, count and average)
scores =  [80,50,40,90]
total = 0
for score in scores :
    total += score
    print("Current total :", total)
print("Final total :", total)


# transform data 
files = ['Report.csv', 'Data.csv', 'Final.txt']
for file in files :
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"processing {file}")

# Task
for i in range(1,11) :
    print("7 x", i, "=", 7*i)

for i in range(1,11) :
    print("8 x", i, "=", 8*i)

for i in range(1,7) :
    print("*" *i)

print()

for i in range(6,0,-1) :
    print("*" *i)


## for loop control statements (Advanced loop)

# break statement
for i in (1,2,3,4,5) :
    if i == 4 :
        break
    print(i)

names = ['Teja', '', 'Sai', 'Navya']
for name in names :
    if name == '' :
        print("Empty value detected!")
        break
    print(f"name = {name}")

names = ['Teja', 'Sai', '', 'Navya']
for name in names :
    if name == '' :
        print("Empty value detected!")
        break
    print(f"name = {name}")

# continue statement
for i in (1,2,3,4) :
    if i == 3 :
        continue
    print(i)

names = ['Teja', '', 'Sai', 'Arun']
for name in names :
    if name == '' :
        print("Empty value detected")
        continue
    print(f'name = {name}')

names = ('Teja', '', 'Sai', 'Arun', 'A')
for name in names :
    if name == '' :
        print("Empty value detected")
        continue
    print(f'Name = {name}')

# pass statement
for i in (1,2,3,4) :
    if i == 3 :
        pass
    print(i)

names = ['Teja', 'Sai', '', 'Arun']
for name in names :
    if name == '' :
        name = name.replace('', 'Unknown')
        pass
    print(f'Name = {name}')


## TASK
# Skip weekends in calender loop
days = ['Sun', 'Mon', 'Wed', 'Sat', 'Fri']
weekends = ['Sun', 'Sat']
for day in days :
    if day in weekends :
        continue
    print(f'Workdays = {day}')


## TASK
# Scan emails to block unsafe data from entering your system
emails = ['g.yuvateja@gmail.com',
          'g.yuvateja@outlook.com',
          'DROP TABLES USER;',
          'g.yuvateja@g.com']
for email in emails :
    if ';' in email :
        print("SQL INJECTION : Hacker Attack")
        break
    print(f'processing email : {email}')


# Else statement in loop
for i in [1,2,3,4] :
    print(i)
else :
    print("End")

items = [1,2,3,4,7,6]
for item in items :
    print(item)
else :
    print("Loop is completed")

# check for even number
items = [1,3,4,5]
for i in items :
    if i % 2 == 0 :
        print("Even Nr. Found :", i)
        break
else :
    print("All numbers are odd")

items = [1,3,7,5]
for i in items :
    if i % 2 == 0 :
        print("Even Nr. Found :", i)
        break
else :
    print("All numbers are odd")


## TASK
# check for missing names in list.
names = ['Teja', 'Sai', None, 'Arun']
for i in names :
    if i is None :
        print("Found a missing name")
        break
else :
    print("All names are available")

names = ['Teja', 'Sai', 'Ram', 'Arun']
for i in names :
    if i is None :
        print("Found a missing name")
        break
else :
    print("All names are available")

## TASK
# check if all files are csv files.
files = ['data.csv',
         'report.pdf',
         'report.csv']
for file in files :
    if not file.endswith('.csv') :
        print(f'{file} is not csv')
        break
else :
    print('All files are csv')

## TASK 
# any filename appears more than one
files = ['report.csv',
         'data.xlsx',
         'summary.docx',
         'report.csv',
         'data.csv']
seen = []
for file in files :
    if file in seen :
        print("Duplicate found")
        break
    seen.append(file)
else :
    print("All files are unqiue")


# nested for loop
for x in [1,2,3,4] :
    for y in [1,2,3] :
        print(x,y)

for x in range(3) :
    for y in range(2) :
        print(f'({x}, {y})')

## TASK
# cross data
colors = ['Red', 'Blue', 'Green']
sizes = ['L', 'M', 'S'] 
for color in colors :
    for size in sizes :
        print(f'{color} - {size}')

# navigate hierarchy
years = [2002, 2003]
months = ['Jan', 'Mar']
days = range(1, 32)
for year in years :
    for month in months :
        for day in days :
            print(f"report_{year}_{month}_{day}.csv")


## while loop

# condition 
i = 1
while i < 4 :
    print(i)
    i += 1

count = 1 
while count <= 5 :
    print(count)
    count += 1

count = 1 
while count <= 10 :
    print(count)
    count += 2

answer = ""
while answer != "Yes" :
    answer = input("Do you agree?(Yes/No) : ")
print("Thank you")

# True
while True :
    x =input('Type')
    if x == 'Stop' :
        break

while True :
    answer = input("Do you agree?(Yes/No) : ")
    if answer == "Yes" :
        break
print("Thank you")


## TASK 

# 3 attempts
# Yes within three attempts -> "Glad we're on same page"
# otherwise  "3 strikes. You're out"

attempts = 0
while attempts < 3 :
    answer = input("Do you agree?(Yes/No) : ")
    if answer == "Yes" :
        print("Glad we're on same page")
        break
    attempts += 1
else :   
    print("3 strikes. you're out!")
print("Thank you")