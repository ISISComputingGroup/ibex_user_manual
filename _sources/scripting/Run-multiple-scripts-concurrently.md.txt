# Running multiple scripts concurrently

For some use-cases, it may be useful to have a script running 'in the background' performing some process, while
leaving the main scripting console free for user scripts. IBEX supports this with multiple approaches, depending
on your needs.

In general, only one script controlling data acquisition should be running. Other scripts should only monitor
a separate, standalone process.

## Standalone python session

For simple one-off scripts (e.g. those that are only useful for one experiment), a standalone python session can be
started using the script in:
```
c:\Instrument\Apps\Python3\genie_python.bat
```

This gives a python shell independent from the scripting console in the GUI, but with equivalent functionality.

:::{important}
Scripts started using this approach will need to be **manually** restarted if IBEX server or the NDX computer is
restarted.
:::

## Background script IOC

For more permanent use-cases, a dedicated background script IOC is available. This IOC starts and stops with IBEX
server, which means it will automatically restart if IBEX server restarts.

To set up this IOC, you need to:
- Create a `background_script.py` file in `c:\instrument\settings\config\<instrument>\Python\background_script.py`
- [Add the `BGRSCRPT` ioc to the IBEX configuration](../how_to/Create-and-Manage-Configurations)

The `background_script.py` file should generally run forever and register itself as having started - a typical way to do structure it is:

```python
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.environ["EPICS_KIT_ROOT"], "ISIS", "inst_servers", "master")))

from server_common.helpers import register_ioc_start

register_ioc_start("BGRSCRPT_01")


while True:
    do_some_process()

    # Sleep to avoid using 100% CPU
    time.sleep(1)
```

```{seealso}
{external+ibex_developers_manual:doc}`specific_iocs/other/Background-Script-IOC` in the developer's manual.
```
