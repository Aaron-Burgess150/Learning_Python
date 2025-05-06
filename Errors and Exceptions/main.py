# 8 Errors and Exceptions

# 8.1 Syntax Errors
# SyntaxError: invalid syntax
# it repeats the offending line but that is not always the place that needs fixing
# while True print('Hello World')
# File "<file_directory>", line 6
#     while True print('Hello World')
#                ^^^^^
#
# SyntaxError: invalid syntax

# 8.2 Exceptions
# errors detected during execution
# last line of error message indicates what happened

# 8.3 Handling Exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# try statement works as follows:
#     try clause (statements between try and except keywords) is executed
#     if no exception occurs, the try clause is executed and the program continues
#     if an exception occurs, the rest of the try clause is skipped
#     if it matches the exception after the except keyword, the except clause is executed and the program continues
#     if the exception does not match the exception named, it is passed on to outer try statements
#     no handler found, it is an unhandled exception and execution stops with an error message
# a try statement can have multiple except clauses
# an except clause can have multiple exceptions in a tuple
# ... except (RuntimeError, TypeError, NameError):
# ...     pass
# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")
# this will print B, C, D in that order

