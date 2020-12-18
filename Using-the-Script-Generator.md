Here we will talk you through what you need to know to use the script generator.

# Keyboard Shortcuts

- Ctrl-click on multiple lines to select them all
- Tab onto the next cell (tabbing from the last cell creates a new line)

# Common questions

### How do I delete multiple lines?

Hold shift and click the lines to select them, then click the delete actions button.

### How do I insert an action at a given point?

Click the line you wish to insert the new line below and click duplicate action.

### How do I add a new line to the end?

Click the add action button.

### Can I tab between cells?

Yes, pressing tab to move between cells will move the focus from left to right and then onto the next line. If you tab off the end of the last line a new line will be created. 

# A tour of the UI

![ScriptGenerator UI](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_user_manual/UI.JPG)

1. The button to generate a script is greyed out when the parameters aren't valid.
2. Select an action in the table by clicking on the row and click the "Duplicate Action" button to duplicate that row into the next row down.
3. Select an action in the table by clicking on the row and click the "Delete Action" button to delete the row.
4. Create a new action (row in the script generator table) with the "Add Action" button.
5. The script generator table is to contain the experimental parameters that will be used by the generated script.
6. Select a row and press the up or down button to reorder rows.
7. The validity column will contain a tick and be coloured green if the row is valid.
8. Hovering over a row that is invalid (highlighted in red and with a cross mark in the validation column) will display the reason this row is invalid.  This is dependent on the script definitions parameters_valid method
9. The validity column will contain a cross and be coloured a deeper red if the row is invalid.  This is dependent on the script definitions parameters_valid method
10. Clicking on this button will bring up a message box describing at least some of the errors when validating the contents of the script generator table.
11. This text box displays the help provided by the currently selected script definition
12. From the drop-down here you may select a script definitions to use to generate a script.
13. This table may not appear in your script generator. However, if it does this means there have been errors loading some of your script definitions. The error message may tell you there is an error in one of your script definitions or there has been an error loading from a specific location.





![ScriptGenerator UI Success](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_user_manual/UIScriptGenGenerated.JPG)
1. When all parameters are valid the get validity errors button is greyed out.
2. All parameters are valid when there are ticks in the validity columns and no rows are red.
3. Press the "Generate Script" button to generate a script from your experimental parameters and get a file message box pop up.
4. - When the script has been generated in the backend a user can provide a filename (without file path prefix or file extension).
    - They are provided with a create default filename which uses the script definition and a timestamp.
    - Can then save or save and open the file (at this stage if there is another file of the same name in the same place the user is asked if they want to overwrite).
    - Opens the file in notepad++ if notepad++ can be found.


# Loading scripts into the scripting window

Say we have generated a script named "my_script.py". We can open the scripting perspective in the ibex gui and type `g.load_script("my_script.py")`. This will then load a function called `runscript()` into the console which you can call by simply typing `runscript()` and pressing enter.