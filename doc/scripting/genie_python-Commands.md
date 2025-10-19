# Genie Python Commands

## Running `genie_python` commands

When running python from an interactive console such as from
the GUI, or after running `C:\Instrument\Apps\Python3\genie_python.bat`,
the `genie` module will be aliased to `g`. Genie commands can then
be accessed by using the prefix `g.[COMMAND_NAME]`. For example:

```python
g.begin()
g.cset("BLOCK_1", 1)
g.abort()
```

This is particularly useful from the GUI which will auto-complete
commands and provide tool tips describing each function and its
arguments.

For user or instrument scripts, the standard way of importing `genie_python` is:

```python
from genie_python import genie as g
```

Note that in many cases, arguments will be optional. For instance,
{external+genie_python:py:obj}`g.begin <genie.begin>` can be used as `g.begin()`, despite additionally supporting optional
arguments including `period`, `meas_id`, `meas_type`, `meas_subid`,
`sample_id`, `delayed`, `quiet`, `paused`, and `verbose`.

## Common `genie_python` commands

Some commonly used `genie_python` commands are listed below.

This is **not a complete list**; For full  information, consult the {external+genie_python:doc}`genie_python reference manual <genie_python>`.
Click on a command name below to view the detailed documentation for that command in the reference manual.

### Starting and stopping a run

| Command                                               | Description                              | Example      |
|-------------------------------------------------------|------------------------------------------|--------------|
| {external+genie_python:py:obj}`begin <genie.begin>`   | Starts a new run                         | `g.begin()`  |
| {external+genie_python:py:obj}`end <genie.end>`       | Ends the current run (saving data)       | `g.end()`    |
| {external+genie_python:py:obj}`abort <genie.abort>`   | Aborts the current run (discarding data) | `g.abort()`  |
| {external+genie_python:py:obj}`pause <genie.pause>`   | Pauses the current run                         | `g.pause()`  |
| {external+genie_python:py:obj}`resume <genie.resume>` | Resumes the current run after it has been paused                         | `g.resume()` |

### Updating blocks and PVs

| Command                                               | Description                                                        | Example                                |
|-------------------------------------------------------|--------------------------------------------------------------------|----------------------------------------|
| {external+genie_python:py:obj}`cget <genie.cget>`     | Gets the useful values associated with a block                     | `g.cget("NEW_BLOCK")`                  |
| {external+genie_python:py:obj}`cset <genie.cset>`     | Sets the setpoint, and optionally runcontrol settings, for a block | `g.cset("NEW_BLOCK",1)`                |
| {external+genie_python:py:obj}`get_pv <genie.get_pv>` | Gets the value of the specified PV                                 | `g.get_pv("IN:INSTNAME:IOC_01:STAT")`  |
| {external+genie_python:py:obj}`set_pv <genie.set_pv>` | Sets the value of the specified PV                                 | `g.set_pv("IN:INSTNAME:IOC_01:STAT",1)` |

### Run control

| Command                                                                   | Description                                                                                                                                                                                                | Example                          |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| {external+genie_python:py:obj}`get_uamps <genie.get_uamps>`               | Gets the number of micro-amp hours of beam collected in the current run                                                                                                                                    | `g.get_uamps()`                  |
| {external+genie_python:py:obj}`get_frames <genie.get_frames>`             | Gets the number of {abbr}`good frames (Pulses which were counted, not counting any pulses that were ignored due to hardware vetoes or software run-control settings)` of beam collected in the current run | `g.get_frames()`                 || {external+genie_python:py:obj}`get_runstate <genie.get_runstate>` | Gets the current status of the instrument as a string | `g.get_runstate()` |
| {external+genie_python:py:obj}`get_mevents <genie.get_mevents>`           | Gets the total counts for all the detectors, in millions of events.                                                                                                                                        | `g.get_mevents()`                |
| {external+genie_python:py:obj}`get_totalcounts <genie.get_totalcounts>`   | Gets the total counts for all the detectors.                                                                                                                                                               | `g.get_totalcounts()`            |
| {external+genie_python:py:obj}`waitfor <genie.waitfor>`                   | Waits until certain conditions are met.                                                                                                                                                                    | `g.waitfor("NEW_BLOCK",value=1)` |
| {external+genie_python:py:obj}`waitfor_block <genie.waitfor_block>`       | Waits until block reaches specific value.                                                                                                                                                                  | `g.waitfor_block("NEW_BLOCK",1)` |
| {external+genie_python:py:obj}`waitfor_time <genie.waitfor_time>`         | Waits for a specified amount of time.                                                                                                                                                                      | `g.waitfor_time(seconds=1)`      |
| {external+genie_python:py:obj}`waitfor_frames <genie.waitfor_frames>`     | Waits for the number of total good frames collected in the current run to reach the specified total value.                                                                                                 | `g.waitfor_frames(5000)`         |
| {external+genie_python:py:obj}`waitfor_uamps <genie.waitfor_uamps>`       | Waits for the number of total micro-amp hours collected in the current run to reach the specified total value.                                                                                             | `g.waitfor_uamps(5.0)`           |
| {external+genie_python:py:obj}`waitfor_runstate <genie.waitfor_runstate>` | Waits for a particular instrument run state.                                                                                                                                                               | `g.waitfor_runstate("PAUSED")`   |
| {external+genie_python:py:obj}`waitfor_move <genie.waitfor_move>`     | Waits for all motion, or specified motion axes, to complete.                                                                                                                                               | `g.waitfor_move()`               |

## Toggling options

Various options can be toggled using the {external+genie_python:py:obj}`genie_toggle_settings` module.

For example, toggling the verbosity of all calls to a command using {external+genie_python:py:obj}`toggle.cset_verbose(True) <genie_toggle_settings.cset_verbose>`. This can be convenient, as there will be no need to explicitly set `verbose=True` for each `cset` call.

There are also advanced options such as {external+genie_python:py:obj}`toggle.exceptions_raised(True) <genie_toggle_settings.exceptions_raised>`, which will allow exceptions to propagate instead of genie handling them, in case you want to handle exceptions yourself.

```{warning}
If you have `exceptions_raised` toggled to True and there is an exception within `genie_python`, it will stop your script from running unless you catch the exception yourself.
```

## Running in simulation mode

Genie_python supports a basic simulation mode; see {doc}`Simulating-Scripts` for how to use this.
