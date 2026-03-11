## FUNCTIONS

# user-defined function

print("Start")
def greet() :
    print("Hello")
greet()
print("End")


# Built-in fuction (just calling)
print(len("python"))


# Function from libraries (Import then call)
import math
number = 4.3
print(math.ceil(number))

# user-defined function (define then call)
def greet() :
    print("Hello")
greet()


# parameters and arguments
def multiply_two(x) :
    print(x * 2)
multiply_two(4)

def clean_name(name) :
    print(name.strip().lower())
clean_name("          TeJA")
clean_name('   YUVA    ')
clean_name("")


# parameter, glabal variable and local variable.
def clean_name(name) :              # parameter
    cleaned = name.strip().lower()  # local
    print("Raw :", name)
    print("Cleaned_name :", cleaned)
clean_name("   YuvaTEJA   ")

case_rule = "lower"                 # global
def clean_name(name) :              # parameter
    cleaned = name.strip()          # local
    if case_rule == "lower" :
        cleaned = cleaned.lower()
    print("Cleaned_name :", cleaned)
clean_name("   YuvaTEJA   ")

case_rule = "N/A"                 # global
def clean_name(name) :              # parameter
    cleaned = name.strip()          # local
    if case_rule == "lower" :
        cleaned = cleaned.lower()
    print("Cleaned_name :", cleaned)
clean_name("   YuvaTEJA   ")
print('The rule is :', case_rule) 

# Building full clean name 
def clean_name(first_name, last_name) :
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name)
clean_name("    YuvA", "   TejA") 

def clean_name(first_name, last_name, country = "N/A") :
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + " " + last
    print(full_name, "from", country)
clean_name("    YuvA", "   TejA", "INDIA") 

# postional arguments
clean_name("INDIA", "    YuvA", "   TejA")   

# keyword arguments
clean_name(country = "India", last_name = "TEJA   ", first_name = "   YUVA") 

# mixed arguments
clean_name("   YUVA", country = "India", last_name = "TEJA   ") 

# default 
clean_name("    YuvA", "   TejA") 

# *args
# calculate the total of values
def total(*args) :
    print((sum(args)))
total(1,2)
total(1,2,3,4,5)
total(1,2,3,4,5,6,7,8,9)

# **kwargs
# create the user profile 
def create_user(**kwargs) :
    print(kwargs)
create_user(first_name = 'Yuva',
            last_name = 'teja',
            age = 24,
            country = 'India')

# return
f = 3
def multiple_factor(x) :
    y = x * f
    return y
z = multiple_factor(4)
print(z)

def clean_name(name) :
    cleaned = name.strip().lower()
    return cleaned
cln_name = clean_name('     YuvaTEJA')
print(cln_name)

def clean_name(name) :
    cleaned = name.strip().lower()
    # return cleaned
cln_name = clean_name('      YuvaTEJA')
print(cln_name)

def clean_name(name) :
    if not name :
        return None
    else :
        cleaned = name.strip().lower()
        return cleaned
cln_name = clean_name('')
print(cln_name)

def clean_name(name) :
    if not name :
        return None
    else :
        cleaned = name.strip().lower()
        return cleaned
cln_name = clean_name('teja')
print(cln_name)

def clean_name(name) :
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned
cln_name = clean_name('     YuvaTEJA')
print(cln_name)


# function type (by purpose of use cases)

# action function
# task : store application log message in a file.
def write_log(message) :
    with open(r"C:\Users\PC\OneDrive\Desktop\PYTHON\app.log", "a") as file :
        file.write(message + "\n")
write_log("App Started")
write_log("User logged in")
write_log("App stopped")

# transformation function
# task : clean an email and split it into username and domain.
def clean_and_split_email(email) :
    cl_email = email.strip().lower() 
    # g.yuvateja1870@gmail.com
    username, domain = cl_email.split("@")
    return {"username" : username,
           "domain" : domain}
print(clean_and_split_email('g.yuvateja1870@gmail.com'))

# validation function
# task : check if a password meets the minimum length of 8.
def is_valid_password(password) :
    return len(password) >= 8
print(is_valid_password("Yuvi12345"))
print(is_valid_password("12345"))

# task : check if email has a basic valid format.
def is_valid_email(email) :
    return "@" in email and "." in email
print(is_valid_email("g.yuvatejagmailcom"))
print(is_valid_email("g.yuvateja@gmail.com"))

# orchestrator function
def process_user_email(email) :
    write_log("App Started")
    # we must check if it is valid  
    # if it is not vaild, we log the problem
    if not is_valid_email(email) :
        write_log(f"Invaild email received : {email}")
    # if it a vaild, we clean it and store structured information
    else :
        clean_email = clean_and_split_email(email)
        write_log(f"Processed email : {clean_email}")
    write_log("App Stopped")
# we receive an email from a user 
email = input("Please enter your Email :")
process_user_email(email)



## writing function styling 

# bad style
def DiscPrint(p, r) :
    print("Calculating discount")
    p = p - (p * r/100)
    print(p)
DiscPrint(3,4)

# good style
def calculate_discount(price : float, rate : float) -> float :
    """
    Calculate the final price after applying a discount.
    Args :
        Price (float) : Orginal product price.
        rate (float) : Discount rate as numbers (e.g 20 for 20%).
    Returns :
        final_price (float) : Final price after applying discount.
    """
    final_price = price - (price * rate/100)
    return final_price
print(calculate_discount(4, 5))