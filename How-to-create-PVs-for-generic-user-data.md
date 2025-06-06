The `INSTETC` [IOC](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Start-and-Stop-IOCs) contains [PVs](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Process-Variables) intended to be user-settable values. These PVs can have blocks pointed at them [via the configurations screen](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Create-and-Manage-Configurations#blocks-tab). These PVs could, for example, be used to hold data about equipment which is manually controlled, but should be put in a nexus file.

There are three types of data that a user PV can hold: integer, real and string. The corresponding process variables are:
- `IN:<instrument>:PARS:USER:I0` for integers
- `IN:<instrument>:PARS:USER:R0` for real types
- `IN:<instrument>:PARS:USER:S0` for strings

The counter at the end of the PV is an index. By default, instruments are set up to have 5 of each type of user PV (indexes 0-4 inclusive). If you find you need more than 5 of any one data type, it is configurable.
- Go to `C:\Instrument\Settings\config\NDX<instrument>\configurations`
- Locate a file called `globals.txt` (if it does not exist, create it)
- Add the following line to the file: `INSTETC_01__NUM_USER_VARS=25`, where `25` should be replaced by the maximum number of user variables you want for any given type.
- Ensure that `globals.txt` ends with at least one blank line, otherwise, the last line will not be read.
- To pick up the changes, IBEX will need to be restarted. Follow the process detailed here: [Starting the IBEX Server](https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Starting-And-Stopping-IBEX#starting-ibex-server).