Banner
######

The Banner is located at the bottom of the IBEX GUI window.

The Banner displays information about the current status of the IBEX GUI. For instance, it displays the name of the current configuration.

.. raw:: html

   <details>
   <summary>Details - Server Processes Restart</summary>

   <p>It also displays the current status of the IBEX server. It will show `UP` if all expected processes are running, `PARTIAL` if atleast one process is running normally, and `DOWN` if no server processes are running. Use the details page to check the status of each server process and contact the experiment controls team if there is unexpected trouble with your server. You may wish to restart specific server processes yourself- before doing so you should consider if doing so will have any effect on the work you're currently undertaking through IBEX- contact the team if you are not sure. To do this you must first be in manager mode and the overall server status must be in `PARTIAL`, clicking restart on the process will prompt you to read a warning that is written specifically for that server process, and will warn you about the specific effects of restarting it. After reading this you may choose `OK` which will restart the process.</p>
   </details>

The Banner also displays important status information about selected devices on an instrument. It is customisable on an instrument by instrument basis. For example, on LARMOR, the Banner is customised to display a message indicating whether any motors are moving and to display a message if the bump strip has been tripped. On IMAT, the Banner is customised to display the current position of the beam attenuator device.

Please discuss how you would like the Banner to be customised for your instrument with the Experiment Controls team.
