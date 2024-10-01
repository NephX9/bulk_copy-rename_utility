# bulk_copy-rename_utility
This repository is for an utility I'm developing to ease many operation I have to do during my work and hobbies.
It was tested using Python 3.12.6
This is MIT licensed.

## What Is It
bulk_copy-rename_utility main purpose is to ease the process of renaming a big number of items (files/folders) using already existing names from other items. 
The total number of items from which you copy the names should be the same number of the target ones.
Keeping the same files/folders ratio it's not needed: 2 files + 3 folders (= 5 items) can freely rename any ratio of files/folders if the total it's still 5.

This utility doesn't provide much more than that, for almost all the other rename operations you can think of there's the powerful "Bulk Rename Utility" free to download (for personal use only).

## Installation
Install the latest version of Python (3+), this utility was developed and tested using Python 3.12.6.
Install tkfilebrowser from your terminal		pip install tkfilebrowser

## How Does It Work
This utility has a simple GUI to navigate the functions and a console to log info/errors.
You can choose any file and folder for the input names and any file or folder as target item to rename.
The Rename button is grayed out until you have the same number of input names and target items.
The Rename button clears the targets only if the operation is successful, the input names are not cleared by default, you have to do so manually with the related button.

##Known Issues
There is some form of error control to prevent the execution of the rename function in presence of duplicates but some cases just catch the exception thrown by the os.
Nothin


## Examples
Example 1:
You have a large number of correctly named folders but you worked on older/wongly named folders and now you have old contents in correctly named folders and updated contents in wrongly named folders.
Instead of renaming the folders one by one, you can use this utility to rename in bulk using the correct folders names as input and the folders to rename as target folders.
Example 2:
You have a large number of correctly named files but you worked on older/wongly named files and now you have correctly named files with outated data and updated data in wrongly named files.
Instead of renaming the files one by one, you can use this utility to rename in bulk using the correct files names as input and the files to rename as targets.
Example 3 (general case):
You have a large number of files/folders and you want to rename them with the same names of some others files/folders or viceversa, for whatever reasons.
With this utility you can do this.

##TO DO
-Rename even when the number of input names it's less than the number of target items, cycling the input list when it reach the end (need handling the duplicates, i.e. chechinkg the targets paths with the same assigned name are different)
-Add a json to customize the experience without touching the code, i.e. to edit some elements (GUI or functions) at runtime/terminal
-Improve the GUI, for example providing a continuos window showing the input names and target items selected

### About Me
I'm a Freelance Software Engineer and in my free time I make applications, fixes, patches and mods for games I like, sometimes I publish them.

### Useful Links
Check out my steam mods here:
https://steamcommunity.com/profiles/76561198004659076/myworkshopfiles/?appid=211820](https://steamcommunity.com/profiles/76561198004659076/myworkshopfiles/

### Donations
If you have requests for specific content or you simply want to support me:
https://ko-fi.com/nephi90
