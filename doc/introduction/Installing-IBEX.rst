Installing IBEX
###############

.. contents:: **Contents**

.. _installing_ibex_client:

Installing IBEX Client
----------------------

Installation of IBEX client on a PC is simple and straightforward.

Pre-requisites for running IBEX Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The IBEX client is designed to run on Windows 10, and so long as that is up to date that should be enough for the client.
It may run on Windows 11, but there is no support for that at present.
It can run on Linux, and there is a build available for use on IDAAS, it is not supported in other Linux environments at present.


Installation
~~~~~~~~~~~~

There is a network drive location that the experiment controls group can direct you to.

.. _installation_layout:

Installation Layout
-------------------

After installation, the current paths are used by the various components.

+-------------------------------------------------------+-------------------------------------------------------------------+
| Item                                                  | Path                                                              |
+=======================================================+===================================================================+
|IBEX Client                                            |  ``C:\Instrument\Apps\Client_E4``                                 | 
+-------------------------------------------------------+-------------------------------------------------------------------+
| genie_python (include python and dependencies)        | ``C:\Instrument\Apps\Python3``                                    |
+-------------------------------------------------------+-------------------------------------------------------------------+
| EPICS utilities                                       | ``C:\Instrument\Apps\Python3\EPICS_UTILS``                        |
+-------------------------------------------------------+-------------------------------------------------------------------+
| Server Code and executables                           | ``c:\Instrument\Apps\EPICS``                                      |
+-------------------------------------------------------+-------------------------------------------------------------------+
| Server Settings                                       | ``C:\Instrument\Settings\config\<Instument name>\configurations`` |
+-------------------------------------------------------+-------------------------------------------------------------------+
| Common settings files (e.g. sensor calibration files) | ``C:\Instrument\Settings\config\common``                          |
+-------------------------------------------------------+-------------------------------------------------------------------+
| Server logs, autosave and database files              |  ``C:\Instrument\Var``                                            |
+-------------------------------------------------------+-------------------------------------------------------------------+

.. _installing_ibex_server:

Installing IBEX Server
----------------------

Most instruments at ISIS are now using at IBEX, with the last few being planned for migration during 2024 and early 2025.
If you need to install the server on an Instrument, please contact the Experiment Controls team.
`The developers manual <https://isiscomputinggroup.github.io/ibex_developers_manual/>`_ holds more detailed information should it be needed.

Uninstalling IBEX
-----------------

Uninstallation of IBEX is performed by manually deleting the relevant directories as listed in :ref:`installation_layout`.