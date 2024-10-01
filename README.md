Key functions:

Separate Selection for Folders:
The select_input_items method allows selecting multiple files and then prompts for folders one by one, allowing you to add folders to the input list without reopening the dialog.

Target Selection:
Similarly, in the select_target_items method, you can select target files and then choose folders individually, allowing for flexible input.

How It Works:
Selecting Input Items:
Select multiple files at once using the file dialog.
Then, you can select folders one at a time until you cancel the folder selection.

Selecting Target Items:
After input selection, select target files and folders similarly. The script checks if the counts match before proceeding to rename.

Usage:
Run the script and select the input files and folders as described.
Select the target files and folders to rename. 

IMPORTANT:
You have to keep count of the items selected by yourself, if the number of input/output items at the end of the process it's different you will get an "error" dialog. 
If you get the error for different I/O numbers you don't have to re-select the input if you don't want, you can re-select only the targets)