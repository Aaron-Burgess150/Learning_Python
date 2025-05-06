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
# when an exception occurs, it may have associated values, known as exception arguments
# presence and type depend on exception type
# the except clause may specify a variable after the exception name
# the variable is bound to the exception instance which typically has an args attribute to store the arguments
# builtin exception types define __str()__ to print all arguments without explicitly accessing .args
# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception type
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                          # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)
# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs
# the exception's __str()__ output is printed as the last part of a message for unhandled exceptions
# BaseException is the common base class of all exceptions
# Exception, one of it's subclasses, is the base class of all non-fatal exceptions
# exceptions that aren't subclasses of Exception are typically unhandled, indicating the program should terminate
# they include SystemExit which is raised by sys.exit() and KeyboardInterrupt
# most common pattern for handling Exception is to print or log the exception and then re-raise it
#     this allows a caller to handle the exception as well
# import sys
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise
# try_except clauses have optional else clauses, which must follow all except clauses
# useful for code that must be executed if the try clause does not raise an exception
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()
# exception handlers also handle exceptions that occur inside functions that are called in the try clause

# 8.4 Raising Exceptions
# raise statement allows the programmer to force a specified error to occur
# raise NameError('HiThere')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     raise NameError('HiThere')
# NameError: HiThere