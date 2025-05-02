# 4. More Control Flow Tools

# 4.1 if Statements
x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else: #else isn't necessary
    print('More')

#4.2 for Statements
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# code to modify a collection while iterating over the collection
users = {'Hans': 'active', 'Ellie': 'inactive', 'Carolina': 'active'}
# either loop over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# or create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

# 4.3 range Function
for i in range(5):
    print(i)

# range(start, end, step)
# list(range(5, 10)) is [5, 6, 7, 8, 9]
# list(range(0, 10, 3)) is [0, 3, 6, 9]
# list(range(-10, -100, -30)) is [-10, -40, -70]

# combine range and len to iterate over the indices of a sequence
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# range(10) is range(0,10)
# sum(range(4)) is 6, 0 + 1 + 2 + 3

# 4.4 break and continue Statements
for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

# break gets out of the innermost for or while loop

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number: {num}")
        continue
    print(f"Found an odd number: {num}")

# continue goes to the next iteration of the loop

# 4.5 else Clauses on Loops
# searching for prime numbers
for n in range(2, 10):
    for x in range(2,n):
        if n%x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        # loop fell through without finding a factor
        print(f"{n} is a prime number")

# that else clause belongs to the for loop, NOT the if statement

# 4.6 pass Statements
# it does nothing, used when a statement is required syntactically but the program requires no action
# commonly used to create minimal classes
class MyEmptyClass:
    pass

# can also be used as a placeholder when you want to work on newer code
def initlog(*args):
    pass #REMEMBER TO IMPLEMENT THIS!

# 4.7 match Statements (HAVE ANANYA EXPLAIN)
# like a better switch statement, after one case is executed, that's it
def http_error(code):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case 418:
            return 'I\'m a teapot'
        case _: #underscore acts as a default case
            return 'Something\'s wrong with the internet'

# combine several literals in a single case using or (|)
# case 401 | 403 | 404:
#    return "Not allowed"

# point is an (x,y) tuple
# match point:
#     case (0, 0):
#         print(f"Origin)
#     case (0, y):
#         print(f"Y = {y}")
#     case (x, 0):
#         print(f"X = {x}")
#     case (x, y):
#         print(f"X = {x}, Y = {y}")
#     case _:
#         raise ValueError("Not a point")

# 4.8 Defining Functions
def fib(n): # write Fibonacci series less than n
    """Print a Fibonacci series less to n"""
    # above is a documentation string (docstring), it's good practice
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

# function creation needs keyword def, name, and any parameters
# the body must be below and indented
# fib is function fib is at 10042ed0
# f = fib
# f(100) is 0 1 1 2 3 5 8 13 21 34 55 89
# fib(0)
# print(fib(0)) is None

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

# f100 = fib2(100)    # call it
# f100 is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# 4.9 More on Defining Functions
# 4.9.1 Default Argument Values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# function can be called in several ways
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
# in keyword tests whether the sequence contains a certain value

i = 5
def f(arg=i):
    print(arg)

i = 6
f() # this prints 5

def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) # this is [1]
print(f(2)) # this is [1, 2]
print(f(3)) # this is [1, 2, 3]

# don't want the default shared, write like this
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# 4.9.2 Keyword Arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                                      # 1 positional argument
parrot(voltage=1000)                                              # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')                         # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)                         # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')       # 1 positional, 1 keyword

# invalid
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#        pos only      either/or       kw only
# keyword parameters are also called named parameters

# 4.9.3.1 Positional-Or-Keyword Parameters
# if / and * aren't present in the function definition
# then arguments may be passed to a function by position or by keyword

#4.3.9.2 Positional-Only Parameters
# positional-only parameters are before / in the function definition
# after the / may be positional-or-keyword or keyword-only

# 4.9.3.3 Keyword-Only Parameters
# place an * in the arguments list before the first keyword-only parameter
# keyword-only parameters must follow positional-only or positional-or-keyword parameters

# 4.3.9.4 Function Examples
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2) # this is 2
standard_arg(arg=2) # this is 2
pos_only_arg(2) # this is 2
# pos_only_arg(arg=2), this is wrong
kwd_only_arg(arg=2) # this is 2
# kwd_only_arg(2), this is wrong
combined_example(1, 2, kwd_only=3) # this is 1 2 3
combined_example(1, standard=2, kwd_only=3) # this is 1 2 3
# combined_example(pos_only=1, standard=2, kwd_only=3), this is wrong
def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2}) # this is True

# def foo(name, **kwds):
#     return 'name' in kwds
# this is a bad function definition

# 4.3.9.5 Recap
# pos before /, either between the / and *, keyword after *

# 4.9.4 Arbitrary Argument Lists
# def write_multiple_items(file, separator, *args):
#     file.write(separator.join(args))
def concat(*args, sep="/"):
    return sep.join(args)
concat("earth", "mars", "venus") # this is earth/mars/venus
concat("earth", "mars", "venus", sep=".") # this is earth.mars.venus

# 4.9.5 Unpacking Argument Lists
# list(range(3, 6)) # normal call with separate arguments, this is [3, 4, 5]
# args = [3, 6]
# list(range(*args)) # call with arguments unpacked from a list, this is [3, 4, 5]
# the * unpacks the arguments from a list/tuple

