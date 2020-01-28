Here we will talk you through what you need to know to use the script generator.

# A tour of the UI

![ScriptGenerator UI](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_user_manual/UI.JPG)

1. This table may not appear in your script generator. However, if it does this means there have been errors loading some of your configs. The error message may tell you there is an error in one of your configs (action definitions) or there has been an error loading from a specific location.
2. From the drop-down here you may select a config (action definition) to use to generate a script.
3. Clicking on this button will bring up a message box describing at least some of the errors when validating the contents of the script generator table.
4. Hovering over a row that is invalid (highlighted in red and with a cross mark in the validation column) will display the reason this row is invalid. This reason is defined in the config.
5. The validity column will contain a cross and be coloured a deeper red if the row is invalid.
6. The validity column will contain a tick and be coloured green if the row is valid.
7. Select a row and press the up or down button to reorder rows.
8. The script generator table is to contain the experimental parameters that will be used by the generated script.
9. Create a new action (row in the script generator table) with the "Add Action" button.
10. Select an action in the table by clicking on the row and click the "Delete Action" button to delete the row.
11. The button to generate a script is greyed out when the parameters aren't valid.
12. Select an action in the table by clicking on the row and click the "Duplicate Action" button to duplicate that row into the next row down.

![ScriptGenerator UI Success](https://raw.githubusercontent.com/wiki/ISISComputingGroup/ibex_user_manual/UIScriptGenGenerated.JPG)

1. When all parameters are valid the get validity errors button is greyed out.
2. All parameters are valid when there are ticks in the validity columns and no rows are red.
3. Click "Open File" to open the file in notepad++ (alternatively copy and paste the file location to open it in your preferred editor).
4. The file message box which notifies you that a script has been generated after clicking the "Generate Script" button. Here you can copy and paste the file location or click open file to open in notepad++.
5. Press the "Generate Script" button to generate a script from your experimental parameters and get a file message box pop up.

# Loading scripts into the scripting window

Say we have generated a script named "my_script.py". We can open the scripting perspective in the ibex gui and type `g.load_script("my_script.py")`. This will then load a function called `runscript()` into the console which you can call by simply typing `runscript()` and pressing enter.