Create and Manage Configurations
################################

A configuration is the means by which an instrument is described and defined to IBEX.  A configuration defines the blocks, IOCs, components, macros and other items which IBEX needs to use to control the instrument.  You can create multiple configurations for an instrument, to describe and define how the instrument has been set up for different experiments. In some cases, there are macro settings which are global for the instrument. These are set outside of the GUI and override the values in the configuration. These are setting which should not change, e.g. the IP address of the Galil motors (see the section below on how to alter these).

**Please note:** An IBEX configuration is **not** the same as a Mantid configuration.  IBEX and Mantid view instruments in fundamentally different ways, which means that their respective configurations are not interchangeable.

.. contents:: **Contents**

Creating a Configuration
------------------------

To create a configuration:

#. Select ``Configurations > New`` from the ``Configuration`` menu.
#. IBEX displays the Edit Configuration dialog, which contains the following eight sections:  

   #. Summary
   #. Components
   #. IOCs
   #. Blocks
   #. Groups
   #. IOC Macros
   #. IOC PV Values
   #. IOC PV Sets

#. At the bottom of the dialog are two buttons

Save as...
   Click on the ``Save as...`` button to save your changes.  The Save as... dialog prompts you to provide a name and description for your configuration.

   * You must provide a name for the configuration.
   * The name of the configuration can contain only the characters a-z, A-Z, 0-9 and _ (underscore).
   * The name must also start with a character.
   * The name of the configuration must be unique (on your instrument).

   The Save as... dialog also includes an option to save a configuration as a component.  The :doc:`Create-and-Manage-Components` page describes more details about this option.

Cancel
   Click on the ``Cancel`` button to exit the Edit Configuration dialog without saving your changes.

We'll describe each of the Edit Configuration dialog tabs in turn.

Summary
~~~~~~~

The Summary allows you to create a short description for your configuration.  It also allows you to associate a default synoptic view with your configuration.

The summary is displayed at the top of the dialog and contains the following fields:

Name
   This is a read-only field.  It is defined when you save the configuration.  When you are creating a new configuration, the ``Name:`` field will be empty.

Description
   Provide a short description of your configuration.  Configuration names can sometimes be a little cryptic; a brief description will help you to remember the purpose of the configuration better.

Synoptic
   IBEX allows you to create different synoptic views for use with different configurations.  Therefore, it is convenient to associate a synoptic view with a configuration - it saves you from having to remember the association.  Your chosen synoptic will be used as the default synoptic whenever you use this configuration.  

Protected
    Selecting this checkbox will restrict editing of this configuration to users in "manager mode". Manager mode can be enabled under the IBEX menu, by inputting the password (please ask experiment controls group if you are unsure about the password)

Dynamic
    Mark this configuration or component as dynamic, meaning that it can be edited automatically in response to certain events. Note that this is advanced functionality which requires other IBEX components to be configured; please ask experiment controls group if you believe you need this functionality on your instrument.

.. _manage_configs_components:

Components Tab
~~~~~~~~~~~~~~

Components are, in essence, mini configurations.  You can use components to "pre-configure" a device (or group of devices) and then include the components in a configuration. The process of creating and managing components is described in :doc:`Create-and-Manage-Components`.

The Components tab displays two lists of components.  The left-hand list shows which components are available to be included in your configuration.  The right-hand list shows which components are already included in your configuration.   You can only include a component once in a configuration.

Use the arrow buttons to move components between the two lists.  

.. _manage_configs_iocs:

IOCs Tab
~~~~~~~~

The :doc:`/Key-Concepts-in-IBEX` page describes what an IOC is. In general, you will only wish to include a subset of these in your configuration (i.e. those that correspond to devices on your instrument).

IOCs need to be explicitly added to the configuration via the IOC tab if you want to change any of their settings such as macros. The IOCs tab shows an overview of all IOCs that are part of the currently viewed configuration. Below the overview table, there are three buttons to add, edit or delete an IOC.

- The "Edit IOC"-button opens a dialog containing all the settings related to the selected IOC: 

  - Auto start: If set, the IOC will be started/restarted whenever the configuration is changed. If not set then if the IOC is not running it will remained stopped after config change, if it is running it will remain running throughout the config change. (Warning: if not set and the IOC is running any changes you make, e.g. a macro change, will not be set on the IOC until you restart it manually.)
  - Auto restart: If set, the IOC will be automatically restarted if it is terminated unexpectedly. If the IOC is stopped from the client or writing to the appropriate PV then it will not be restarted. 
  - The simulation level: By default, the simulation level file is set to NONE, meaning that the IOC will not run in simulation mode.  Under normal circumstances, you should not change the default setting. Simulation mode is used for running the IOC without the actual physical device.
  - `IOC Macros`_, `IOC PV Values`_ and `IOC PV Sets`_.

- The "Add IOC"-button opens a dialog which lets you choose from a list of all IOCs available on the instrument. Confirming your selection will take you to the "Edit IOC" dialog for the selected IOC.
- The "Delete IOC"-button allows you to delete IOCs from the list and the configuration. This works with multiple selections, too.

.. _manage_configs_blocks:

Blocks Tab
~~~~~~~~~~
The Blocks tab lists all the blocks that have been defined for the current configuration.  When creating a new configuration, the list of blocks will be empty.  A :doc:`block </concepts/Blocks>` is, essentially, an alias to a :doc:`PV</concepts/Process-Variables>`.


To create a new block, click on the ``Add Block`` button or use the keyboard shortcut ``Ctrl+A``. Blocks can also be copied using the ``Duplicate Block`` button or the keyboard shortcut ``Ctrl+D``. Upon creation of a new block, IBEX displays a dialog to allow you to define the new block.  By default, the new block is given the name ``NEW_BLOCK``.  You can give the block any name you like, provided the name:

* contains only the characters a-z, A-Z, 0-9 and _ (underscore).
* starts with a character.
* is unique (on your instrument).

Below the block name field is the PV address field.  Click on the ``Select PV`` button next to the PV address field to choose a PV to be aliased by the block name.

On clicking the ``Select PV`` button, IBEX will display a list of PVs available on your instrument.  There can be a huge number of PVs on an instrument, so the dialog provides some filters to help you narrow your search.  Choose PVs from:

   ``All IOCs`` to see PVs from all IOCs on your instrument (this can result in a very long list of PVs).

   ``Active IOCs`` to see PVs only from IOcs that are currently running on your instrument.

   ``Config IOCs`` to see PVs only from IOCs included in the current configuration.

Interest Level
   ``High`` to see PVs considered to be of high interest to scientists

   ``Medium`` to see PVs considered to be of medium interest to scientists (many PVs in this category will be of more interest to technicians and support staff, rather than scientists)

   ``Facility`` to see PVs that relate to a facility, rather than an instrument, devices (PVs in this category typically include PVs relating to the accelerator, target stations, shared beamlines and instrument shutters).

   ``All`` to see all PVs from your selected category of IOCs (again, this can generate a very long list of PVs).

You can also narrow down the list of PVs by typing the start of the PV name in the ``PV address`` field.  For example, if you type ``IN:IRIS:EURO`` you will see only PVs whose address starts with those characters.  This is useful if you already know which PV you are looking for.

Scroll down the list of PVs until you find the one you want.  Click on it, to select it and then click on the OK button to return to the Add Block dialog.

On the Add Block dialog, you can also choose to 

Visible/Local
   Toggle the ``Visible`` check-box to make the block visible or hidden.  By default, blocks are always visible.  This feature is useful, for example, if you need to see blocks while setting up an experiment but don't need to see them once the experiment is running.

   The ``Local`` check-box is used when you need to view PVs from another instrument as blocks.  In most circumstances, you will not need to view PVs belonging to another instrument, so you should leave the ``Local`` check-box checked.  Facility PVs are an exception to this rule, but IBEX knows about facility PVs and, in this case, automatically sets the ``Local`` check-box to unchecked.  If you do need to view PVs belonging another instrument, please consult with the Experiment Controls team.

Run-Control Settings
   Toggle the ``Enabled`` check-box to enable run-control on this block.  Use the Low Limit and High Limit fields to define the run-control range (i.e. data is only collected when the block lies within the range).

   Run-control can also be set on non-numbers as boolean or enum values in IBEX are mapped to underlying numbers. For example, a shutter status of OPEN corresponds to a 1 and CLOSED to 0, so setting run control of between 0.5 and 1.5 will put the instrument into waiting when the shutter is not open. In most cases, a 1 will correspond to true and 0 to false, if you are unsure, please consult with the Experiment Controls team.

   When you create a run control for a block it will be used as the default for that configuration. You can temporarily override these values using the `Run-Control menu <https://github.com/ISISComputingGroup/ibex_user_manual/wiki/Menu-Bar#run-control-menu>`_.

   Run controls set on blocks are unique to the configuration. If you would like identical run controls on a block for all configurations, you must set the run control for that block in each individual configuration. 

Logging Settings
   Use the Logging Settings section of the Configure Block dialog to control how the value of the block is logged.

   * **Note:** By default logging is enabled (i.e. changes in the value of the block will be logged).  
   * Click on the ``Enabled`` check-box to change the way the block is logged.  If the ``Enabled`` check-box is checked, then logging is enabled.
   * You can choose to log the block value periodically (the default period is every 30 seconds).
   * Alternatively, you can set a "deadband" - the block will only be logged if its value falls outside +/- the limit defined by the deadband value.

**PREVIOUS VERSIONS OF IBEX:** In releases 2.1.0 or earlier, the logging is disabled by default.

To edit an existing block, click on the ``Edit Block`` button or use the keyboard shortcut ``Ctrl+E``. Blocks can be deleted by clicking the ``Delete Block`` button or by using the keyboard shortcut ``DEL``.

**Note:** Blocks that have been inherited from a component will be shown, but cannot be modified, in the Edit Configuration dialog (the blocks will be shown as "greyed-out").  To modify inherited blocks you need to use the Edit Component dialog (see :doc:`Create-and-Manage-Components`).

.. _manage_configs_groups:

Groups Tab
~~~~~~~~~~
Use the Groups tab to arrange your blocks into convenient groups.  You can define as many groups as you wish and you can place as many blocks in each group as you wish, although a block can only appear in one group.

By default, all blocks are assigned to an automatic group called "Other".  By creating new groups, you have the opportunity to override the default assignment and assign blocks to groups of your choosing.  

To create a new group, select the Groups tab and click on the ``Add`` button.  IBEX displays a dialog to allow you to define a new group.  By default, each new group has the name ``NEW_GROUP``.  You can give the group any name you like, provided the name:

* contains only the characters a-z, A-Z, 0-9 and _ (underscore).
* starts with a character.
* is unique (on your instrument).

When you click on the ``Add`` button, the dialog displays which blocks are available to be assigned to the new group (i.e. blocks in the "Other" group).

Use the buttons with the Up and Down arrows to control the ordering of the groups and the order of the blocks within the groups.

You can select multiple blocks to be added (or removed) from a group using the ``Shift`` and/or ``Ctrl`` keys on your keyboard.

**Note:** Groups that have been inherited from component will be shown, but cannot be cannot be modified, in the Edit Configuration dialog (the blocks in an inherited group as shown as "greyed-out").  To modify inherited groups you need to use the Edit Component dialog (see :doc:`Create-and-Manage-Components`).

.. _manage_configs_add_ioc:

Edit/Add IOC Dialog
-------------------

The Edit/Add IOC dialogue is opened from the IOC on the New/Edit Configurations/Components dialog. 

.. _manage_configs_ioc_macros:

IOC Macros
~~~~~~~~~~

IOC Macros are configurable values that IBEX can supply to the IOC when the IOC is started.  For example, if the IOC is controlling a serial device attached to a COM port, you can use a macro to identify the appropriate port to the IOC.  This is especially useful if the device moves between instruments and may be attached to different COM ports on different instruments.  Another example of an IOC macro might be the name of a calibration file.

To set an IOC macro:

#. Select the IOC Macros tab for the IOC they will be displayed in the table.  The columns in the table are:

   #. Macro Name: the name of the macro (e.g. ``PORT``, ``BAUD`` or ``IPADDRESS``)
   #. Value: the current value of the macro (e.g. ``COM3``, ``9600`` or ``192.83.42.106``)
   #. *v3.7+* Use Default?: whether to not set a value and use the default, if one exists
   #. *v3.7+* Default: the default value if one exists, otherwise (no default) or (default unknown)
   #. Description: a short description of the macro's purpose
   #. Pattern: macro values need to be defined correctly.  IBEX uses the pattern to validate the macro value. (For those familiar with such things, the pattern is a "regular expression").

#. Choose a macro from the table.  The ``Name:`` field (read-only) is populated with the macro name and the ``Value:`` field is populated with the current value of the macro.

#. Edit the ``Value:`` field to change the macro value.  Please note that the value you enter will be validated against the pattern.  If the macro does not conform to the pattern, IBEX will display a warning message.  IBEX will refuse to accept any values that do not conform to the pattern.

#. The table of macros will be updated with the new value.  You can also use the ``Clear Macro`` button to clear the contents of the ``Value:`` field.

As of version 5.7, values can be edited directly in the table. Pressing enter or clicking somewhere else will set the value. To clear the value so that it is no longer set, set "Use Default?" to yes. To set the macro to a blank value, i.e an empty string or "", set "Use Default?" to no and leave the value box empty.

If you are not sure about how to correctly configure macro values for a device, please consult with the Experiment Controls team.

.. _manage_configs_pv_values:

IOC PV Values
~~~~~~~~~~~~~

IOC PV Values allows you to set the values of a PV when the configuration is first loaded. For example, you may have a CCR in one configuration but a Furnace in another, both using the same Eurotherm. However, the Eurotherm may require the Furnace.txt sensor file for the furnace and the CCR.txt file for the CCR. In this case the we would add a PV Value of 

*IN:INST:EUROTHRM_01:A01:CAL:SEL* *Furnace.txt*

to the furnace config and 

*IN:INST:EUROTHRM_01:A01:CAL:SEL* *CCR.txt*

to the CCR config. If you are unsure what PVs you need to write to see :ref:`faq_find_pv`

**Note**: The value of a PV will remain until it is set to something else. So if a configuration sets it loading another configuration will not set it back to what it was before.

.. _manage_configs_pv_sets:

IOC PV Sets
~~~~~~~~~~~

IOC PV Sets is an experimental feature within IBEX **do not** use this before talking to the IBEX team. It can be used to load in autosaved values from a specific file setup beforehand.

**Note**: The value of any PVs will remain until it is set to something else. So if a configuration does this auto-load then loading another configuration will not set it back to what it was before.

.. _manage_configs_edit_config:

Editing a Configuration
-----------------------

To edit a configuration:

#. Select ``Configurations > Edit`` from the ``Configuration`` menu.
#. IBEX displays the Edit Configuration dialog (as described in `Creating a Configuration`_).
#. This time the Edit Configuration dialog has three buttons at the bottom of the dialog

Save
   Clicking immediately on the ``Save`` button saves your changes without any further prompting.  

Save as...
   Clicking on the ``Save as...`` button operates as described in the previous section.  You can use the ``Save as...`` button to save the configuration with a new name, before making further changes.

Cancel
   Click on the ``Cancel`` button to exit the Edit Configuration dialog without saving your changes. 

.. _manage_configs_edit_current_config:

Edit Current Configuration ...
------------------------------

To edit the current configuration select ``Edit Current Configuration ...`` from the ``Configuration`` menu.  This avoids the need to select the current configuration from a list of configurations.  Otherwise, this option behaves in the same way as `Editing a Configuration`_.

It is always a good idea to check the name of the current configuration before you start editing it - to be sure that you are about to edit the configuration you intended to edit. The :doc:`/gui/Banner` displays the name of the current configuration

**Note:** When you click on the ``Save`` button when editing the current configuration, the changes you make are applied immediately.  There will be a short pause while IBEX re-loads the current configuration and refreshes the display.

.. _manage_configs_load_config:

Load a Configuration
--------------------

To load a configuration:

#. Select ``Configurations > Load`` from the ``Configuration`` menu.
#. IBEX displays the Load Configuration dialog, which lists all the configurations defined for your instrument.
#. Select a configuration from the list and press the ``OK`` button
#. IBEX discards the currently loaded configuration and loads the selected configuration.  The discarded configuration is not lost - it still exists as a saved configuration and can be reloaded later, if you wish.

.. _manage_configs_recent_config:

Recent Configurations
--------------------

To load a recent configuration:

#. Select ``Configurations > Recent`` from the ``Configuration`` menu.
#. IBEX displays the Load Recent Configuration dialog, which lists the last five loaded configurations defined for your instrument and the time at which they were last loaded.
#. Select a configuration from the list and press the ``OK`` button
#. IBEX discards the currently loaded configuration and loads the selected configuration.  The discarded configuration is not lost - it still exists as a saved configuration and can be reloaded later, if you wish.

**Note**: As the current configuration is already loaded, it is not displayed in the list. However, it will be displayed after loading another configuration.

.. _manage_configs_delete_config:

Delete a Configuration
----------------------

To delete a configuration:

#. Select ``Configurations > Delete`` from the ``Configuration`` menu.
#. IBEX displays the Delete Configuration dialog, which lists all the configurations defined for your instrument.
#. Select a configuration from the list and press the ``OK`` button
#. IBEX deletes the selected configuration.

**Note 1:** If you try to delete the currently loaded configuration, IBEX will do nothing.  It will not delete the current configuration, because that would leave IBEX unable to communicate with the instrument.  If you want to delete the current configuration you need to load a different configuration, then delete the previously loaded configuration.

**Note 2:** When you delete a configuration it really is deleted.  It is no longer available to be used by IBEX. Before deleting a configuration, please be sure that you really do want to delete it.  If you unintentionally delete a configuration, please contact the Experiment Controls team - it may be possible to recover the deleted configuration.

.. _manage_configs_globals:

Editing a global setting
------------------------

Global settings are stored in the configuration directory in a file called ``globals.txt`` (the configuration directory is ``<Setting directory>\\config\\<instrument name>\\configurations``). Lines in the file starting with a '#' are comments. Settings are expressed by a line 

``<IOC name>__<Macro Name>=<value>``

where ``IOC name`` is the name of the IOC on which the macro is set, ``Macro name`` is the name of the macro and value is the value it should have. (**N.B.** that is a double underscore between ``IOC name`` and ``Macro name``).