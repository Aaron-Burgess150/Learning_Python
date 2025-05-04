# 6 Modules
# if you close the Python interpreter, definitions are lost
# better off using a text editor and then running it with that file as input
# this is called creating a script
# may want to split into multiple files for easier maintenance
# a module is a file containing Python definitions and statements
# the file name is the module name with the suffix .py appended
# the name is available as a value of the global variable __name__
import fibo
fibo.fib(1000)
print(fibo.fib2(100))
# fibo.__name__ is 'fibo'
# to reuse a function from fibo
f = fibo.fib
f(1000) # this is the same as fibo.fib(1000)

# 6.1 More on Modules
# a module can contain executable statements as well as function definitions
# these statements are intended to initialize the module
# executed only the first time the module name is encountered in an import statement
# also run if the file is executed as a script
# modname.itemname
# modules can import other modules, place all import statements at the top
# import placed at top level adds to the module's global namespace
# different uses of import
# from fibo import fib, fib2 (fibo is not defined)
# fib(500), you can directly call the method
# from fibo import * (this imports all names the module defines, except ones that begin with an _)
# if the module name is followed by as, then the name following as is a placeholder
# import fibo as f
# f.fib(100) is the same as fibo.fib(100)
# from fibo import fib as fibonacci
# fibonacci(500) is the same as fibo.fib(500)

# 6.1.1 Executing Modules as Scripts
# you can run a Python module as
# python fibo.py <arguments>
# when you do, the code in the module will be executed as imported
# the name is set to __main__
# adding the following code at the end of the module makes it unusable as a scipt and an imported module
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))

# 6.1.2 The Module Search Path
# first the interpreter searches for a built-in module with the name "name"
# if not found, it searches for "name".py in a list of directories given by sys.path
# sys.path is initialized from these locations:
#     directory containing input script
#     PYTHONPATH (list of directory names)
#     installation-dependent default
# if a module you want to load has the same name as a standard library module
# this is because Python programs modify sys.path
# the directory with the script being run is placed at the beginning of the search path

# 6.1.3 "Compiled" Python Files
# to load modules fastly, python caches the compiled version of it in __pycache__ directory
# __pycache__/"name".cpython-33.pyc
# python automatically checks date to see if it should be recompiled
# no cache check to recompile and no cache check if no source module
# Expert tips:
#     You can use the -O or -OO switches on the Python command to reduce the size of a compiled module.
#         The -O switch removes assert statements, the -OO switch removes both assert statements and __doc__ strings.
#     Only use this option if you know what you’re doing. “Optimized” modules have an opt- tag and are usually smaller.
#
#     A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file
#     the only thing that’s faster about .pyc files is the speed with which they are loaded.
#
#     The module compileall can create .pyc files for all modules in a directory.

# 6.2 Standard Modules
# some modules are built-in to the interpreter
# winreg module provided on Windows systems
# sys is built into every Python interpreter
# import sys
# sys.ps1 is '>>> '
# sys.ps2 is '... '
# sys.ps1 = 'C>'
# C> print('Yuck!')
# Yuck!
# C>
# these two variables are only defined if the interpreter is in interactive mode
# sys.path is a list of strings containing the search path for modules
# initialized to a default path taken from the environment variable PYTHONPATH
#     or a built-in default if PYTHONPATH is not set
# modify using standard list operators
# import sys
# sys.path.append('/ufs/guido/lib/python')

# 6.3 dir() Function
# used to find out which names the module defines
# import fibo, sys
# dir(fibo) is ['__name__', fib, fib2]
# dir(sys)) is a long list
# without arguments, dir() lists the names you have currently defined
# all types of names listed (variables, modules, functions, etc.)
# dir() does not list built-in functions or variables
# import builtins
# dir(builtins) is a long list

# 6.4 Packages
# a way of structuring Python's module namespace
# ex: module name 'A.B' means package 'A' contains submodule 'B'
# dotted module names saves the authors of multi-module packages to have to worry about each other's names
# ex: a package contains modules for audio files of different types
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

# when importing a package, Python searches through directories in sys.path
# the __init__.py file is required to make Python treat directories containing the file as packages
# this prevents unintentionally hiding valid modules that happen to have the same names as packages
# the __init__.py file can be empty but can also execute initialization code
# the __init__.py file is always executed when the package is imported
# __all__ defines list of module names in the package
# import sound.effects.echo
# ^ loads the submodule sound.effects.echo, must be referenced with full name
# sound.effect.echo.echofilter(input, output, delay=0.7, atten=4)
# ^ calls the echofilter function in the submodule
# alternative way of importing the submodule:
# from sound.effects import echo
# no need for full name if you do this
# echo.echofilter(input, output, delay=0.7, atten=4)
# you can also import the desired function
# from sound.effects.echo import echofilter
# echofilter(input, output, delay=0.7, atten=4)
# ImportError exception raised if no package/module of the name is found in package
# when using the syntax "   import item.subitem.subsubitem   ", each item except the last must be a package
# last item can be a module or a package but not a variable or function defined in the previous item

# 6.4.1 Importing * From a Package
# from package import *
# this imports all names from the package defined in __all__
# package authors can decide not to support it if they don't see a use for importing *
# submodules might become shadowed by locally defined names
# __all__ = [
#     "echo",      # refers to the 'echo.py' file
#     "surround",  # refers to the 'surround.py' file
#     "reverse",   # !!! refers to the 'reverse' function now !!!
# ]
#
# def reverse(msg: str):  # <-- this name shadows the 'reverse.py' submodule
#     return msg[::-1]    #     in the case of a 'from sound.effects import *'
# if __all__ is not defined, the statement from sound.effects import * would
#   only ensure package sound.effects has been imported and whatever names are
#   defined in the package
# import sound.effects.echo, echo imported
# import sound.effects.surround, surround imported
# from sound.effects import *, echo and surround modules imported
# import * is considered a bad practice in production code
# from package import specific_submodule is the recommended notation unless
#   the module needs to use submodules of the same name in a different package

# 6.4.2 Intra-Package References
# when packages are structured in subpackages, you can use absolute imports to refer to submodules
# if module sound.filters.vocoder needs to use the echo module in sound.effects,
# you can use the following syntax:
# from sound.effects import echo
# from sound.filters import vocoder
# vocoder.filter(input, output, echo.echofilter)
# this is called intra-package references
# absolute imports are not recommended in production code
# relative imports are the recommended way to import submodules
# from . import echo
# from .. import formats
# from ..filters import equalizer
# relative imports based off name of current module
# modules intended for use as the main module of the a Python application must always be absolute imports

# 6.4.3 Package in Multiple Directories
# packages have one more special attribute: __path__
# initiialized to be a sequence of strings containing the name of the directory holding the package's __init__.py file
# __path__ can be modified to change the search path for modules
#     this affects future searches for modules and subpackages contained in the package
# feature is not often needed but can be used to extend the set of modules found in a package