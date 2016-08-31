.. _NavigateSynoptics:

Navigating Synoptic Views
=========================

In IBEX, synoptic views provide you with interactive, schematic views of your instrument.  Each icon on a synoptic view represents a device attached to your instrument.  You can tailor the synoptic view to display key PVs next to the device icons.  By double-clicking on an item, you can drill down to see more detail.

The focus of this page is navigating synoptic views.  If you wish to create your own synoptic view see [[CreateandManageSynoptics]].

Selecting a Synoptic View
-------------------------

#. To view an instrument synoptic, click on the ``Synoptic`` button on the View Selector (see [[Views]]).
#. If a default synoptic has been defined for your current configuration, IBEX will display it.  The name of the synoptic will be displayed in the drop-down menu in the area labelled ``Synoptic Selection`` at the top of the synoptic display area.
#. If no default synoptic has been defined for your current configuration, IBEX will display ``--NONE--`` in the drop-down menu in the area labelled ``Synoptic Selection`` at the top of the synoptic display area and the synoptic display will be blank. 
#.  You can choose to view any synoptic defined for your instrument by in the drop-down menu in ``Synoptic Selection`` area and choosing any of the synoptics listed.  IBEX will refresh the synoptic display to show your chosen synoptic.



Synoptic Preview
   Click on the ``Synoptic Preview`` button to get a preview of how your synoptic will appear.  You can click on the ``Synoptic Preview`` button at any time.

Save as...
   Click on the ``Save as...`` button to save your changes.  You must provide a name for the synoptic view.  The name of the synoptic can contain only the characters a-z, A-Z, 0-9 and _ (underscore).  The name must also start with a character.

Cancel
   Click on the ``Cancel`` button to exit the dialog without saving your changes.

Use the Synoptic editor as follows:

#. Click on the ``Add Component`` button to add a new component to the Instrument Tree.

   #. When you add a new component, its details are shown in the Component Details pane.  It is given the default name ``New Component`` and a default type of ``UNKNOWN``.  
   #. In the Component Details pane, you can adjust the general properties of the component.

      * Give it a suitable name
      * Select the type of device it represents.  Click on the drop-down menu to select the device type.
      * Click on the ``Add New PV`` button to add blocks or PVs to be associated with the component (remember - blocks are just aliases to PVs).  Any blocks or PVs you select will be displayed below the component in the synoptic view.
      * Remove any blocks or PVs previously associated with the component.
      * You can change the order of components in the synoptic view by dragging & dropping any component to the desired position.  As you drag a component, a black line will appear to indicate the you can drop the component and it will be positioned between the two components immediately above and below the black line.  If you drop a component on top of another component, it will be positioned as "sub-component".  "Sub-components" are useful if you have several components that are grouped together as a composite unit.

   #. If you add an associated block or PV (using the ``Add New PV`` button), its details appear in the PV Details pane.  Use the the ``Select Block`` or ``Select PV`` buttons to choose a specific block or PV to associated with the component.

   #. Use the Component Target Details pane to adjust the specific properties of the component (e.g. which model of device the component represents, which component properties are needed).

      * The ``Name:`` field is a drop-down menu.  Select the name/model of the device.  Some names on the list refer to general classes of device (e.g. ``Eurotherm`` refers to all Eurotherm temperature controllers); other names refer to specific models (e.g. ``Julabo FP300`` refers to a specific model of Julabo water bath).  Whether a name is general or specific depends on whether the manufacturer of the device has chosen a common interface to all models of a device or interfaces that are unique to individual models.  When you have made your selection, a short description of the component will be displayed in the ``Description:`` field.
      * If you are not sure which name/model to select for the ``Name:`` field, click on the ``Default Target`` button.  IBEX will then display a list of names/models filtered by the Component Type field (see Component Details pane).  This will significantly reduce the size of the list (often there will be only one choice).  Choose the most appropriate name/model.
      * Clicking on the ``Clear Target`` button will clear any selection in the ``Name:`` field.
      * Below the ``Description:`` field is a table of ``Properties:``, which lists the properties belonging to the selected component.  Each property has a name and a value.  Select each property in turn to edit the value.
      * On selecting a property, the value of the property will  appear ``Value:`` field.  A description of the value is provided in the ``Description:`` field below the ``Value:`` field.  The default value might be blank.
      * Set the property value.   
      * **Please note:** Component properties are very specific to individual devices - it is impractical to give definitive advice in a user manual on the correct value for a component property.  The  ``Description:`` field will provide general advice on the type of value to be entered in the ``Value:`` field.  If you are unsure about the correct value to choose, please consult with the Experimental Controls team.

#. Click on the ``Copy Component`` button to duplicate the currently selected component.  If no component is selected, the ``Copy Component`` button is inactive.

#. Click on the ``Delete Component`` button to delete the currently selected component.  If no component is selected, the ``Delete Component`` button is inactive.

#. Toggle the ``Show Beam`` check-box to show or hide the schematic representation of the beam in the synoptic view.  By default, the beam will be shown.

