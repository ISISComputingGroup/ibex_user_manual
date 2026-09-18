Scripting
#########

Introduction
============

So far we have run ``genie_python`` commands by entering them via a terminal. However, there may be cases where we want to reuse common sets of commands multiple times. These cases are where creating a script can be very useful.

Creating scripts
================

Python scripts have the extension ``.py``. You can create them from any number of editors. A good editor will do syntax highlighting, and will make it easy to work with Python's indented blocks without accidentally mixing spaces and tabs. Notepad++ is a good choice.

We generally classify scripts as:

1. **Instrument scripts**. These are either aimed at instrument scientists, or put the instrument in a particular state that multiple users may wish to access.
2. **User scripts**. These are scripts that specific users need for particular experiments. They may be reused to an extent but they don't generally need to be accessed quite so readily.

**NOTE**: IBEX puts all configurations and **Instrument scripts** under version control. That means if you change or delete them and want to restore a previous version, you can. The same isn't true for user scripts.

- Instrument scripts are located in: ``C:\Instrument\Settings\config\NDX[Instrument name]\Python\inst``
- User scripts are located in: ``C:\scripts``

.. _gp_and_ibex_ex3:

Exercise 3a
-----------

Create two empty scripts:

- An **instrument** script called ``set_up_instrument.py``
- A **user** script called ``run_my_experiment.py``

:doc:`Solution<genie_python-and-IBEX-(Exercise-solutions)>`

Writing scripts
===============

When writing scripts, you can use any Python and ``genie_python`` functionality that you've already learnt. **In instrument scripts, you must have this as your first line:**

.. code-block:: python

    from genie_python import genie as g, BLOCK_NAMES as b

In general, we recommend all executable code within a script should be contained within functions and classes. For example:

.. code-block:: python

    def my_function(arg1, arg2):
         print "The first argument is {0}, the second argument is {1}".format(arg1, arg2)

This gives much greater control over when and how custom code is executed.

Exercise 3b
-----------

-   Update your instrument script, ``set_up_instrument.py``, so that it contains a single function

    - The function should be called "set_up_instrument"
    - It should set the title to "My experiment"
    - It should set the username to your name

-   Update your user script, ``run_my_experiment.py`` which contains a function that does the following

    - Begins the run
    - Prints the current uamps for the current period over 10 seconds at 1 second intervals
    - Ends the run

:ref:`Solution<gp_and_ibex_ex3_solution>`

Loading scripts
===============

Once you've created your scripts, you need to make sure they're available to use. This works differently for instrument scripts and user scripts.

- **Instrument scripts** are loaded automatically when you open the scripting perspective
- **User scripts** can be loaded by using the ``load_script`` method in genie_python. For example, ``g.load_script('C:\scripts\run_my_experiment.py')``. ``g.load_script`` looks automatically in ``C:\scripts``. A full path can be given for other locations


**IMPORTANT**: When a script is loaded, Python runs all the commands contained within. We strongly recommend keeping all executable code within functions, so that it runs when you call it rather than executing immediately.

Exercise 3c
-----------

Load your user script ``run_my_experiment.py``

:ref:`Solution<gp_and_ibex_ex3_solution>`

Running scripts
===============

Instrument scripts
------------------

Methods defined in instrument scripts are available via the ``inst`` namespace. For example, if we define a method called ``my_method`` in an instrument script which takes 1 argument, a block name, then I can make it run in the scripting perspective by entering:

.. code-block:: python

    inst.my_method("MY_BLOCK")

As with ``genie_python`` commands, the IBEX scripting perspective will provide auto-completion for instrument methods so you can see what is available

Exercise 3d
-----------

Run the instrument method you wrote in exercise 3b

:ref:`Solution<gp_and_ibex_ex3_solution>`

User scripts
------------

Functions loaded from user scripts using the ``g.load_script(...)`` command will be available to call like any other user-defined function. For example, if I defined a function ``my_function``:

.. code-block:: python

    g.load_script("my_script_file.py")
    my_function()

Exercise 3e
-----------

Run the user script method you wrote in exercise 3b

:ref:`Solution<gp_and_ibex_ex3_solution>`

Modifying scripts
=================

Every new scripting perspective will be a clean slate; any previously loaded scripts will be forgotten. A new scripting perspective is opened each time IBEX is started, but your scripting session will be preserved if you switch between views without closing the client.

Sometimes you might want to change a script and update it without having to change scripting terminal.

- Instrument scripts: Run the command ``reload(inst)``
- User scripts: Run ``g.load_script("C:\scripts\file_to_reload.py")`` with the appropriate file name

Exercise 3f
-----------

- Modify your instrument script to output the current at 0.1 second intervals
- Reload the script
- Run it again and confirm the behaviour has changed

:ref:`Solution<gp_and_ibex_ex3_solution>`

Using functions from other files
================================

You may want to call a function from one file in another file.

Calling an instrument function from a different instrument script
-----------------------------------------------------------------

It is recommended that you ``import`` it using standard Python rather than trying to call it with the ``inst.`` because you don't know the order in which the scripts are loaded. For example, if I have one instrument script, ``counts.py``:

.. code-block:: python

    def vanadium(title, duration):
        g.change_title(title)
        g.begin()
        g.waitfor_time(seconds=duration)
        g.end()

and another called ``calibrate.py`` that uses the ``vanadium`` function then I would write:

.. code-block:: python

    from counts import vanadium
    def calibration():
        for title, duration in [("10 second run", 10), ("1 minute run", 60), ("1 hour run", 3600)]:
            vanadium(title, duration)

Calling an instrument function from a user script
-------------------------------------------------

Here you can just use ``inst.`` prefix, for example ``inst.my_function(arg1, arg2)``

Calling a user function from an instrument script
-------------------------------------------------

This is feasible, but generally not recommended. The user script won't be kept in version control like the instrument script and could be moved or changed unexpectedly.

Calling a user function from a different user script
----------------------------------------------------

The same as calling a function in one instrument script from another.

.. _gp_and_ibex_ex4:

Exercise 4
==========

-   Create a new instrument script containing a function

    - The function sets the title to "Ramping [block name] from [initial value] to [final value]"
    - The block name, initial and final values should all be provided as input arguments
    - The method begins a run and then changes the value of the block incrementally in steps of size 1
    - Once the target is reached, the method ends the run

-   Put a line at the top of your instrument script **outside the function definition** that prints the current title

-   Create a new user script containing a function

    - The function runs the new instrument script on two different blocks

-   Load and run your new user-script function
-   When was the print statement at the top of your instrument script executed?

:ref:`Solution<gp_and_ibex_ex4_solution>`
