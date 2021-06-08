# Keyboard Shortcuts

- Ctrl-click on multiple lines to select them all
- Tab onto the next cell (tabbing from the last cell creates a new line)

# Common questions
### How do I copy and paste lines?

Select the line you want to copy (does not have to contiguous) and press `Ctrl+c` to copy. Press `Ctrl+v` after selecting the line where you want to
paste.

### How do I delete multiple lines?

Hold shift and click the lines to select them, then click the delete actions button.

### How do I insert an action at a given point?

Click the line you wish to insert the new line below and click duplicate action.

### How do I add a new line to the end?

Click the add action button.

### Can I tab between cells?

Yes, pressing tab to move between cells will move the focus from left to right and then onto the next line. If you tab off the end of the last line a new line will be created. 

# A tour of the UI
[[/script_generator/script_generator_ui.jpg|ScriptGenerator UI]]

1. From the drop-down here you may select a script definitions to use to generate a script.
2. This text box displays the help provided by the currently selected script definition.
3. Help options, click the arrow to open a drop down allowing access to a link to this page and an about section which contains the current version, Java version, and the Java Path.
4. If the data entered in one of the global parameters text box is not the correct type it will highlight in red, mousing over the text box will display the error.
5. Text box to enter global parameters, these are only displayed if they are defined by the selected script definition.
6. This table may not appear in your script generator. However, if it does this means there have been errors loading some of your script definitions. The error message may tell you there is an error in one of your script definitions or there has been an error loading from a specific location.
7.  The script generator table is to contain the experimental parameters that will be used by the generated script.
8.  The validity column will contain a tick and be coloured green if the row is valid.
9.  The validity column will contain a cross and be coloured a deeper red if the row is invalid.  This is dependent on the script definitions parameters_valid method.
10. Hovering over a row that is invalid (highlighted in red and with a cross mark in the validation column) will display the reason this row is invalid.  This is dependent on the script definitions parameters_valid method.
11. Select a row and press the up or down button to reorder rows.
12. Select an action or actions and click the "Copy selected actions" button to add the selected actions to the clipboard.
13. Select a row and click "Paste actions" to add the actions in the clipboard to the table.
14. Create a new action (row in the script generator table) at the bottom of the table with the "Add Action To End" button.
15. Select a row and click the "Insert Action Below" button to add a new action directly below the current action.
16. Select an action or actions and click the "Duplicate Selected Actions Below" button to create a copy of all currently selected actions directly below the last selected item.
17. Select an action or actions and click the "Delete Selected Actions" button to remove the selected actions from the table.
18. Click the "Clear All Actions" button to remove all actions from the table.
19. Click the "Generate Script" button to save out the script when all actions are ready. The button to generate a script is greyed out when the parameters aren't valid.
20. Click the "Save Parameters" button to save the current parameters to a file that can be loaded in at another time. The button to generate a script is greyed out when the parameters aren't valid.
21. Click the "Save Parameters As ..." button to save the current parameters to a file that can be loaded in at another time, specifying the file to save to rather than saving to the file last saved to or loaded. The button to generate a script is greyed out when the parameters aren't valid.
22. Click the "Load Parameters" button to load previously saved parameters in from a file.






[[/script_generator/UIScriptGenGenerated.JPG|ScriptGenerator UI Success]]
1. When all parameters are valid the get validity errors button is greyed out.
2. All parameters are valid when there are ticks in the validity columns and no rows are red.
3. Press the "Generate Script" button to generate a script from your experimental parameters and get a file message box pop up.
4. - When the script has been generated in the backend a user can provide a filename (without file path prefix or file extension).
    - They are provided with a create default filename which uses the script definition and a timestamp.
    - Can then save or save and open the file (at this stage if there is another file of the same name in the same place the user is asked if they want to overwrite).
    - Opens the file in notepad++ if notepad++ can be found.


# Loading scripts into the scripting window

Say we have generated a script named "my_script.py". We can open the scripting perspective in the ibex gui and type `g.load_script("my_script.py")`. This will then load a function called `runscript()` into the console which you can call by simply typing `runscript()` and pressing enter.