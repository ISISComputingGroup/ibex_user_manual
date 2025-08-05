Menu Bar
########

The menu bar on the IBEX GUI provides access to the application features described below.

.. contents:: **Contents**

IBEX Menu
---------
Switch Instrument
   Select the Switch Instrument menu item to re-direct the IBEX GUI to view a different instrument.

   **Please Note:** If you connect to an instrument from outside the instrument's sub-network (i.e. if you are not in the instrument blockhouse or cabin/pod), you will only be able to view the instrument (i.e. you will not be able to make changes to any of the fields).

Manager Mode
   Selecting the Manager Mode option allows the user to enter manager mode after entering the manager password.

Exit IBEX Client
   Select the Exit IBEX Client menu item to quit.  Please note, quitting the IBEX Client does not terminate the IBEX server, which will continue to run on the instrument control PC.

Configuration Menu
------------------
Edit Current Configuration
   Select the Edit Current Configuration menu item to make changes to the currently loaded instrument configuration.
Configurations
   Select the Configuration menu item to perform one of the following actions:

   * New - create a new configuration
   * Load - replace the current configuration with a different configuration loaded from a file
   * Edit - edit an existing configuration (independently of the current configuration)
   * Delete - delete a configuration
   * Recent - load one of the last 5 loaded configurations

Components
   Select the Components menu item to perform one of the following actions:

   * New - create a new component
   * Import - import a component from another instrument
   * Edit - edit an existing component
   * Delete - delete a component


Synoptic Menu
-------------
New 
   Create a new synoptic.
Edit
   Select an existing synoptic and edit it.
Delete
   Select an existing synoptic to delete it. 

IOC Menu
--------
Start/stop IOCs
   Selecting the Start/stop IOCs menu item displays a dialog allowing you to start an IOC or to stop an IOC that is currently running.

Block Actions Menu
------------------
View run-control settings
   Selecting the View Run-Control Settings menu item displays a dialog showing you which blocks (if any) are currently under run-control.  You can also assign new run-control settings to blocks and modify or remove existing run-control settings.

You can change run-control settings in 3 different ways (2 temporary and 1 permanent changes)

* Temporary change
    1. You can set temporary run-controls settings via Run-Control menu.
       Input low and high limit from the bottom of the window.

    2.  You can also set temporary run-controls settings via scripting.
        Type ``g.cget(b.YOUR_BLOCK_NAME, runstate=true, highlimit= x, lowlimit=y``, where x and y are numbers you want to set as limits.

    **Note:** Defaults can be restored using the ``Restore Configuration Values`` for the selected block or ``Restore All Configuration Values``    
    buttons.
            
    Temporary setting will override the default set for the block in the configuration and will persist until the configuration is reloaded.


* Permanent change
    You can set default run-controls settings that will remain, unless you change it temporarily.

    1. From ``Run-Control`` menu, select the block you would like to change and click ``Edit Host Configuration`` to change the settings.

The :doc:`Blocks-and-Groups` page describes how blocks under run-control are shown in the GUI.

Alert on blocks settings
   1. Selecting the "Alert on blocks settings" menu item displays a dialog showing us blocks in current configuration and the facilitates configuring the alert parameters for individual blocks. 
   2. The dialog also shows the emails and mobiles configured for receiving the alerts. We can change change these values.
   3. We can also send a test message of our choice. This message is changed by the server, once a new alert condition happens.

Preferences Menu
----------------

Colour settings
    Allows the user to one of the supported colour schemes:

    * Standard colour scheme
    * Alternative colour scheme 1    

Help Menu
---------
About
   Selecting the "About" menu item displays a dialog showing the current version of the IBEX client and the current version of the IBEX server (running on the instrument control PC to which you are currently connected).  If you need to report a problem with IBEX, support staff may ask you to look up this information, so that they know which version of the IBEX software you are using.
User manual
   Selecting the "User manual" menu item opens the IBEX user manual in a web browser.
Console Log
   The console log is used by support staff to help them diagnose any problems that IBEX might encounter.
Icon Licences
   View the licences for the icons used in IBEX
Get help
   Displays support telephone numbers and how to get help or report problems.
