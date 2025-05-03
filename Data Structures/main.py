# 5. Data Structures

# 5.1 More on Lists
# list.append(x)- add x to end of list (similar to a[len(a):] = x)
# list.extend(iterable)- extend the list by appending all items from iterable to end of list
#     (similar to a[len(a):] = iterable)
# list.insert(i, x)- insert x at index i
# list.remove(x)- remove first occurrence of x, raises ValueError if not found
# list.pop([i])- remove item at index i (default last) and return it
#     IndexError if list is empty or index is out of range
# list.clear()- remove all items from list
#     (similar to del a[:])
# list.index(x[,start[, end]])- return index of first occurrence of x, raises ValueError if not found
#     optional start and end is slice notation
# list.count(x)- return number of occurrences of x
# list.sort(*, key=None, reverse=False)- sort list in place, arguments can be used for sort customization
# list.reverse()- reverse list in place
# list.copy()- return a shallow copy of the list
#     similar to a[:]

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple') # this returns 2
fruits.count('tangerine') # this returns 0
fruits.index('banana') #this returns 3
fruits.index('banana', 4)  # Find next banana starting at position 4, it returns 6
fruits.reverse()
# fruits is ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
# fruits is ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
# fruits is ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop() # this returns 'pear' and removes it from the list

# 5.1.1 Using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
# stack is [3, 4, 5, 6, 7]
stack.pop() # this returns 7 and removes it from the list
# stack is [3, 4, 5, 6]
stack.pop() # this returns 6 and removes it from the list
stack.pop() # this returns 5 and removes it from the list
# stack is [3, 4]

# 5.1.2 Using Lists as Queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # Terry arrives
queue.append("Graham") # Graham arrives
queue.popleft() # this returns "Eric" because he was the first to arrive
queue.popleft() # this returns "John" because he was second to arrive
# queue is deque(['Michael', 'Terry', 'Graham'])

# 5.1.3 List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)

# squares is [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# you can also do the following for the same list
squares2 = list(map(lambda x: x**2, range(10)))
squares3 = [x**2 for x in range(10)]

# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] is [(1, 3), (1, 4), (2, 3), (2, 4), (3, 1), (3, 4)]
# and it is the same as all this code:
# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
#
# combs is [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# tuples must be in parentheses
# e.g: [(x, x**2) for x in range(6)] is [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# vec = [-4, -2, 0, 2, 4]
# [x*2 for x in vec] is [-8, -4, 0, 4, 8]
# [x for x in vec if x >= 0] is [0, 2, 4]
# [abs(x) for x in vec] is [4, 2, 0, 2, 4]
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# [weapon.strip() for weapon in freshfruit] is ['banana', 'loganberry', 'passion fruit']
# [(x, x**2) for x in range(6)] is [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
#  ^^^^^^^^    must be in parentheses
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# [num for elem in vec for num in elem] is [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list comprehensions can contain complex expressions and nested functions

# 5.1.4 Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# [[row[i] for row in matrix] for i in range(4)] is [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

# transposed is [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# which is the same as
# transposed = []
# for i in range(4):
#     # the following 3 lines implement the nested listcomp
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
#
# transposed is [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# suggested to use the zip function for this purpose
# list(zip(*matrix)) is [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

# 5.2 del Statement
# removes something by index, can also be used in slicing and for the whole list
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# a is [1, 66.25, 333, 333, 1234.5]
# del a[2:4]
# a is [1, 66.25, 1234.5]
# del a[:]
# a is []
# del can also be used to delete variable
# del a

# 5.3 Tuples and Sequences
t = 12345, 54321, 'hello' #example of tuple packing
x, y, z = t # sequence unpacking
# t[0] is 12345
# t is (12345, 54321, 'hello)
# tuples may be nested
u = t, (1, 2, 3, 4, 5)
# u is ((12345, 54321, 'hello'), (1, 2, 3, 4, 5))
# tuples are immutable
# t[0] = 88888
# TypeError: 'tuple' object does not support item assignment
# but they can contain multiple mutible objects
v = ([1, 2, 3], [3, 2, 1])
# v is ([1, 2, 3], [3, 2, 1])

empty = ()
singleton = 'hello',    # <-- note trailing comma
# len(empty) is 0
# len(singleton) is 1
# singleton is ('hello',)

# 5.4 Sets
# sets are unordered with no duplicates
# sets are written with curly braces {}
# empty set creation is set(), not {} (this is for dictionaries)\
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                          # show that duplicates have been removed
# 'orange' in basket is True           # fast membership testing
# 'crabgrass' in basket is False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
# a is {'a', 'r', 'b', 'c', 'd'}                    # unique letters in a
# a - b is {'r', 'd', 'b'}                          # letters in a but not in b
# a | b is {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'} # letters in a or b or both
# a & b is {'a', 'c'}                               # letters in both a and b
# a ^ b is {'r', 'd', 'b', 'm', 'z', 'l'}           # letters in a or b but not both
# set comprehension is also supported
# {x for x in 'abracadabra' if x not in 'abc'} is {'r', 'd'}

# 5.5 Dictionaries
# indexed by keys
# keys must be immutable, e.g. strings, numbers or tuples of numbers, strings, or tuples
# cant use lists as keys
# dictionaries are a set of key: value pairs, each key is unique
# empty {} makes an empty dictionary
# store using a key that is already in use overwrites the old value
# can delete a key: value pair with del d[key]
# error to extract a value using a non-existent key
# performing list(d) returns a list of all the keys in the dictionary
# to sort it, use sorted(d) instead
# check whether a key is in the dictionary with keyword in

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
# tel is {'jack': 4098, 'sape': 4139, 'guido': 4127}
# tel['jack'] is 4098
del tel['sape']
tel['irv'] = 4127
# tel is {'jack': 4098, 'guido': 4127, 'irv': 4127}
# list(tel) is ['jack', 'guido', 'irv']
# sorted(tel) is ['guido', 'irv', 'jack']
# 'guido' in tel is True
# 'jack' not in tel is False
# dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) is {'sape': 4139, 'guido': 4127, 'jack': 4098}
# dict comprehensions can be made with arbitrary keys and values
# {x: x**2 for x in (2, 4, 6)} is {2: 4, 4: 16, 6: 36}

# 5.6 Looping Techniques
# looping through dictionaries: key and value can be retrieved with items() method
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# looping through a sequence: index and value can be retrieved with enumerate() function
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# looping through two sequences: entries can be paired with zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# looping through a sequence in reverse order: use reversed() function
for i in reversed(range(1, 10, 2)):
    print(i)

# looping through a sequence in sorted order: use sorted() function
bucket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(bucket)):
    print(f)

# using set() on a sequence eliminates duplicates
for f in sorted(set(bucket)):
    print(f)

# instead of changing the list while looping, just make a new list

# 5.7 More Conditions
# in and not in checks whether an element is in or not in a sequence
# is and not is compares whether two objects are the same object
# priority of comparison operators are the same, lower than numerical operators
# a < b == c tests whether a is less than b and b is equal to c
# Boolean operators and and or can be used to combine conditions, negated with not
# lower priorities than comparison operators
# not is the highest and or is the lowest
# A and not B or C is the same as (A and (not B)) or C
# always use parentheses when combining conditions
# and and or are short-circuit operators, so evaluated from left to right and stops as soon as the outcome is determined
# A and C are true, B is false
# A and B and C does not evaluate to C
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
# non_null is 'Trondheim'
# assignment inside an expression is done with := so = can be used to compare (unlike C)

# 5.8 Comparing Sequences and Other Types
# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
# first two compared; if equal, then the next
# same type of object compared
# shorter sequence is smaller one
# lexicographical ordering is followed
# not the same type raises a TypeError exception