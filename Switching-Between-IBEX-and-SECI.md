When an existing instrument is migrated to IBEX, the SECI installation is not deleted which allows the instrument to temporarily switch back to SECI if needed for a particular experiment. During normal hours, you can contact the IBEX team for assistance, but this section will cover how you can carry out this yourself and any matters to watch out for. Please let the IBEX team know of the reason you needed to move back to SECI if they are not already aware.

Switching between SECI and IBEX is possible as they both use the same underlying DAE control software (ISISICP) and sample environment logging database. This means that the run number is preserved etc. as well as other details. However the following points should be born in mind:
* only swap when in SETUP mode and you are sure any data file has completed being written. The control program writes files asynchronously in the background so being in SETUP is not a guarantee file writing has completed - in event mode the file write can be a while afterwards. So you should check the last file has appeared on the archive before continuing.
* Don't have both SECI and IBEX running at the same time, they will likely both try and talk to the same devices
* 

Procedure

* If SECI is running, close SECI (File Menu + Exit) or run **KillSECI**. If IBEX is running (or you are not sure) run **stop_ibex_server.bat** which will either be a shortcut on the Windows "Start" menu or you can browse with explorer to c:\\Instrument\\apps\\EPICS where it is located
* To start SECI use either the SECI shortcut in your windows Start menu, or browse to  **c:\\Program Files (x86)\\STFC ISIS Facility\\SECI** where **SECIUserInterface.exe** is located
* To start IBEX either use the shortcut in the Windows start menu or run **start_ibex_server.bat** located in  **c:\\Instrument\\apps\\EPICS**