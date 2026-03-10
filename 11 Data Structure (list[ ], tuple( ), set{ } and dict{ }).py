## DATA STRUCTURE

## List()   # common

## ordered, allow duplicates, indexed and mutable
my_list = [10, 30, 20, 10]
print(my_list)          # ordered
print(my_list)          # allow duplicates
print(my_list[1])       # Indexed 
my_list[3] = 40
print(my_list)          # Mutable


## Tuple()  # No change

## ordered, allow duplicates, indexed and immutable
my_tuple = (10, 30, 20, 10)
print(my_tuple)         # ordered
print(my_tuple)         # allow duplicates
print(my_tuple[1])      # Indexed 
# my_tuple[3] = 40      # Immutable


## Set{}  # Unique

## unordered, unique, not indexed and mutable
my_set = {10, 30, 20, 10}
print(my_set)           # unordered
print(my_set)           # unique
# print(my_sets[1])     # not indexed
my_set.remove(20)
print(my_set)           # mutable 


## Dict{}   # key : value

my_dict = {'a' : 10, 'b' : 30, 'c' : 30, 'a' : 40}
print(my_dict)          # ordered
print(my_dict)          # keys are unique and values allows duplicates
print(my_dict['b'])     # not indexed (keyed)
my_dict['c'] = 20
print(my_dict)