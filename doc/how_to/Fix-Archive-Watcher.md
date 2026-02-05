Fix Archive Watcher
###################

The archive watcher program runs on an analysis computer and copies data files to a local directory.  To fix it after the password change on the NDX computer you need to:
- stop the archive watcher service and disable it, via task manager or services.msc
- copy `archive_watcher.exe`, `archive_watcher.pdb` and `vc_redist.x64.exe` from `\\isis\shares\ISIS_Experiment_Controls_Public\archive_watcher` to `c:\Program Files (x86)\STFC ISIS Facility\ISIS Archive Watcher`
- run `vc_redist.x64.exe`
- map a network drive to `data$` on your instrument e.g. for GEM you would map a network drive to `\\ndxgem\data$`. In thsi case use `ndxgem\spudulike` as username and your new spudulike password for this drive mapping
- run `archive_water.exe` in `c:\Program Files (x86)\STFC ISIS Facility\ISIS Archive Watcher` interactively to test
- create a shortcut in the user logon startup `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
