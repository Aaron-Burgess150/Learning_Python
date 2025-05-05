# 7 Innput and Output

# 7.1 Fancier Output Formatting
# expression statements and print() statements have been used to print to write values
# you can also use the write() method of file objects
# standard output file can be referenced as sys.stdout
# several different ways to format output
# formatted string literals, begin with f or F before the " " or """ """
# use {} for Python expressions to refer to variables or literal values
# use str.format, stil use {} for variables
# you have to say the variables in the parameters of str.format()
# yes_votes = 42_572_654
# total_votes = 85_705_149
# percentage = yes_votes / total_votes
# '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
# ^^^ this is ' 42572654 YES votes  49.67%'
# yes_votes is padded with spaces and a negative sign for negative numbers
# convert any value to a string the repr() or str() function
# str() meant to return representations of fairly human-readable values
# repr() meant to generate representations read by the interpreter
# forces a SyntaxError if no equivalent syntax
# s = 'Hello, world.'
# str(s) is 'Hello, world.'
# repr(s) is "'Hello, world.'"
# str(1/7) is 0.14285714285714285
# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# print(s) is The value of x is 32.5, and y is 40000...
# The repr() of a string adds string quotes and backslashes:
# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos) is 'hello, world\n'
# The argument to repr() may be any Python object:
# repr((x, y, ('spam', 'eggs'))) is "(32.5, 40000, ('spam', 'eggs'))"

# 7.1.1 Formatted String Literals
# allows inclusion of expressions using {} and an f or F before the ""
# a format specifier can follow the expression to allow control over format
# passing an integer after : will cause the field to be a minimum number of characters wide
# !a applies acii(), !r applies repr(), and !s applies str()
# = specifier adds the variable and an equal sign before the repr() representation

# 7.1.2 The String format() Method
# print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# is We are the knights who say "Ni!"
# The brackets and characters within them are called format fields
# They are replaced with the objects passed into the str.format() method
# Numbers inside the bracket can refer to the object passed to the method
# print('{0} and {1}'.format('spam', 'eggs')) is spam and eggs
# print('{1} and {0}'.format('spam', 'eggs')) is eggs and spam
# Keywords used in str.format(), then values are referred to by the names of their arguments
# print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
# ^ is This spam is horrible.
# Positional and keyword arguments can be arbitrarily combined
# Passing the dict and using [] to access the keys
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
#       'Dcab: {0[Dcab]:d}'.format(table))
# ^ is Jack: 4098; Sjoerd: 4127; Dcab: 8637678
# can also pass the dict using **
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# ^ is Jack: 4098; Sjoerd: 4127; Dcab: 8637678
# vars() returns a dictionary containing all local variables
# table = {k: str(v) for k, v in vars().items()}
# message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
# print(message.format(**table)) is __name__: __main__; __doc__: None; __package__: None; __loader__: ...
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print()

# 7.1.3 Manual String Formatting
# manual formatting of above code:
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

# print() keeps one space between arguments
# str.rjust() right justifies objects padding it with spaces on the left
# str.ljust() and str.center() exist as well
# input too long, it leaves the string unchanged, messing up formatting
# str.zfill() pads a numeric string on the left with 0s, respects +/-
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

# Old String Formatting
# %, used as format % values (format is a string)
# this is known as string interpolation
import math
print('The value of pi is approximately %5.3f.' % math.pi)

# 7.2 Reading and Writing Files
# open() returns a file object, most commonly used with 2 positional arguments and one kw argument
# f = open('workfile', 'w', encoding="utf-8")
#           ^filename       ^utf-8 is modern de-facto standard
#                       ^how the file will be used
# r will read only, w is for overwriting, a will append, r+ reads and writes, optional (default is r)
# adding a b to the end of the mode opens the file in binary mode
# be careful to use binary mode for .JPEG and .EXE files
# use the with keyword when dealing with file objects
# this ensures the file is properly closed after its suite finishes, even with exceptions raised
# with open('workfile', encoding="utf-8") as f:
#     read_data = f.read()
#
# # We can check that the file has been automatically closed.
# f.closed is True
# if not using with, immediately close the file with f.close()
# attempting to do anything with the file object after the file closes will automatically fail