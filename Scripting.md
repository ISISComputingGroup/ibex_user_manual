Scripting
=========

Scripting in IBEX is done using genie_python. The [genie_python reference manual] http://shadow.nd.rl.ac.uk/genie_python/sphinx/genie_python.html ) gives a full account of what functions are available in genie_python. This page is intended to give a broad guide to scripting for the beginner and novice user.

Running genie commands
======================

When running `genie_python` from an interactive console such as from the GUI or after running `C:\Instrument\Apps\Python\genie_python.bat`, the `genie` module will be aliased to `g`. Genie commands can then be accessed by using the prefix `g.[COMMAND_NAME]`. For example:

```
g.start()
g.cset("BLOCK_1",1)
g.abort()
```

This is particularly useful from the GUI which will auto-complete commands and provide tool tips describing each function and its arguments.

Most common genie commands
==========================

[TODO]

Converting Open Genie to genie_python
=====================================

[TODO]

Creating and running instrument scripts
=======================================

[TODO]

Creating and running user scripts
=================================

[TODO]