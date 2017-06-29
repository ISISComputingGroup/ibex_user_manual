Introduction
============

So far we have run ``genie_python`` commands by entering them via a terminal. However, there may be cases where we want to reuse common sets of commands multiple times. These cases are where creating a script can be very useful.

Creating scripts
================

Python scripts have the extension ``.py``. You can create them from any number of editors. A good editor will do syntax highlighting, and will make it easy to work with Python's indented blocks without accidentally mixing spaces and tabs. Notepad++ is a good choice.

We generally classify scripts as:

1. **Instrument scripts**. These are either aimed at instrument scientists, or put the instrument in a particular state that multiple users may wish to access.
2. **User scripts**. These are scripts that specific users need for particular experiments. They may be reused to an extent but they don't generally need to be accessed quite so readily.

**NOTE**: Ibex puts all configurations and **Instrument scripts** under version control. That means if you change or delete them and want to restore a previous version, you can. The same isn't true for user scripts.

- Instrument scripts are placed in the folder: ``C:\Instrument\Settings\config\NDX[Instrument name]\Python\inst``
- User scripts are placed in the folder: ``C:\scripts``

Exercise 3a
===========

Create two empty scripts:

- An **instrument** script called ``set_up_instrument.py``
- A **user** script called ``run_my_experiment.py``

Writing scripts
===============

When writing scripts, you can use any Python and ``genie_python`` functionality that you've already learnt.

In general, we recommend all executable code within a script should be contained within functions and classes. For example::

    def my_function(arg1, arg2):
         print The first argument is {0}, the second argument is {1}

This gives much greater control over when and how custom code is executed.

Exercise 3b
===========

-   Update your instrument script, ``set_up_instrument.py``, so that it contains a single function

    - The function should be called "set_up_instrument"
    - It should set the title to "My experiment"
    - It should set the username to your name

-   Update your user script, ``run_my_experiment.py`` which contains a function that does the following

    - Begins the run
    - Prints the current uamps for the current period over 10 seconds at 1 second intervals
    - Ends the run

Loading scripts
===============

Once you've created your scripts, you need to make sure they're available to use. This works differently for instrument scripts and user scripts.

- **Instrument scripts** are loaded automatically when you open the scripting perspective
- **User scripts** can be loaded by using the ``load_script`` method in genie_python. For example, ``g.load_script('C:\script\my_script.py')``

**IMPORTANT**: When a script is loaded, Python runs all the commands contained within. We strongly recommend keeping all executable code within functions, so that it runs when you call it rather than executing immediately.


-------------------------------------------------------------------------------

**Next**: [[Converting from OpenGENIE|Ibex-and-genie_python:-Converting-from-OpenGENIE]]
   
**Previous**: [[Common commands|Ibex-and-genie_python:-Common-commands]]