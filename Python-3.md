From January 1, 2020 Python 2 is no longer supported. Therefore, from cycle 2020/01 (28th April 2020), IBEX will move to Python 3 only.  Mantid is also migrating to Python 3 on the same timescale.

The materials used for Python 2 to 3 migration workshop can be found here: [Workshop slides](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FPython3&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View=%7bF2C33C51-70E6-4343-B937-2C59A2568306%7d.)

The material is trimmed down to only target python 2 to 3 migration for IBEX users.

## Why Python 3?

The main reason for migrating is that Python 2 is no longer supported by its creators. Python 3 also has implemented many useful features and its support community is growing making it easier for users to learn Python 3.

## Changes in IBEX due to Python 3

Under python 3, the mechanism by which instrument scripts are imported has changed.

For instruments with single-file ``inst`` modules, we have migrated your scripts from ``C:\Instrument\Settings\config\[MACHINE_NAME]\Python\inst\xxx_routines.py`` to ``C:\Instrument\Settings\config\[MACHINE_NAME]\Python\inst.py``.

For instruments with multi-file ``inst`` modules, they are still in the same location as before. However, when adding new functions, in most cases you will also need to import them in ``__init__.py`` before they are available in ``inst``.

This change has been made because our previous approach (which attempted to emulate ``from * import *``) is increasingly difficult to maintain in python 3, and has caused confusion in a number of instances due to functions accidentally overwriting previously defined functions of the same name. 

You can learn more about the structure of python modules at https://docs.python.org/3/tutorial/modules.html#packages

## Changes in Python 3

Python 3 introduces a number of changes, but the 3 main changes you need to be aware of are:
   1. changes to the syntax of print statements
   1. behaviour of the division operator
   1. changes to text and binary data

There are some other changes.  We've listed the most common ones below.  If your  scripts rely on behaviour that changes in Python 3, you need to update your scripts to the new Python 3 behaviour.

### Print Statements
In Python 3, the `print` statement becomes a function. Therefore, you need to pass the string you wish to print in parentheses.  For example:<br>
   * in Python 2 you would write: `print "Hi this is Python 2"`
   * in Python 3 you write: `print("Hi this is Python 3)`

### Division:
In Python 3, the division of two `int` values will result in `float`: for example: `5/2` will result in `2.5`.  If you want the division of two `int` values to result in an integer, use the `//` operator: for example `5//2` will result in a value of `2`.

### Text and Binary Data
The handling of text and binary data changes in Python 2.  This is one of the main reasons why Python 3 is not backwards compatible with Python 2.  In Python 3, text and binary data are distinct types which users are not allowed to mix together. For example ` var = b"python" + u"three"` is an illegal operation, whereas in Python 2 this was a permitted operation. 

String literals such as `var = "Python"` are `Unicode` by default in Python 3,  whereas in Python 2 they were of type `bytes`. Comparison between of type `bytes` and `Unicode` for e.g. `b"test2" == u"test"` would return true in Python 2 whereas in Python 3 it returns false.

### Banker’s Rounding
Python 3 way of rounding is the standard of way of rounding decimals when it has resulted in a tie(.5). Python 3 will now round to the nearest even number, unlike Python 2 which rounds up to the next largest integer. For e.g. `round(16.5)` will result in `16` in Python 3 whereas in Python 2 it will result in `17`.

### Range in Python 3
Python 2 `xrange` is now equivalent to Python 3 `range`. `range` cannot be used as list object for e.g. `range(0,10)` will no longer return a list of `[0,1...,9]`. It can still be used in for loop `for x in range(10)`. If you need a list you using `range()` you can still do `list(range(0, 10))` which will then return a list.

## Porting to Python 3
### Futurize
The Future module eases the process of making Python 2 code compatible with Python 3 as well.  The [Workshop Slides](http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FPython3&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View=%7bF2C33C51-70E6-4343-B937-2C59A2568306%7d.) provide an introduction to futurize.

To run futurize in more than one files you have to make sure that all the `.py` files you want to convert is in the same directory for e.g. `C:\example\allPythonScripts` all my scripts to be converted are in the folder `allPythonScripts`. Once you have collected the scripts you want to convert in a single directory, run the command `futurize –w C:\example\allPythonScripts`. 

This will then convert all scripts present in `allPythonScripts` to python2/3 compatible script. It will also generate a file with extension `.py.bak` which is a backup file. If you require original python file then you can simply rename the file extension from `.py.bak` to `.py`. If you want to be careful about what futurize might do to your python file, running the command without `-m` flag `futurize C:\example\allPythonScripts` will only suggest you some changes without overwriting it. Please do make sure manually that changes made by `futurize` are valid.

## Topics not covered but might be worth reading

Python 3 has disallowed implicit relative import and only the following two imports are allowed. 
* [Absolute Imports](https://realpython.com/absolute-vs-relative-python-imports/#absolute-imports)

* [Relative Imports](https://realpython.com/absolute-vs-relative-python-imports/#relative-imports)

* [Common Stumbling Blocks](https://docs.python.org/3/whatsnew/3.0.html#common-stumbling-blocks)