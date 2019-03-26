[[Scripting|scripting]] > [[The Scripting Console|the-scripting-console]]

Using Genie Python in the IBEX Client
=====================================

Genie python can be used inside the IBEX client by using the scripting console. To start this press the scripting button in the sidebar:

![Toolbar](genie_python_and_ibex/OpenTheScriptingPerspective.png)

This console will let you type genie commands.  Pressing "Page Up" will display a window containing the command history.  Previous commands can be selected from the list or searched for using the text box at the bottom.

The toolbar in the top right provides additional functionality.

![Toolbar](genie_python_and_ibex/TheScriptingPerspectiveToolbar.png)

From left to right these buttons do the following:

1. Stop the whole console. This will stop the current script and remove the console from view, useful if you are running multiple consoles.
1. Save the text that's in the console to file.
1. Stop the currently running script. This is useful if you realise that the script is doing something wrong. (This can also be done by pressing Ctrl+C)
1. Clear the console. This will remove all the text from the window, be careful though as this WON'T stop the current script.
1. Pin the console. This is not used.
1. Switch to a different console. This will be greyed out if you only have one console running.
1. Start a new console or a new view. You can use this to start a new console by selecting PyDev Console -> Python Console -> Ok. Be careful! Having multiple consoles running can lead to different consoles 'fighting' for control of the instrument.