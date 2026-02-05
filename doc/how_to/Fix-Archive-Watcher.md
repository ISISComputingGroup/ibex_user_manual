# Upgrade Archive Watcher

The archive watcher program runs on an analysis computer and copies data files to a local directory. 

To install/upgrade it on an NDX computer:
- Stop the archive watcher service and disable it via task manager or `services.msc`
- Copy `archive_watcher.exe`, `archive_watcher.pdb`, `*.dll` and `vc_redist.x64.exe` from `\\isis\shares\ISIS_Experiment_Controls_Public\archive_watcher` to `c:\Program Files (x86)\STFC ISIS Facility\ISIS Archive Watcher`
- Run `vc_redist.x64.exe`
- Either map a network drive to `data$` on your instrument e.g. for GEM you would map a network drive to `\\ndxgem\data$`, or just type e.g. `\\ndxgem\data$` and check the "save credentials" box. In this case use `ndxgem\spudulike` as username and the NDX\spudulike password for the drive mapping
- You will likely need to adjust permissions on the directory files are copied to, see `archive_watcher.properties` for this, but it is likely somewhere like `c:\data`. The service would have run as `inst_mgr` but you now need to add the account the PC is logged in as to have permission.
- Run `archive_water.exe` in `c:\Program Files (x86)\STFC ISIS Facility\ISIS Archive Watcher` interactively to test
- Look at `archive_watcher.log` in `%TEMP%` and check for errors
- Create a shortcut to `archive_watcher.exe` in the user logon startup `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
