## CONDITIONAL STATEMENTS

# if statement
score = 90
if score >= 75 :
    print("A") 

# else statement
score = 40
if score >= 75 :
    print("A")
else :
    print("F") 

# elif statement
score = 40
if score >= 75 :
    print("A")
elif score >= 30 :
    print("B")
else :
    print("F") 

# elif statement (WE CAN USE ELIF MORE TIMES ALSO)
score = 40
if score >= 75 :
    print("A")
elif score >= 50 :
    print("B")
elif score >= 35 :
    print("C")
else :
    print("F") 

# nested if statement
score = 90
submitted_project = True
if score >= 75 :
    if submitted_project :
        print("A+")
    else :
        print("A")
elif score >= 95 :
    print("B")
elif score >= 100 :
    print("C")
else :
    print("F") 

score = 90
submitted_project = False
if score >= 75 :
    if submitted_project :
        print("A+")
    else :
        print("A")
elif score >= 95 :
    print("B")
elif score >= 100 :
    print("C")
else :
    print("F")

# connecting more conditons (USE and AND or operator)
score = 90
submitted_project = True
if score >= 75 and submitted_project :
    print("A+")
elif score >= 80 :
    print("A")
elif score >= 95 :
    print("B")
elif score >= 100 :
    print("C")
else :
    print("F")

score = 90
submitted_project = False
if score >= 75 and submitted_project :
    print("A+")
elif score >= 80 :
    print("A")
elif score >= 95 :
    print("B")
elif score >= 100 :
    print("C")
else :
    print("F")

# more ifs statments 
score = 70
submitted_project = True
if score >= 80 :
    print("High score")
else :
    print("Low score")
if submitted_project :
    print("Project is submitted")
else :
    print("Project is not submitted")

# inline if
score = 90
grade = "A" if score >= 80 else "B"
print(grade)

score = 70
grade = "A" if score >= 80 else "B"
print(grade)

# match case
country = "Germany"
match country :
    case "united states" :
        print("US")
    case "India" :
        print("IN")
    case "Egypt" :
        print("EG")
    case "Germany" :
        print("DE")
    case _:
        print("Unknown country")
    
country = "UK"
match country :
    case "united states" :
        print("US")
    case "India" :
        print("IN")
    case "Egypt" :
        print("EG")
    case "Germany" :
        print("DE")
    case _:
        print("Unknown country")

country = "USA"
match country :
    case "united states" | "USA":
        print("US")
    case "India" :
        print("IN")
    case "Egypt" :
        print("EG")
    case "Germany" :
        print("DE")
    case _:
        print("Unknown country")


## TASK 

email = "g.yuvateja1870@gmail.com"
# Clean the string
email = email.strip()
# Email must not be empty
if email == "" :
    print("Email can't be empty.")
# Email must contain a '.' and '@'
elif not('.' in email and '@' in email) :
    print("Email must contain . and @")
# Email must contain exactly one '@' symbol
elif email.count('@') != 1 :
    print("Email must contain exactly one '@'.")
# Email must end with '.com', '.org', or .'.net'
elif not email.endswith(('.com', '.org', '.net')) :
    print("Email must end with .com, .org, .net")
# Email must not be longer than 254 characters 
elif len(email) > 254 :
    print("Email must not be longer than 254 characters")
# Email must start and end with a letter or digit
elif not(email[0].isalnum() and email[-1].isalnum()) :
    print("Email must start and end with a letter or digit")
else :
    print("Email is valid.")



email = "g.yuvate#@ja1870@gmail.co$"
# Clean the string
email = email.strip()
# Email must not be empty
if email == "" :
    print("Email can't be empty.")
# Email must contain a '.' and '@'
if not('.' in email and '@' in email) :
    print("Email must contain . and @")
# Email must contain exactly one '@' symbol
if email.count('@') != 1 :
    print("Email must contain exactly one '@'.")
# Email must end with '.com', '.org', or .'.net'
if not email.endswith(('.com', '.org', '.net')) :
    print("Email must end with .com, .org, .net")
# Email must not be longer than 254 characters 
if len(email) > 254 :
    print("Email must not be longer than 254 characters")
# Email must start and end with a letter or digit
if not(email[0].isalnum() and email[-1].isalnum()) :
    print("Email must start and end with a letter or digit")
else :
    print("Email is valid.")