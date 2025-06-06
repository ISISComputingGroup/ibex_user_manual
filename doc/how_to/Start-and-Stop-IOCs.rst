Start and Stop IOCs
###################

In `EPICS <http://www.aps.anl.gov/epics/>`_ an IOC is a component which controls hardware devices.  In IBEX, we use IOCs to control sample environment devices attached to instruments. The acronym IOC stands for Input/Output Controller.  As the name suggests, an IOC controls the communication between a hardware device and other parts of IBEX.

In order to communicate with a hardware device, the corresponding IOC must be running.  The ``IOC`` menu in IBEX provides the means to start IOCs (and to stop IOCs, when they are no longer required).

Starting or Stopping an IOC
---------------------------
To start, stop or restart an IOC:

#. Select ``Start/Stop IOCs`` from the ``IOC`` menu.
#. IBEX displays a dialog containing a list of all the IOCs available on the instrument.  The list shows whether each IOC is running or stopped.
#. Find the IOC you want in the list and use the buttons at the bottom to start, stop or restart that IOC.

It might take a few moments from pressing the button for the selected IOC to fully start itself up or fully shut itself down.  You might also see a number of messages written to the IOC Log (see [[Views]]) as the IOC starts up or shuts down.

**Note**: The effect of auto-restart has no effect on the stop action. Stop will stop the IOC and it will not restart.