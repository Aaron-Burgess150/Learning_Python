# 3. Informal Introduction to Python
# done in an interpreter but translated by me (properly I hope)
# >>> is where you puts the expressions, the part after the "is" is returned

# this is a comment
spam = 1
text = "# This is not a comment bc it's inside quotes."

# 3.1 Python as a Calulator

# 3.1.1 Numbers
# 2+2 is 4
# 50 - 5*6 is 20
# (50 - 5*6) / 4 is 5.0, division always returns a floating point number
# 8/5 is 1.6
# 17 / 3 is 5.666666666666667
# 17 // 3 is 5, this is floor division so no decimals
# 17 % 3 is 2
# 5**2 is 25 (EXPONENTS)
# 2**7 is 128
#-3**2 is -9
# (-3)**2 is 9

width = 20
height = 5 * 9
# width * height is 900
# you can't do anything with an undefined variable in the interpreter
# 4 * 3.75 - 1 is 14.0
tax = 12.5 / 100
price = 100.50
# price * tax = 12.5625
# price + _ is 113.0625, the underscore is used as a previous answer saver
# round(_,2) is 113.06

# 3.1.2 Text
# 'spam eggs' is 'spam eggs'
# "Paris rabbit got your back :)! Yay!" is 'Paris rabbit got your back :)! Yay!'
# '1975' is '1975'
# doesn\'t' is 'doesn't'
# "doesn't" is "doesn't"
# using a double quote needs \" if you want the " in the string
# vice versa for single quotes
s = 'First line.\nSecond line.'
# s is 'First line.\nSecond line.'
print(s)
print('C:\some\name')
print(r'C:\some\name')
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""") #string literal
# 3*'un' + 'ium' is 'unununium'
# 'Py' 'thon' is 'Python'
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
prefix = 'Py'
# prefix + 'thon' is an error, you can't concatenate a variable with a string literal (invalid syntax)
# ('un'*3) 'ium' is an error, invalid syntax
# use a +
print(prefix+'thon') # this was in the interpreter, no print function
word = 'Python'
# word[0] is 'p', character position 0
# word[5] is 'n', character position 5
# word[-1] is 'n', last character
# word[-2] is 'o', second to last character
# word[-6] is 'p'
# slicing
# word[0:2] is 'Py', goes from 0 (included) to 2 (excluded)
# word[2:5] is 'tho'
# word[-2:] is 'on'
# word[:2] is 'Py', goes from start to 2 (excluded)
# word[4:] is 'on', goes from 4 to end
# word[:i] + word[i:] is always word
# length of word[a:b] is b-a
# word[42] is an error, string index out of range
# word[4:42] is 'on', it'll just go to the end instead of out of bounds
# word[42:] is ''
# strings are immutable so word[0] = j is not a thing
# neither is word[2:] = 'py'
# you'd need to create a new string
# 'J' + word[1:] is 'Jython'
# word[:2] + 'py' is Pypy
# s = poop
# len(s) is 4

# 3.1.3 Lists
# Lists might contain items of different types, but usually the items all have the same type
# squares = [1, 4, 9, 16, 25]
# squares is [1, 4, 9, 16, 25]
# squares[0] is 1
# squares[-1] is 25
# squares[-3:] is [9, 16, 25]
# squares + [36, 49, 64, 81, 100] is [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# lists are mutable so squares[0] = 2 makes squares [2, 4, 9, 16, 25]
# you can add to a list by using .append() so -->
# squares.append(11**2), you can just do 121
# squares is [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
# Python never copies data so -->
# rgb = ['Red', 'Green', 'Blue']
# rgba = rgb
# id(rgb) == id(rgba) is true
# rgba.append('Alph')
# rgb is ['Red', 'Green', 'Blue', 'Alph']
# all slicing returns a new list
# something[:] is the whole something
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# letters is ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# letters[2:5] = ['C', 'D', 'E']
# letters is ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# letters[2:5] = []
# letters is ['a', 'b', 'f', 'g']
# letters[:] = []
# letters is []
# letters = ['a', 'b', 'c', 'd']
# len(letters) is 4
# 2D array creation with variables
a = [1, 2, 3]
b = [4, 5, 6]
x = [a,b]
# x is [[1, 2, 3], [4, 5, 6]]
# x[0] is [1, 2, 3]
# x[0][1] is 2

# 3.2 Programming
# Fibonacci Sequence
a, b = 0, 1
while a < 10:
        print(a)
        a, b = b, a+b

i = 256*256
print('The value of i is', i)

a, b = 0, 1
while a < 1000:
        print(a, end=',')
        a, b = b, a+b