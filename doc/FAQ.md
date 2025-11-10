# FAQ

In this section of the IBEX user manual, we have compiled a list of frequently asked questions.  If your question about IBEX is not answered below, please let us (the Experiment Controls team) know.  If your question is likely to be asked by others, we'll add it to the list.

```{contents} List of Frequently Asked Questions
```

## IBEX Processes and Support

{#report_a_problem}
### How do I report a problem or get help with IBEX?

```{include} contact.mdinc
```

### How do I install IBEX Server?

Please {ref}`contact experiment controls <report_a_problem>` if you need a new installation of the IBEX server.

### How do I install IBEX Client?

To install IBEX Client, see {ref}`installing_ibex_client`.

### How do I view which new IBEX features have been requested or are being worked on?

There are internal lists showing priorities available covering the work which will feed into IBEX, please ask the experiment controls group or your group leader if you need to see these. These lists give you an idea of the long term work, and the priorities at that level.

IBEX is released and deployed to each instrument at least once a year, with patches as required. To see what is being worked on for the next release, you will need to find the most recent PI project on https://github.com/orgs/ISISComputingGroup/projects, note that these are in the format `PI_YYYY_MM`, with the month being the one the PI starts in.

The shortest timescale we consider is a sprint, which is approximately 4 weeks.

There is also a backlog of issues [on GitHub](https://github.com/ISISComputingGroup/IBEX/issues). It is easiest to search for an issue if you already know what you're looking for (e.g. a device name).

## Running IBEX

### How do I start IBEX Server?

To start IBEX Server, see {ref}`starting_ibex_server`.

### How do I stop IBEX Server?

To stop IBEX Server, see {ref}`stopping_ibex_server`.

### What do I look at if there are no RAW frames when Collecting Data?

If when collecting data no raw frames are counted (`Good / Raw` Frames on the dashboard), then:

**Timing is ISIS**
- ISIS may be off (check [ISIS beam status display](https://www.isis.stfc.ac.uk/Pages/beam-status.aspx))
- There may be a problem with the ISIS timing signal. Check other instruments to find out.

**Timing is SMP**
- The chopper may not be spinning, or there is a problem with the signal
    
Consider swapping the DAE timing source to help diagnose the problem. 

### What do I look at if there are no GOOD frames when Collecting Data?

If there are RAW frames but no good frames then the count is being vetoed. Open the DAE perspective and select the Vetoes tab to see what is vetoing the frame. 

- **FIFO veto**: Too many counts in a frame, e.g. noisy detector, jaws opened too wide
- **SMP veto**: Chopper is out of phase with ISIS, or no ISIS signal
- **External veto 0-3**: These are additional beamline-specific vetoes, for example an additional chopper, the shutter or the moderator.

### Can I change what my graphs look like in the log plotter or OPI?

**Yes!** There are lots of settings exposed by the native control. These include graph title, axis font type and size, trace line colour, line type, and line width. To reach these settings for a graph in an OPI do the following:

1. To show the toolbar on an OPI graph right click and select Show/Hide Graph Toolbar.
1. Then click the settings button (leftmost icon with a spanner and screwdriver on it)
1. Click on the tabs to find what you want to change. The graph is the first panel, axes on the second and traces (with a drop down to select for which trace) is on the third.

To open the settings in a log plotter graph; right click and click "Open Properties Panel".

{#faq_find_pv}
### How do I find a specific PV?

PVs in IBEX should all follow the naming convention as specified in {doc}`/concepts/PV-Naming-Conventions`. You can search for PVs that are available on your instrument by using the `Select PV` button in the {ref}`manage_configs_blocks`. Finally, if you can see the value that you want on an OPI you can hover over it to get the PV name or right click and `Show PV Info`.

### How do I set a value to change when I change configuration/component?

This can be accomplished by using {ref}`manage_configs_pv_values`.

### Why are some blocks and their PV addresses greyed-out in the "Edit Configuration" dialogue box?

This is because they are part of a component and can't be edited from a host configuration. To make changes to the master copy, open the relevant component from the menu `Configuration -> Components -> Edit Component`. The name of the component in which the block is defined is shown in the configuration screen. See the note at the bottom of the {ref}`manage_configs_blocks` section for more information.

## Scripting in IBEX

### Can I write scripts to control my experiment?

Yes, you can.  Scripting in IBEX is done using python (with support from a library called `genie_python`).  See {doc}`Scripting` for more details.

### Which version of Python does IBEX use?

IBEX uses a recent version of Python 3 and is periodically updated (at the same time as the rest of IBEX is deployed). To find out the exact version of Python used on a specific instrument, type the following commands at a python shell:

```python
import sys
print(sys.version)
```

### Where can I learn about Python?

Python is the scripting language used by IBEX. If you are new to Python, we suggest you consult the excellent {external+mantid:ref}`introduction_to_python` created by the Mantid team.

`genie_python` is a python library implementing ISIS-specific functions. A {doc}`/scripting/Genie-Python-Training` is available for a general introduction, alongside a more detailed {doc}`listing of common commands </scripting/genie_python-Commands>` and the {external+genie_python:doc}`API reference <genie_python>` for more a more detailed description of specific commands.

### In the scripting view, I don't want the arguments when I autocomplete

In the scripting console type `g.` will show a list of possible `genie_python` commands. If you select one of these or type to narrow down the possibilities, pressing return will autocomplete the method name including the parameters. However, sometimes you will not want all the parameters, so instead of pressing `<return>` press `<ctrl> + <return>`, this will give only the function name without any parentheses or arguments.

### When I load script I get an error complaining about `unicodeescape`

If you try to load a script and you get the following error:

```
>>> g.load_script('c:\scripts\NiceScript.py')
  File "<ipython-input-7-c5705547e6ca>", line 1
    g.load_script('c:\scripts\NiceScript.py')
                  ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 10-11: malformed \N character escape
```

The problem is that the string has not been escaped correctly. In python, the backslash character, `\`, is an {external+python:ref}`escape character <escape-sequences>`, used to create special characters. In this command, the `\N` is the beginning of a {abbr}``unicode escape sequence (The intended usage of this sequence is, for example, \N{LATIN CAPITAL LETTER A})``. You can either:

- Place an `r` before the string (called a {external+python:ref}`raw string <raw-strings>`)
  - `g.load_script(r'c:\\scripts\\NiceScript.py')`
- {external+python:ref}`Escape<escape-sequences>` the backslashes
  - `g.load_script('c:\\scripts\\NiceScript.py')`
- Use the default script path:
  - `g.load_script('NiceScript.py')`

### Can I run scripts from Mantid?

`genie_python` - the library which provides convenience functions such as `cset` and `cget` in order to run scripts can be installed from `pip`, and is [available on pypi](https://pypi.org/project/genie-python/). 
