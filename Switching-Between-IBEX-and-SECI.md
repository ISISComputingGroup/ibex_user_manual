When an existing instrument is migrated to IBEX, the SECI installation is not deleted. This allows the instrument to temporarily switch back to SECI if needed for a particular experiment. During normal hours, you can contact the IBEX team for assistance, but this section will cover how you can carry out this yourself and any matters to watch out for. Please let the IBEX team know of the reason you needed to move back to SECI if they are not already aware.

Switching between SECI and IBEX is possible as they both use the same underlying DAE control software (ISISICP) and sample environment logging database. This means that the run number is preserved etc. as well as other details. 

However, the following points should be born in mind:
- Only swap when in SETUP mode and you are sure any raw/nxs data file has completed being written. The control program writes files asynchronously in the background, so just being in SETUP does not guarantee that file writing has been completed. When in event mode, the file write can happen a while afterwards. So you should check the file from the last run number has appeared on the data archive (Usually d: network drive) before continuing.
- Don't have both SECI and IBEX running at the same time; they will likely try and talk to the same devices
- You may get at least one raw data file containing sample environment data from both SECI and IBEX; this is because a run contains all data from the end of the previous run up until when it ends. If this would cause confusion (maybe there are blocks in SECI and IBEX with the same name that don't mean the same thing), do a BEGIN/END to create a file and so put this data elsewhere.

## Procedure

### If SECI is running and you want to start IBEX:

1. Check that the Instrument is in SETUP and previous run data files saved and copied to an archive.
2. Then close SECI (`File Menu->Exit`).
3. Then to start IBEX Server, use the shortcut in the Windows start menu or run `start_ibex_server.bat` located in `c:\Instrument\Apps\EPICS`. This will close any open IBEX client windows.
4. To start IBEX client, click on the IBEX shortcut in the Windows start menu or the taskbar.

### If IBEX is running and you want to start SECI:

1.	Check that the Instrument is in SETUP and previous run data files saved and copied to an archive.
2.	Then run stop_ibex_server.bat which will either be a shortcut on the Windows Start menu, or you can browse with explorer to `c:\Instrument\Apps\EPICS` where it is located. This will close any open IBEX client windows as well.
3.	Next browse to `c:\Program Files (x86)\STFC ISIS Facility\SECI` where `SECIUserInterface.exe` is located. Click on `SECIUserInterface.exe` to start SECI.

## Post Switch Tasks

- Check and, if necessary, update the RB number, username and run title - either IBEX or SECI may reset this back to what it was last time they were run.
- If you don't wish your next proper run to contain both IBEX and SECI sample environment data, do a short BEGIN/END to push this into a data file to discard.
