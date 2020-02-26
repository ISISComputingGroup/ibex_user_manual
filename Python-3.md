From January 1, 2020 python 2.x.x is no longer supported. Therefore we have decided that IBEX migrate to only use Python 3 from the cycle 28th April 2020.

The materials used for Python 2 to 3 migration workshop could be found here: http://www.facilities.rl.ac.uk/isis/computing/ICPdiscussions/Forms/AllItems.aspx?RootFolder=%2Fisis%2Fcomputing%2FICPdiscussions%2FPython3&FolderCTID=0x01200027AD8F05966A2748B3B04C98BB5B442B&View=%7bF2C33C51-70E6-4343-B937-2C59A2568306%7d.

The material is trimmed down to only target python 2 to 3 migration for IBEX users.

## Why Python 3?

One of the main reasons for migration is that Python 2 is no longer supported by its creators. Python 3 also has implemented many useful features and also the Python 3 support community is growing and it makes it easier for scientists to learn Python 3.

## Python 3 major changes:

### Print Statements
In Python 3, the `print` statement is changed to a function. Therefore, you need to pass parentheses  for e.g. `print("Hi this is Python3)` instead of `print "Hi this is Python2"`

### Division:
In python 3 the division between two `int` values will result in `float` for example: `5/2` will result in `2.5`.

### Text and Binary Data
This is one of the main reasons why Python 3 is not backwards compatible.
In Python 3, text and binary data are distinct types which users are not allowed to mix together. for example ` var = b"python" + u"three"` will be an illegal operation whereas in python 2 users would be allowed to do so. 

String literals such as `var = "Python"` are `Unicode` by default in Python 3 whereas in Python 2 they were of type `bytes`. Comparison between of type `bytes` and `Unicode` for e.g. `b"test2" == u"test"` would return true in Python 2 whereas in Python 3 it would return false.

### Banker’s Rounding
Python 3 way of rounding is the standard of way of rounding decimals when it has resulted in a tie(.5). Python 3 will now round to the nearest even number unlike Python 2 which rounds up to a large number. For e.g. `round(16.5)` will result to `16` in Python 3 whereas in Python 2 it will result in `17`.

## Porting to Python 3
