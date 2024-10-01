Bulk Copy-Rename Utility   Copyright (C)   2024   NephX9 (original author)   
Licensed under the GNU General Public License, Version 3 (GPL-3.0)

# Bulk Copy-Rename Utility
Bulk Copy-Rename Utility is a tool I'm developing to simplify many operations I frequently perform.   
It was tested using Python 3.12.6

## What Is It?
The main purpose of Bulk Copy-Rename Utility is to simplify the process of renaming a large number of items (files/folders) by using names from existing items.   
The total number of items from which you copy the names should match the number of target items.   
The same file/folder ratio does not need to be maintained: for example, 2 files and 3 folders (5 items) can be used to rename any combination of 5 files or folders.   

This utility is specifically designed for this task. For more advanced renaming operations, the powerful "Bulk Rename Utility" (free for personal use) is recommended.

## Installation
Install the latest version of Python (3+). This utility was developed and tested using Python 3.12.6.   
Install tkfilebrowser via your terminal:   
```pip install tkfilebrowser```

## How Does It Work?
This utility features a simple GUI for navigating its functions and a console for logging information and errors.   
You can select any files or folders as the input names and any files or folders as the target items to be renamed.   
The "Rename" button remains disabled until you have the same number of input names and target items.   
The "Rename" button only clears the target items after a successful operation. Input names are not cleared by default and can be manually cleared using the corresponding button.

## Use cases
Example 1:   
You have a large number of correctly named folders, but you've worked on older, wrongly named folders.   
Now, you have outdated content in correctly named folders and updated content in wrongly named folders.   
Instead of renaming the folders one by one, you can use this utility to rename them in bulk, using the correct folder names as input and the folders to be renamed as the target folders.

Example 2:   
You have a large number of correctly named files, but you've worked on older, wrongly named files.   
Now, you have correctly named files with outdated data and wrongly named files with updated data.   
Instead of renaming the files one by one, you can use this utility to rename them in bulk, using the correct file names as input and the files to be renamed as targets.

Example 3 (General Case):   
You have a large number of files/folders and want to rename them using the names of other files/folders, or vice versa, for any reason.   
With this utility, you can easily do that.

## Known Issues
Some error control exists to prevent renaming when there are duplicates, but certain cases are only caught by exceptions thrown by the OS.

## To-Do List
- Better duplicates management: 
  - SAFE MODE -> check every target path and abort the renaming process entirely if a target path has any of either the target names or input names
  - BALANCED -> check the target path only for duplicates of the input name used for renaming that specific target, preventing any operation
  - FAST MODE -> similar to balanced mode but when a duplicate is found the renaming process is not aborted entirely, only the duplicate target is skipped
- Add input CYCLING:  when the number of input names is fewer than the number of target items, cycle through the input list when it reaches the end (with handling for duplicates, such as checking that target paths with the same assigned name are different)
- Add a JSON configuration to customize the experience (SAFE/BALACED MODE) without modifying the code, allowing runtime/terminal editing of certain elements (GUI or functions)
- Improve the GUI, for example by providing a continuous window that shows the selected input names and target items.
- Possibility to remove only single input names or targets instead of clearing all those lists

### About Me
I'm a Freelance Software Engineer and Developer.
In my free time, I create applications, fixes, patches, and mods for games I enjoy, occasionally I publish them.

### Useful Links
Check out my steam mods here:   
[My Steam Workshop](https://steamcommunity.com/profiles/76561198004659076/myworkshopfiles)

### Donations
If you have requests for specific content or you simply want to support me:   
[My Ko-fi](https://ko-fi.com/nephi90)
