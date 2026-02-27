## CLEANING

# clean whitespaces

# lstrip
text = "  Engineering"
print(text.lstrip())

# rstrip
text = " Engineering "
print(text.rstrip())

# strip
text = " Engineering "
print(text.strip())


# clean cases

# lower()
text = "Yuva TejA"
print(text.lower())

# upper()
text = "Yuva TejA"
print(text.upper())



## SEARCHING

# startswith(substring)
phone = "798-152-4920"
print(phone.startswith("79"))
print(phone.startswith("789"))

# endswith(substring)
phone = "798-152-4920"
print(phone.endswith("920"))
print(phone.endswith("333"))

email = "name@gmail.com"
print(email.endswith("mail.com"))
print(email.endswith("outlook.com"))

# in ## 'substring' in 'string'
email = "name@gmail.com"
print("@" in email)
print("a" in email)

# find(substring)
phone = "798-152-4920"
print(phone.find("-"))
print(phone[phone.find("-")+1])
print(phone[phone.find("-")+1:])


## VALIDATING

# isalpha()
country = "INDIA"
print(country.isalpha())

country = "12 India"
print(country.isalpha())

# isnumeric()
phone = "7981524920"
print(phone.isnumeric())

phone = "798-152-4920"
print(phone.isnumeric())