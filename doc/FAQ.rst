FAQ
###

In this section of the IBEX user manual, we have compiled a list of frequently asked questions.  If your question about IBEX is not answered below, please let us (the Experiment Controls team) know.  If your question is likely to be asked by others, we'll add it to the list.

.. contents:: **List of Frequently Asked Questions**

IBEX Processes and Support
==========================

.. _report_a_problem:

How do I report a problem or get help with IBEX?
------------------------------------------------

**A:** For a non-urgent issue use the `Instrument Problem/Bug Report <http://sparrowhawk.nd.rl.ac.uk/footprints/?product=PC%20Instrument%20Control&amp;format=pcinst>`_ page or email ISISExperimentControls@stfc.ac.uk

When reporting a problem, it is helpful to include the version numbers of your IBEX Client and Server in your report.  To view the version numbers select ``Help > About`` from the menu bar in the IBEX Client.

For urgent issues call **1763** (RAL site landline or ZOOM phone) or **01235394488**
 
How do I install IBEX Server?
-----------------------------

To install the IBEX Server - see :ref:`installing_ibex_server`.

How do I install IBEX Client?
-----------------------------

To install IBEX Client - see :ref:`installing_ibex_client`.

Can I run IBEX and SECI at the same time?
-----------------------------------------

In a word - No.  Running two control programs on any system is a bad idea - which program has control?  If you were to run IBEX and SECI on the same system, the two would contend for control of individual devices.  It would not be clear which device was controlled by which program.  The results would be unpredictable.

Which version of Python does IBEX use?
--------------------------------------

IBEX currently uses Python 3.11.2. 

Where can I learn about Python?
-------------------------------

Python is the scripting language used by IBEX. `genie_python` is a python library implementing ISIS-specific functions. If you are new to Python, we suggest you consult the excellent :external+mantid:ref:`introduction_to_python` created by the Mantid team.


How do I view which new IBEX features have been requested or are being worked on?
---------------------------------------------------------------------------------

There are internal lists showing priorities available covering the work which will feed into IBEX, please ask the experiment controls group or your group leader if you need to see these. These lists give you an idea of the long term work, and the priorities at that level.
IBEX is released and deployed to each instrument at least once a year, with patches as required. To see what is being worked on for the next release, you will need to find the most recent PI project on https://github.com/orgs/ISISComputingGroup/projects, note that these are in the format PI_YYYY_MM, with the month being the one the PI starts in.
The shortest time scale we consider is a sprint, and you can view this information on github at https://github.com/ISISComputingGroup/IBEX/projects/1.
There is also a long list of issues on github that can be viewed at https://github.com/ISISComputingGroup/IBEX/issues. Please note, this is a rather long list and not very friendly to browse through unless you already know what you're looking for (e.g. a device name).


Running IBEX
============

How do I start IBEX Server?
---------------------------

To start IBEX Server - see :ref:`starting_ibex_server`.

How do I stop IBEX Server?
--------------------------

To stop IBEX Server - see :ref:`stopping_ibex_server`.

Can I switch from running IBEX to SECI and vice-versa?
------------------------------------------------------

Yes, it is possible to switch from running IBEX to SECI or to switch from SECI to IBEX, but you have to be careful. See :doc:`obsolete/Switching-Between-IBEX-and-SECI` for details.

Can I write scripts to control my experiment?
---------------------------------------------

Yes, you can.  Scripting in IBEX is done using python (with support from a library called genie_python).  See :doc:`Scripting` for more details.

What do I look at if there are no RAW frames when Collecting Data?
------------------------------------------------------------------

If when collecting data no raw frames are counted (see `Good / Raw` Frames on the dashboard) then:

Timing is ISIS:
    Either ISIS is off, or there is a problem with the ToF (ISIS) signal. Check other instruments to find out.

Timing is SMP:
    Chopper is not spinning, or there is a problem with the signal
    
Consider swapping the timing source to help diagnose the problem. 

What do I look at if there are no GOOD frames when Collecting Data?
-------------------------------------------------------------------

If there are RAW frames but no good frames then the count is being vetoed. Open the DAE perspective and select the Vetoes tab to see what is vetoing the frame. 

FIFO veto:
    Too many counts in a frame, e.g. noisy detector, jaws opened too wide

SMP veto:
    chopper out of phase with ISIS, or no ISIS signal

External veto{0-3}:
    could be an additional chopper, the shutter or moderator

Can I change what my graphs look like in the log plotter or OPI?
----------------------------------------------------------------

**Yes!** There are lots of setting exposed by the native control. These include graph title, axis font type and size, trace line colour, line type, and line width. To reach these settings for a graph in an OPI do the following:

#. To show the toolbar on an OPI graph right click and select Show/Hide Graph Toolbar.
#. Then click the settings button (leftmost icon with a spanner and screwdriver on it)
#. Click on the tabs to find what you want to change. The graph is the first panel, axes on the second and traces (with a drop down to select for which trace) is on the third.

To open the settings in a log plotter graph, just right click and click "Open Properties Panel".

.. _faq_find_pv:

How do I find a specific PV?
----------------------------

PVs in IBEX should all follow the naming convention as specified in :doc:`/concepts/PV-Naming-Conventions`. You can search for PVs that are available on your instrument by using the `Select PV` button in the :ref:`manage_configs_blocks`. Finally, if you can see the value that you want on an OPI you can hover over it to get the PV name or right click and `Show PV Info`.

How do I set a value to change when I change configuration/component?
---------------------------------------------------------------------

This can be accomplished by using :ref:`manage_configs_pv_values`.

Why are some blocks and their PV addresses greyed-out in the "Edit Configuration" dialogue box?
-----------------------------------------------------------------------------------------------

This is because they are part of a `component` and can't be edited from a host configuration.  To make changes to the "master" copy, open the relevant component from the menu `Configuration -> Components -> Edit Component`.  See the note at the bottom of the :ref:`manage_configs_blocks` section for more information.


Scripting in IBEX
=================

In the scripting view I don't want the arguments when I autocomplete
--------------------------------------------------------------------

In the scripting console type `g.` will show a list of possible genie_python commands. If you select one of these or type to narrow down the possibilities, pressing return will autocomplete the method name including the parameters. However, sometimes you will not want all the parameters, so instead of pressing <return> press <crtl> + <return>, this will give only the function name without any parenthesis or arguments.

When I load script I get an error complaining about unicodeescape
-----------------------------------------------------------------

If you try to load a script and you get the following error:

.. code-block::

    >>> `g.load_script('c:\scripts\NiceScript.py')`
      File "<ipython-input-7-c5705547e6ca>", line 1
        g.load_script('c:\scripts\NiceScript.py')
                      ^
    SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 10-11: malformed \N character escape

The problem is you have not escaped the string correctly, in python the slash character, `\\`, is an escape character used to create things like newline characters. In this command, the `\\N` is a newline character and is causing python trouble. You can either:

#. Place an `r` before the string (called a raw string) this makes it ignore escapes except for quote marks
    - `g.load_script(r'c:\\scripts\\NiceScript.py')`
#. Escape the slashes
    - `g.load_script('c:\\\\scripts\\\\NiceScript.py')`
#. Just use the default script path so:
    - `g.load_script('NiceScript.py')`

Can I run scripts from Mantid?
-----------------------------------------------------------------

`genie_python` - the library which provides convenience functions such as `cset` and `cget` in order to run scripts can be installed from `pip`, and is available on pypi under https://pypi.org/project/genie-python/ . 