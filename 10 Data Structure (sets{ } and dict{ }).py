## DATA STRUCTURE

## SETS{ } 

# how to add value to set

a = {10, 30, 20, 50}
a.add(40)
a.update({1,2})
a |= {1,2}
# a.remove(100)
a.discard(1)
a.discard(100)
print(a)


# math operations

a = {10, 30, 20, 50}
b = {20, 30, 40, 60}
print(a.union(b))                   # union()
print(a | b)

print(a.intersection(b))            # intersection()
print(a & b)

print(a.difference(b))              # difference()
print(a - b)
print(b.difference(a))
print(b - a)

print(a.symmetric_difference(b))    # symmetric_difference()
print(a ^ b)


# relational method 

a = {30, 20}
b = {20, 30, 40, 60}
print(a.issubset(b))                # issubset()
print(b.issuperset(a))              # issuperset()
print(a.isdisjoint(b))              # isdisjoint()



## DICT{ }

# methods

# acess
user = {'id' : 1, 'age' : 24, 'city' : 'Hyderabad'}
print(user.get("name", "Unknown"))      # get()
print(user.get('id'))

# checks
print("age" in user)                    # in
print("name" not in user)               # not in

# view objects
print(user.keys())                      # keys()
print(user.values())                    # values()
print(user.items())                     # items()

# add, remove, update
user["Name"] = "Teja"                   # add
print(user)

user["age"] = 25                        # update
print(user)

user.pop("age")                         # remove  # pop()
print(user)

user.popitem()                          # popitem()
print(user)

# creation
user = {'id' : None,
        'Name' : None,
        'age' : None,
        'city' : None}
user = dict.fromkeys(['id', 'Name', 'age', 'city'], 0)
print(user)