PV Naming Conventions
#####################

Facilities running `EPICS <http://www.aps.anl.gov/epics/>`_ usually adopt a convention for naming PVs (:doc:`Process-Variables`).  ISIS is no exception.

The purpose of the naming convention is to:

a. Provide a systematic means of describing the PV,
b. Ensure that the name of the PV is unique (within the facility).

ISIS Naming Convention
----------------------

At ISIS, PV names are chosen to describe a function, not hardware/technology - the PV name is the purpose of a channel and is abstracted from the underlying hardware; the name of the IOC (to which the PV belongs) can, however, reflect technology/hardware/implementation. 

The essential format of the ISIS naming convention is ``DOMAIN:SUBDOMAIN:TECHNICALAREA:DEVICE:SUBDEVICE:SIGNAL``

PV names should contain only the following characters ``A-Z``, ``0-9``, ``_``, ``:``, ``*``. Notice that lowercase characters are not allowed.  The colon character ``:`` is used to separate different elements of the PV name; therefore, do not use the ``:`` for other purposes (e.g. as part of an IOC name).  To break up individual components of a PV name into readable segments, use the underscore, ``_`` character.

In addition, PV names must start with a letter and must not end with ``_``.

Domain & Subdomain Names
~~~~~~~~~~~~~~~~~~~~~~~~

Names appearing in the domain & subdomain levels include:

+------+--------------------------------------------------------------------------------------------------------+ 
| Name | Description                                                                                            | 
+======+========================================================================================================+ 
| AC   | ISIS Accelerator/synchrotron related parameter                                                         |
+------+--------------------------------------------------------------------------------------------------------+ 
| TG   | ISIS Target related parameter                                                                          |
+------+--------------------------------------------------------------------------------------------------------+ 
| IN   | Instrument related parameter                                                                           |
+------+--------------------------------------------------------------------------------------------------------+ 
| BL   | Beamline – used if multiple instruments are sharing a common set of equipment; e.g, the muon beamlines |
+------+--------------------------------------------------------------------------------------------------------+ 
| TE   | Testing domain, used by local EPICS developers                                                         |
+------+--------------------------------------------------------------------------------------------------------+ 

In the instrument domain, the sub-domain is the full instrument name.  For example: ``IN:GEM`` or ``IN:POLREF``.

Technical Area and Device Names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Technical Area and Device Names reflect the nature of the device that owns the PV in question.  For example:

* ``IN:GEM:MOT`` relates to PVs associated with motion control equipment on GEM.
* ``IN:ZOOM:VAC`` relates to PVs associated with vacuum equipment on ZOOM
* ``IN:IRIS:DAE`` relates to PVs associated with the DAE on IRIS
* ``IN:IMAT:MOT:MTRccmm`` relates to EPICS motor records on IMAT for a motor on controller number cc, motor number mm. These numbers are zero padded to two digits and start from 1 (e.g. MTR0101 is the first motor on the first controller).
* ``IN:LARMOR:MOT:JAWSmm`` mm-th set of jaws on LARMOR (e.g. JAWS01 is the first set of jaws, etc.).

Signal Names
~~~~~~~~~~~~

Standard signal names include:

+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| Signal Name | Meaning                 | Valid Units                                                                                  |
+=============+=========================+==============================================================================================+ 
| POS         | Position                |  M, mm, cm                                                                                   |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| STAT        | Status, State           | Open, Closed, On, Off, Ok, Error                                                             |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| CURR        | Current                 | A, mA, uA                                                                                    |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| VOLT        | Voltage                 | kV, V                                                                                        |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| CMD         | Device command          | e.g. write to this to perform an action, such as start/stop a run                            |  
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| SEL         | Select mode or position |                                                                                              |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| TEMP        | Temperature             |  K                                                                                           |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| COUNT       | Counter value           | neutron counts                                                                               | 
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| COUNTD      | Counter value           | as a distribution, i.e. divided by bin width - so neutron counts per microsecond for example |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| P, I, D     |  P, I, D values         |  e.g. on a Eurotherm                                                                         |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| TOF         | Time of flight          |                                                                                              |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| TIME        | An absolute timestamp   | preferably in ISO8601 format                                                                 |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 
| FIELD       | Magnetic field          |                                                                                              |
+-------------+-------------------------+----------------------------------------------------------------------------------------------+ 

If a value can fluctuate, these refer to the current measured value of a quantity and the signal qualifiers SP and RBV are used to indicate the desired value software requested (setpoint) and the desired value being used in the hardware (RBV)

For example, for a TEMP signal

* ``...:HEATER:TEMP`` Current temperature
* ``...:HEATER:TEMP:SP`` Temperature set point (requested value) – this is the value that was input in software and sent to the equipment. Writing to this PV will cause the setpoint to change
* ``...:HEATER:TEMP:SP:RBV``  This is the setpoint “readback”  from hardware, which may differ from SP sent above if, for example, the hardware was unable to exactly match the requested value.  By definition, a readback PV is read-only.  Also if the SP was changed by some other mechanism (e.g. manually on the hardware) ``:SP`` would not reflect this, but ``:SP:RBV`` would.

**Note:** The RBV suffix can be used more generally e.g. For P,I,D values you could have ``...:P`` and ``...:P:RBV``
