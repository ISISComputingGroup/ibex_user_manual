Manage the DAE
##############

The Data Acquisition Electronics (DAE) is the hardware which collects neutron or muon data. The DAE is controlled by the ICP (see :doc:`/Key-Concepts-in-IBEX`), which informs the DAE when to start and stop collecting data from the instrument detectors. The ICP also receives sample environment information and combines it with the detector data and is responsible for transferring the final combined dataset to a data file.

The DAE view communicates with the ICP to control the DAE. The DAE can be managed from the DAE view of the client. The DAE view is split into some tabs and sub tabs which are listed with their functions below.

.. contents:: **Contents**

Run Summary
-----------

The Run Summary tab displays some summary information about the current run and displays any log messages received from the ICP. 

Run Summary Fields
~~~~~~~~~~~~~~~~~~

* ``Instrument``: the instrument on which the current run is being performed
* ``Run Status``: status of the current run
* ``Run Number``: the current run number
* ``ISIS Cycle``: the current ISIS cycle
* ``Title``: you can provide a short description of the current run in the ``Title`` field.  Click on the ``Set`` button to commit the change (i.e. send it to the ICP, so that it gets included in the data file). To embed block values within the run title see :doc:`/how_to/Add-blocks-to-run-title`.
* ``Show Title in Dataweb Dashboard Page``: set whether to display the title in the :doc:`/The-Web-Dashboard`. This checkbox only affects the Dataweb dashboard; it does not affect the display of the title in IBEX, or the inclusion of the title in the data file.

Message Log
~~~~~~~~~~~
The message log area lets you view any messages issued by the ICP.  The message log area is the same as the main Log Messages view but filtered to show only messages from the ICP.

Run Control Buttons
~~~~~~~~~~~~~~~~~~~

The Run Summary tab also provides some buttons to control the acquisition of data. Which buttons are available is dependent on the current status of the DAE; this is displayed in the ``Run Status`` field and the IBEX :doc:`/gui/Dashboard`.

Begin Run
   Beginning a run instructs the ICP to tell the DAE to start collecting data. The run status of the DAE will change to BEGINNING and then RUNNING.

End Run
   Ending a run instructs the ICP to tell the DAE to stop collecting data and save the data. The run status of the DAE will change to ENDING (while it saves the data) and then SETUP when it is ready to be started again.

Pause Run
   Pausing a run instructs the ICP to tell the DAE to pause data collection indefinitely. The run status of the DAE will change to PAUSED.  The status will remain PAUSED until it is instructed to resume, end or abort the run.

Resume Run
   Resuming a run instructs the ICP to tell the DAE to resume data collection after it has been paused. The run status of the DAE will return to RUNNING.

Abort Run
   Aborting a run instructs the ICP to tell the DAE to stop data collection (as for END).  However, the data that has been collected is not written to a file; if a new run is started, then any data that has been collected will be lost. The run status of the DAE will change to SETUP. If this is done mistakenly, the cancel abort button can be used to undo the abort.

Cancel Abort
   This will instruct the DAE to cancel a previous abort. The DAE will be left in a paused state.

Save Run
   This will save the current run data without stopping the current run.

Experiment Setup
----------------

The Experiment Setup comprises of sub-tabs which will have been configured by an ISIS Instrument Scientist.  Please do not modify their contents without consulting with the instrument scientist.

Any changes made are only sent to the DAE when the ``Apply Changes`` button is pressed and will be highlighted until the ``Apply Changes`` button is pressed. If there is a problem with the setting, an error message will appear on the `Run Summary`_ panel.

Time Channels
~~~~~~~~~~~~~

The time channels sub-tab allows the setting of the spectra captured in different time regimes. By setting different step sizes and modes, you can optimise the sizes of the time bins in the final spectra. The setting for the time channels can be set either using the table or by setting a file; usually used when more than 6 regimes are required. The files are stored in the ``configurations/tcb`` directory in the :ref:`installation_layout` on the instrument.

.. _dae_data_acquisition:

Data Acquisition
~~~~~~~~~~~~~~~~

The data acquisition sub-tab allows you to set up how the DAE will collect the data. The page is split into several sections:

Tables
    The wiring table, detector table and spectra table set the files used when turning signals generated in the detectors into spectra. These files are stored in the ``configurations/tables`` directory in :ref:`server settings <installation_layout>` on the instrument.

Monitor
    Set which spectra number is used for the monitor counts and between which times the spectra should be integrated to return the monitor counts.

Vetoes
    Set which :ref:`vetoes <concept_veto>` are active.

Muons
    Set if and how to collect muon data.

Timing
    Set the source of the :ref:`timing signal <concept_timing>` and how often the data should be auto saved.

Periods
~~~~~~~

The period sub-tab allows the period types and needed parameters to be set up within the DAE. Periods allow data to be collected as if restarting the DAE but without the time overhead of doing this. Software periods are controlled via software command, e.g. genie_python's ``change_period`` command. The other options are hardware controlled, and these are internal (within the DAE) or external control. 

Run Information
---------------

The Run Information tab provides a more complete summary of the DAE set up than the Run Summary tab.  All the fields on this tab are read-only.

Spectra Plots
-------------

The Spectra Plots Tab displays up to 4 spectra plots.  The plots show the recorded spectra from the detectors which were set up using the tables in the data acquisition tab.  You can choose which spectra are plotted by using the ``Spectrum`` and ``Period`` fields for each plot.  Click on the ``Set Plot`` button (positioned at the top right of each plot) to update the plot after changing the ``Spectrum`` or ``Period`` fields.

Combined Spectra Plot
---------------------

The Combined Spectra Plot Tab displays up to 4 spectra plots on the *same graph*. This allows for more direct comparison with one another. The plots show the recorded spectra from the detectors which were set up using the tables in the data acquisition tab. You can choose which spectra are plotted by using the ``Spectrum`` and ``Period`` fields for each plot and make each plot visible or hidden with its corresponding ``Checkbox`` field.


Detector Diagnostics
--------------------

This tab shows detector diagnostics, the count rate, max and integral for a range of detectors set above. It is possible to show all spectrum with zero or non-zero counts or all the spectra. This can be useful for identifying broken detector tubes. 

The page only updates when it is open on an instrument, so if you are viewing it remotely you may have no information. This is to reduce the load on the server and DAE.

Vetoes
------

The Vetoes tab shows a summary of the vetoes that are in force and their effect for the current run.  This information is read-only.  Vetoes can only be changed before the start of a run, via the `Data Acquisition`_ sub-tab on the `Experiment Setup`_ tab.

Simulated DAE
-------------

The DAE can be placed into a **simulation**/**simulate** mode if you want to do an off-line experiment or test something out when the physical DAE is not usable. In simulation mode the DAE will count frames as normal and has a spectrum count in some spectra but it is not realistic. To turn this on use in genie_python:

.. code-block:: python

    g.set_dae_simulation_mode(True)

to switch it off:

.. code-block:: python

    g.set_dae_simulation_mode(False)

In simulation mode the dashboard should be coloured correctly and `SIMULATION MODE` is shown in large black letters.
NB All instruments can be placed in simulation mode but some are not set up correctly. If you are having problems please contact us.

It is also possible to run the DAE and do real counts without the timing signal from ISIS. The setting for this are on :ref:`Experimental Setup -> Data Acquisition tab under Timing <dae_data_acquisition>`