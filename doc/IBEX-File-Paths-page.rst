Where is ...?
#############

The installation of IBEX is common for most instruments you shouldn't need to delve into the paths as a user but as an instrument scientist there may be some items you wish to edit or look at. The system is set out as follows:

* IBEX Client: ``C:\Instrument\Apps\Client_E4\ibex-client.exe`` there should be a shortcut on the task bar

* IBEX Server: ``C:\Instrument\Apps\EPICS`` to start and stop the server; see :doc:`introduction/Starting-and-Stopping-IBEX`.

* genie_python: ``C:\Instrument\Apps\Python3\genie_python.bat`` usually python is accessed through the client scripting console

* Configurations: ``C:\Instrument\Settings\config\<computer>\configurations`` this directory contains configuration, components and IOC specific configuration. The IOC specific configurations include:

  - galil: ``galil`` galil motor configurations for all controllers, including jaws, axes and motion setpoint commands but not value
  - motion setpoints: ``motionSetPoints`` the motion setpoints
  - refl: ``refl\config.py`` default reflectometry configuration
  - DAE tables: ``tables`` contains wiring, spectra and detector tables for the DAE
  - TCB files: ``tcb`` contains the tcb files

* Common calibration files: ``C:\Instrument\Settings\config\common`` calibration files for instruments e.g. Eurotherm sensors

* Log files: These are in various places depending on the source see :external+ibex_developers_manual:doc:`iocs/troubleshooting/Log-file-location` on the developer's manual.

* User scripts: instrument dependent often in ``c:\scripts``

* Instrument scripts: ``C:\Instrument\Settings\config\<computer>\Python`` version controlled instrument scripts which are accessed through ``inst.``. Either as a single file called ``inst.py`` or a folder called ``inst``

* Shared instrument scripts: ``C:\Instrument\scripts`` these are scripts shared between multiple instruments `see shared instrument scripts <https://github.com/ISISNeutronMuon/InstrumentScripts/wiki>`_

* Data: ``C:\data`` the data recorded by the instrument


