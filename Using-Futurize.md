# Futurize

### Description:
Futurize takes in your Python 2 code and turns it into valid Python 3 code, and also makes it backwards compatible with Python 2 using future package.

## Using Futurize:
There are mainly two ways on how you can translate your script using Futurize. More information could be found [here](http://python-future.org/futurize_cheatsheet.html).

### Translating a single file
* Open Command Prompt
* **cd** `C:\Instrument\Apps\Python\Scripts`
* **futurize** `path\to\your\script`

Now it should suggest some changes, to overwrite your current file with the suggested changes run the following command.

* **futurize -w** `path\to\your\script`


### Translating multiple files at once
You have to manually create a list of python scripts you want to translate and place them in a separate folder. Replace `path\to\your\recently\created\folder` with the name of the folder where you have bundled all your script.

* Open Command Prompt
* `cd C:\Instrument\Apps\Python\Scripts`
* `futurize path\to\your\recently\created\folder -wno name_of_your_output_folder`

`name_of_your_output_folder` = name of the folder where you want to save the output, does not require to be created beforehand.

The output will be saved in `path\to\your\folder\name_of_your_output_folder`

## Common Problems and troubleshooting:

### Separating Unicode from bytes:
Python 2 str is equivalent to python 3 bytes and Python 2 Unicode is now Python 3's default string literal. Unicode in Python 2 is implicitly converted to bytes when it is being compared against bytes `b'123' == u'123` will result to `True` in Python 2 whereas in Python 3 this will result to `False`. 

### Division:
In Python 3, all divisions between int values will result into float. If you want an integer division/floor division '//' can be used in both python 2 and 3.

## Additional Resources:
[More on Futurize](https://python-future.org/futurize.html)

[Cheatsheet on writing Python2/3 compatible code](https://python-future.org/compatible_idioms.html)