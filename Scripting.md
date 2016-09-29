Scripting
=========

Scripting in IBEX is done using genie_python. The [genie_python reference manual] (http://shadow.nd.rl.ac.uk/genie_python/sphinx/genie_python.html ) gives a full account of what functions are available in genie_python. This page is intended to give a broad guide to scripting for the beginner and novice user.

- [Running genie commands](#running-genie-commands)
- [Common genie commands](#common-genie-commands)
- [Converting Open Genie to `genie_python`](#converting-open-genie-to-genie-python)
- [Creating and running instrument scripts](#creating-and-running-instrument-scripts)
- [Creating and running user scripts](#creating-and-running-user-scripts)
- [Tips from the developers](#tips-from-the-developers)

Running genie commands
======================

When running `genie_python` from an interactive console such as from the GUI or after running `C:\Instrument\Apps\Python\genie_python.bat`, the `genie` module will be aliased to `g`. Genie commands can then be accessed by using the prefix `g.[COMMAND_NAME]`. For example:

```
g.start()
g.cset("BLOCK_1",1)
g.abort()
```

This is particularly useful from the GUI which will auto-complete commands and provide tool tips describing each function and its arguments.

Note that in many cases, arguments will be optional. For instance, `begin` can be used as `g.begin()` despite supporting all of the arguments `period`, `meas_id`, `meas_type`, `meas_subid`, `sample_id`, `delayed`, `quiet`, `paused`, and `verbose`.

Common genie commands
=====================

Many `genie_python` commands share the same name with their Open Genie equivalent so it will often be very straightforward to find the function you're looking for. Still, here is a list of the most commonly used `genie_python` commands. This is **not a complete list**. For full information, consult the [genie_python reference manual] ( http://shadow.nd.rl.ac.uk/genie_python/sphinx/genie_python.html ).

Starting and stopping a run
---------------------------

| Command | Description                                      | Example    |
|---------|--------------------------------------------------|------------|
| begin   | Starts a new run                                 | g.begin()  |
| end     | Ends the current run                             | g.end()    |
| abort   | Aborts the current run                           | g.abort()  |
| pause   | Pauses the current run                           | g.pause()  |
| resume  | Resumes the current run after it has been paused | g.resume() |

Updating blocks and PVs
-----------------------

| Command | Description                                          | Example                               |
|---------|------------------------------------------------------|---------------------------------------|
| cget    | Gets the useful values associated with a block       | g.cget("NEW_BLOCK")                   |
| cset    | Sets the setpoint and runcontrol settings for blocks | g.cset("NEW_BLOCK",1)                 |
| get_pv  | Get the value for the specified PV                   | g.get_pv("IN:INSTNAME:IOC_01:STAT")   |
| set_pv  | Set the value for the specified PV                   | g.set_pv("IN:INSTNAME:IOC_01:STAT",1) |


Run control
----------

| Command | Description                                                                                    | Example                               |
|------------------|---------------------------------------------------------------------------------------|---------------------------------------|
| get_uamps        | Get the current number of micro-amp hours                                             | g.get_uamps() |
| get_frames       | Gets the current number of good frames                                                | g.get_frames() |
| get_runstate     | Get the current status of the instrument as a string                                  | g.get_runstate() |
| get_mevents      | Gets the total counts for all the detectors                                           | g.get_mevents() |
| get_totalcounts  | Get the total counts for the current run                                              | g.get_totalcounts() |
| waitfor          | Interrupts execution until certain conditions are met                                 | g.waitfor("NEW_BLOCK",value=1) |
| waitfor_block    | Interrupts execution until block reaches specific value                               | g.waitfor_block("NEW_BLOCK",1) |
| waitfor_time     | Interrupts execution for a specified amount of time                                   | g.waitfor_time(1) |
| waitfor_frames   | Interrupts execution to wait for number of total good frames to reach parameter value | g.waitfor_frames(1000) |
| waitfor_uamps    | Interrupts execution to wait for a specific total charge                              | g.waitfor_uamps(9.9) |
| waitfor_runstate | Wait for a particular instrument run state                                            | g.waitfor_runstate("paused") |
| waitfor_move     | Wait for all motion or specific motion to complete                                    | g.waitfor_move("NEW_BLOCK") |

Converting Open Genie to genie_python
=====================================

[TODO]

Creating and running instrument scripts
=======================================

[TODO]

Creating and running user scripts
=================================

Creating scripts
----------------

1. First, we need to create a script file. By default, user scripts should be placed in `C:\scripts`. Navigate to your desired directory and create the script file with extension `.py`.
2. Write some `genie_python`!
3. Save the file

We have glossed over step 2 because Python is a very powerful scripting language. Combined with Open Genie, the potential scope of a script is enormous, and well beyond the scope of this guide. For example though, here is a simple script that executes a calibration run.

```
# Change the title
calibration_run_title = "Calibration run 1, 29th September"
g.change(title=calibration_run_title)

# Begin the run
print "Beginning calibration run : " + calibration_run_title
g.begin()

# Wait for 100 uamps
g.waitfor(uamps=100)

# End the run
g.end()
print "Calibration run finished successfully"
```

Running
-------

Once you've created your script, it's time to run it. There are a number of ways of launching a Python script.

### From Ibex

1. Launch the Ibex GUI 
1. Navigate to the scripting perspective
1. Run the command `g.load_script("C:\path\to\script\my_script.py")` where the path and script name are updated appropriately
    - Note that if you omit the absolute path to the file (i.e. `C:\path\to\script`) then `genie_python` will look in the current script directory. By default this is `C:\scripts` but can be viewed and set with the commands `g.get_script_dir()` and `g.set_script_dir()` respectively.
1. When the script is loaded, any procedures in the script will be run automatically. If the script contains any function, you will now be able to call them from within the scripting window.

### From a genie_python terminal

1. Launch a `genie_python` terminal from `C:\Instrument\Apps\Python\` by running `genie_python.bat`
1. Follow the above starting at step 3.

Tips from the developers
========================

Argument ordering
-----------------

As this is Python, `genie_python` conforms to the standard pattern of calling Python functions. The arguments to the function are contained within brackets and the variables passed in as a comma-separated list. Ordering is important but can be overridden by using named variables, for instance the following are all correct and equivalent:

```
g.change_beamline_pars("PAR1",1)
g.change_beamline_pars(name="PAR1",value=1)
g.change_beamline_pars(value=1,name="PAR1")
g.change_beamline_pars("PAR1",value=1)
```

In the last example, named and unnamed variables are mixed. Unnamed variables must precede named variables. The following examples are not valid

```
g.change_beamline_pars(name="PAR1",1) # Named variable before unnamed
g.change_beamline_pars(1,"PAR1") # Cannot change order of unnamed variables
```

Using named variables can be **very useful in avoiding mistakes**. For instance, getting the order of high and low limits the wrong way round. For instance this example:

```
g.change_monitor(1,10,0)
```

is wrong and wouldn't work. Instead, we could have written:

```
g.change_monitor(1,high=10,low=0)
```

which would have work and makes it clear for whoever comes to edit the code in future.