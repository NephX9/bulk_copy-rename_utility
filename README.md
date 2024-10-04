Bulk Copy-Rename Utility   Copyright (C)   2024   NephX9 (original author)
<br>
Licensed under the GNU General Public License, Version 3 (GPL-3.0)
<br><br>
# Bulk Copy-Rename Utility
Bulk Copy-Rename Utility is a tool I'm developing to simplify many operations I frequently perform.<br>
It was tested using Python 3.12.6
<br><br>
## What Is It?
The main purpose of Bulk Copy-Rename Utility is to simplify the process of renaming a large number of items (files/folders) by using names from existing items.   
The total number of items from which you copy the names should match the number of target items.   
The same file/folder ratio does not need to be maintained: for example, 2 files and 3 folders (5 items) can be used to rename any combination of 5 files or folders.   
   
This utility is specifically designed for this task. For more advanced renaming operations, the powerful "Bulk Rename Utility" (free for personal use) is recommended.
<br><br>
## Installation
Install the latest version of Python (3+). This utility was developed and tested using Python 3.12.6.   
Install tkfilebrowser via your terminal:   
```pip install tkfilebrowser```
<br><br>
## How Does It Work?
This utility features a simple GUI for navigating its functions and a console for logging information and errors.   
You can select any file or folder as inputs and any file or folder as the target items to be renamed.   
The "Rename" button stays disabled until you have the same number of inputs and targets.   
The "Rename" button only clears the target items after a successful operation.   
Input names are not cleared by default and can be manually cleared using the corresponding button.   
<br>
**IMPORTANT:**   
This application processes files' extensions as part of the items' names, so **"name.txt" is different than "name.md" and they can coexist in the same directory**, just as how modern OSs process them.
<br><br>
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
<br><br>
## Known Issues
Some error control exists to prevent renaming when there are duplicates, but certain cases are only caught by exceptions thrown by the OS.
<br><br>
## To-Do List
- Better duplicates management modes (SAFE/BALANCED/FAST)
- Add a JSON configuration to customize the experience (SAFE/BALANCED/FAST MODE) without modifying the code, allowing runtime/terminal editing of certain elements (GUI or functions)
- Improve the GUI, for example by providing a continuous window that shows the selected input names and target items.
- Possibility to remove only single input names or targets instead of clearing all those lists
<br><br>
### About Me
I'm a Freelance Software Engineer and Developer.
In my free time, I create applications, fixes, patches, and mods for games I enjoy, occasionally I publish them.
<br><br>
### Useful Links
Check out my steam mods here:   
[My Steam Workshop](https://steamcommunity.com/profiles/76561198004659076/myworkshopfiles)

### Donations
If you have requests for specific content or you simply want to support me:   
[My Ko-fi](https://ko-fi.com/nephi90)
