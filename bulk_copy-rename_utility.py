# Bulk Copy-Rename Utility  Copyright (C)   2024    NephX9 (original author)
# Licensed under the GNU General Public License, Version 3 (GPL-3.0)

import tkinter as tk
import os
import shutil
#from tkinter import ALL
from tkinter import messagebox
#from tkinter import dialog
#from tkinter.filedialog import askdirectory
from tkfilebrowser import askopendirnames, askopenfilenames

def display_notice():
    print("Bulk Copy-Rename Utility  Copyright (C) 2024  NephX9 (original author)")
    print("Licensed under the GNU General Public License, Version 3 (GPL-3.0)\n")
    print("This program comes with ABSOLUTELY NO WARRANTY.")
    print("This is free software, and you are welcome to redistribute it under certain conditions.")
    print("Please see the LICENSE.md file for details.\n\n")
    print("Program ready, use the GUI to proceed.\n")

class BatchRenameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Batch Rename Tool")
        self.master.geometry("300x380")
        self.center_window(self.master)

        self.input_items = [] # list of file(s)/folder(s) names
        self.target_items = [] # list of file(s)/folder(s) full paths
        self.app_mode = 1 # Default = 1 (BALANCED) ; Other modes: 0 = SAFE;   1 = BALANCE;    2 = FAST
        self.default_path = os.path.expanduser("~/Desktop")  # Default to user desktop
        #self.last_accessed_path = self.default_path  # Initial last accessed path
        self.last_inputs_accessed_path = self.default_path  # Initial last accessed path for inputs
        self.last_targets_accessed_path = self.default_path  # Initial last accessed path for targets

        # Special function1 related attributes
        self.special_input_list = []  # Holds special input folder paths
        self.special_output_file = None  # Holds the special output filename
        self.last_special_accessed_path = self.default_path  # Initial last accessed path for special function 1

        # Main Buttons
        self.select_input_button = tk.Button(master, text="Select Input", command=self.open_input_dialog)
        self.select_input_button.pack(pady=10)

        self.select_target_button = tk.Button(master, text="Select Target", command=self.open_target_dialog)
        self.select_target_button.pack(pady=10)

        self.show_selected_button = tk.Button(master, text="Show Selected Items", command=self.show_selected_items)
        self.show_selected_button.pack(pady=10)

        self.clear_selection_button = tk.Button(master, text="Clear Selection", command=self.open_clear_dialog)
        #self.clear_selection_button = tk.Button(master, text="Clear Data", command=self.clear_data)
        self.clear_selection_button.pack(pady=10)

        self.clear_console_button = tk.Button(master, text="Clear Console", command=self.clear_console)
        self.clear_console_button.pack(pady=10)

        self.rename_button = tk.Button(master, text="Rename", command=self.rename_items, state=tk.DISABLED)
        self.rename_button.pack(pady=10)
        
        # Special function I/O: select some folders as inputs and a single file as output
        # Special function run: For each folder selected as input, the function searches for files with the same name as the selected output file.
        # Special function run: If a match is found, it writes the name of the folder that is six levels above the file (relative to its location in the directory hierarchy) into the file.
        # Special function run: The intended use is to have only one file with the same name as the selected output file, 6 levels deep, in every selected input folder
        self.special_function_button = tk.Button(master, text="SPECIAL FUNCTION", command=self.open_special_function_dialog)
        self.special_function_button.pack(pady=10)
    
    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")
    
    def open_input_dialog(self):
        self.close_sub_dialogs()
        dialog = tk.Toplevel(self.master)
        dialog.title("Select Input")
        dialog.geometry("300x120")
        self.center_window(dialog)
        dialog.geometry("+{}+{}".format(self.master.winfo_x() - 250, self.master.winfo_y() + 50))  # Shift to the left        

        select_input_files_button = tk.Button(dialog, text="Select Input File(s)", command=lambda: self.select_input_items(0))
        select_input_files_button.pack(pady=10)

        select_input_folders_button = tk.Button(dialog, text="Select Input Folder(s)", command=lambda: self.select_input_items(1))
        select_input_folders_button.pack(pady=10)
        dialog.focus_force()
    
    def open_target_dialog(self):
        self.close_sub_dialogs()
        dialog = tk.Toplevel(self.master)
        dialog.title("Select Target")
        dialog.geometry("300x120")
        self.center_window(dialog)
        dialog.geometry("+{}+{}".format(self.master.winfo_x() + 250, self.master.winfo_y() + 50))  # Shift to the right        

        select_target_files_button = tk.Button(dialog, text="Select Target File(s)", command=lambda: self.select_target_items(0))
        select_target_files_button.pack(pady=10)

        select_target_folders_button = tk.Button(dialog, text="Select Target Folder(s)", command=lambda: self.select_target_items(1))
        select_target_folders_button.pack(pady=10)
        dialog.focus_force()
    
    def open_clear_dialog(self):
        self.close_sub_dialogs()
        dialog = tk.Toplevel(self.master)
        dialog.title("Clear Selection")
        dialog.geometry("300x200")
        self.center_window(dialog)
        dialog.geometry("+{}+{}".format(self.master.winfo_x(), self.master.winfo_y() + 200))
        
        clear_both_button = tk.Button(dialog, text="Clear All Items Selected", command=self.clear_both_selection)
        clear_both_button.pack(pady=10)

        clear_input_button = tk.Button(dialog, text="Clear Input List", command=self.clear_input_selection)
        clear_input_button.pack(pady=10)

        clear_target_button = tk.Button(dialog, text="Clear Target List", command=self.clear_target_selection)
        clear_target_button.pack(pady=10)
        dialog.focus_force()
    
    def open_special_function_dialog(self):
        self.close_sub_dialogs()
        dialog = tk.Toplevel(self.master)
        dialog.title("Special Function")
        dialog.geometry("300x270")
        self.center_window(dialog)
        dialog.geometry("+{}+{}".format(self.master.winfo_x(), self.master.winfo_y()))

        special_input_button = tk.Button(dialog, text="SPECIAL INPUT", command=self.special_input_dialog)
        special_input_button.pack(pady=10)

        special_output_button = tk.Button(dialog, text="SPECIAL OUTPUT", command=self.special_output_dialog)
        special_output_button.pack(pady=10)

        special_data_button = tk.Button(dialog, text="SPECIAL DATA", command=self.special_data)
        special_data_button.pack(pady=10)
        
        special_clear_data_button = tk.Button(dialog, text="SPECIAL CLEAR DATA", command=self.special_clear_data)
        special_clear_data_button.pack(pady=10)

        self.special_run_button = tk.Button(dialog, text="SPECIAL RUN", command=self.special_run, state=tk.DISABLED)
        self.special_run_button.pack(pady=10)
        self.update_special_run_button_state()
        dialog.focus_force()
    
    def special_input_dialog(self):
        contex_index = 2 # 2 here is for special function
        try:
            folders = askopendirnames(title="Select Folders", initialdir=self.get_initial_directory(contex_index))
            if folders and folders[0]:
                self.last_special_accessed_path = os.path.dirname(folders[0])  # Update last accessed path during special function 1 selection
                for folder in folders:
                    if folder in self.special_input_list:                        
                        print(f"\nSPECIAL INPUT SELECTION ABORTED, Cannot Add: '{os.path.basename(folder)}' ,Path already present\n")
                        return
                self.special_input_list.extend(folders)  # Add folders to the special input list            
                for folder in self.special_input_list:
                    print(f"Added path: {folder}")
            self.update_special_run_button_state()
        except Exception as e:
            print(f"Error while selecting special input path: {e}")
            return
    
    def special_output_dialog(self):
        contex_index = 2 # 2 here is for special function
        try:
            file = askopenfilenames(title="Select Output File", filetypes=[("All files", "*.*")], initialdir=self.get_initial_directory(contex_index))
            if file:
                self.last_special_accessed_path = os.path.dirname(file[0])  # Update last accessed path during special function selection
                self.special_output_file = os.path.basename(file[0])  # Store only the filename
                print(f"Selected special output file: {self.special_output_file}")
            self.update_special_run_button_state()
        except Exception as e:
            print(f"Error selecting output file: {e}")
            return
    
    def special_data(self):
        if self.special_input_list:
            print("SPECIAL INPUT paths:")
            for folder in self.special_input_list:
                print(folder)
        else:
            print("SPECIAL INPUT paths: NONE SELECTED YET")
        if self.special_output_file:
            print(f"SPECIAL OUTPUT file: {self.special_output_file}")
        else:
            print(f"SPECIAL OUTPUT file: NOT SELECTED YET")
    
    def special_clear_data(self):
        if self.special_input_list:
            self.special_input_list.clear()
        if self.special_output_file:
            self.special_output_file=""
        print("Special data have been cleared.")
        self.update_special_run_button_state()    

    def special_run(self):
        if not self.special_input_list or not self.special_output_file:
            print("No special input paths or special output file specified.")
            return
        
        for folder in self.special_input_list:
            for root, dirs, files in os.walk(folder):
                if self.special_output_file in files:
                    found_file_path = os.path.join(root, self.special_output_file)
                    #path_parts = found_file_path.split(os.sep)[-6:]  # Last 6 steps of the path
                    path_parts = found_file_path.split(os.sep)[-6:-5]  # 6th step of the path
                    try:
                        with open(found_file_path, 'a') as f:
                            #f.write("\n" + os.sep.join(path_parts))  # Append last 6 steps of the path to the file
                            f.write(os.sep.join(path_parts))  # Append 6th step of the path to the file
                        print(f"Updated '{found_file_path}' file, ancestor folder name '{os.sep.join(path_parts)}' written.")
                    except Exception as e:
                        print(f"Failed to write the ancestor folder name from 'os.sep.join(path_parts)' variable at the path in 'found_file_path' variable: {e}")
                        return
        print("SPECIAL RUN terminated, clearing special data..")
        self.special_clear_data()    
    
    def select_input_items(self, item_type):
        contex_index = 0 # 0 here is for inputs, 1 is for outputs
        try:
            item_type_name = ""
            if item_type == 0:
                items = askopenfilenames(title="Select Input File(s)", filetypes=[("All files", "*.*")],
                                     initialdir=self.get_initial_directory(contex_index)) # the 
                item_type_name = "file"
            elif item_type == 1:
                items = askopendirnames(title="Select Input Folder(s)", initialdir=self.get_initial_directory(contex_index))
                item_type_name = "folder"
            else:
                raise ValueError("CUSTOM EXCEPTION:\nUnexpected 'item_type' value, it can only be 0 (File) or 1 (Folder).")
            valid = True
            if items and items[0]:
                self.last_inputs_accessed_path = os.path.dirname(items[0])  # Update last accessed path during input(s) selection
                for item in items:
                    if os.path.basename(item) in self.input_items:
                        valid = False
                        print(f"\nINPUT SELECTION ABORTED:\nCannot add '{os.path.basename(item)}' {item_type_name} as input, name already present in input list.")
                        break
                    else:
                        for target_item in self.target_items:
                            if os.path.basename(item) == os.path.basename(target_item):
                                valid = False
                                print(f"\nINPUT SELECTION ABORTED:\nCannot add '{os.path.basename(item)}' {item_type_name} as input, name already present in target list.")
                                break
                            elif self.exists_in_path(os.path.basename(item), os.path.dirname(target_item)):
                                valid = False
                                print(f"\nINPUT SELECTION ABORTED:\nCannot add '{os.path.basename(item)}' {item_type_name} as input, name already present in {target_item}' target directory.")
                                break
                if valid == True:
                    for item in items:
                        self.input_items.append(os.path.basename(item))
                        print(f"'{os.path.basename(item)}' {item_type_name} name added to input list.")
                    self.update_rename_button_state()
        except ValueError as ve:
            print("ValueError exception caught during input(s) selection: \n", ve)
            return
        except Exception as e:
            print("Exception caught during input(s) selection: \n", e)
            return    
    
    def select_target_items(self, item_type):
        contex_index = 1 # 1 here is for outputs, 0 is for inputs
        try:
            item_type_name = ""
            if item_type == 0:
                items = askopenfilenames(title="Select Target File(s)", filetypes=[("All files", "*.*")],
                                     initialdir=self.get_initial_directory(contex_index))
                item_type_name = "file"
            elif item_type == 1:
                items = askopendirnames(title="Select Target Folder(s)", initialdir=self.get_initial_directory(contex_index))
                item_type_name = "folder"
            else:
                raise ValueError("TARGET SELECTION ABORTED:\nUnexpected 'item_type' value, it can only be 0 (file) or 1 (folder).")
            valid = True
            if items and items[0]:
                self.last_targets_accessed_path = os.path.dirname(items[0])  # Update last accessed path during target(s) selection
                for item in items:
                    if os.path.basename(item) in self.input_items:
                        valid = False
                        print(f"\nTARGET SELECTION ABORTED:\nCannot add '{item}' {item_type_name} as target, name already present in input list.")
                        break
                    elif item in self.target_items:                       
                        valid = False
                        print(f"\nTARGET SELECTION ABORTED:\nCannot add '{item}' {item_type_name} as target, target already selected.")
                        break
                    else:
                        for input_item in self.input_items:
                            if self.exists_in_path(input_item, os.path.dirname(item)):
                                valid = False
                                print(f"\nTARGET SELECTION ABORTED:\nCannot add '{item}' {item_type_name} as target, the target directory already contain the name '{input_item}' from the input list.")
                                break
                if valid == True:
                    for item in items:
                        self.target_items.append(item)
                        print(f"'{item}' {item_type_name} added to target list.")
                    self.update_rename_button_state()
        except ValueError as ve:
            print("ValueError exception caught during target(s) selection: \n", ve)
            return
        except Exception as e:
            print("Exception caught during target(s) selection: \n", e)
            return
    
    def show_selected_items(self):
        self.close_sub_dialogs()
        if not self.input_items and not self.target_items:
            print("No items have been selected.")
            return

        #input_names = "\n".join(os.path.basename(item) for item in self.input_items) # self.input_items now only cointains the input names
        input_names = "\n".join(self.input_items) # self.input_items now only cointains the input names
        target_names = "\n".join(os.path.basename(item) for item in self.target_items)

        message = "Input Items:\n" + (input_names if input_names else "None") + \
                  "\n\nTarget Items:\n" + (target_names if target_names else "None")
        print(message)
    
    def clear_input_selection(self):
        self.input_items.clear()
        print("Input items have been cleared.")
        self.update_rename_button_state()
    
    def clear_target_selection(self):
        self.target_items.clear()
        print("Target items have been cleared.")
        self.update_rename_button_state()
    
    def clear_both_selection(self):
        self.input_items.clear()
        self.target_items.clear()
        print("Both input and target items have been cleared.")
        self.update_rename_button_state()
        self.close_sub_dialogs()
    
    '''
    def clear_data(self):
        self.close_sub_dialogs()
        self.input_items.clear()
        self.target_items.clear()
        print("Both input and target items have been cleared.")
        self.update_rename_button_state()
    '''
    
    def clear_console(self):
        self.close_sub_dialogs()
        print("\n" * 100)  # Clear console output by printing new lines
        display_notice()
    
    def close_sub_dialogs(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()
    
    def update_special_run_button_state(self):            
        if self.special_input_list and self.special_output_file:
            self.special_run_button.config(state=tk.NORMAL)
        else:
            self.special_run_button.config(state=tk.DISABLED)
    
    #When not in SAFE MODE allow for len(self.input_items) < len(self.target_items)  ;   when it is so, cycle self.input_items list when "assigning" names on targets
    #Never allow for len(self.input_items)=1, use the application suggested on my github for that
    def update_rename_button_state(self):
        if self.input_items and self.target_items and len(self.input_items) == len(self.target_items):
            self.rename_button.config(state=tk.NORMAL)
        else:
            self.rename_button.config(state=tk.DISABLED)
    
    #PLACEHOLDER FUNCTION TO PREVENT DUPLICATES IN A TARGET DIRECTORY - now implemented
    #Takes a single input name and a single target (path)
    #Returns false if any file/folder in the target directory has the same name as the input, return true otherwise
    def exists_in_path(self, input_name, target_dir):
        #print("PLACEHOLDER FUNCTION CALLED")
        already_exists = False        
        #Logic to check dir -- START
        #target_dir = os.path.dirname(target_item)
        new_target_path = os.path.join(target_dir, input_name)
        if os.path.exists(new_target_path):
            already_exists = True
        #Logic to check dir -- END
        #if already_exists:
        #    print("PATH CHECK FAILED:") #move and improve this message to the caller when implemented
        
        return already_exists
    
    def rename_items(self):
        self.close_sub_dialogs()
        if not self.input_items or not self.target_items:
            print("You need atleast one input name and one target item to rename.")
            return
        elif len(self.input_items) != len(self.target_items):
            print("The number of input names and target items must be the same.")
            return
        
        for input_item, target_item in zip(self.input_items, self.target_items):
            target_dir = os.path.dirname(target_item)  # Keep the target's directory path
            new_target_path = os.path.join(target_dir, input_item)  # Rename target item            
            try:
                if not os.path.exists(target_item):
                    raise FileNotFoundError(f"Target '{target_item}' not found.\nIt was renamed or (re)moved outside of the application.")
                if self.exists_in_path(input_item, os.path.dirname(target_item)):
                    raise Exception(f"Target '{new_target_path}' already exist.\nAnother item named '../{input_item}' was moved or renamed in the target directory outside of the application.")
            except FileNotFoundError as nfe:
                print(f"RENAME PROCESS ABORTED, no item was renamed:\n{nfe}")
                messagebox.showerror("Error", "RENAME PROCESS ABORTED.\nItems changed outside of the application, check the console log for more info.")
                return
            except Exception as e:
                print(f"RENAME PROCESS ABORTED, no item was renamed:\n{e}")
                messagebox.showerror("Error", "RENAME PROCESS ABORTED.\nItems changed outside of the application, check the console log for more info.")
                return
        
        for input_item, target_item in zip(self.input_items, self.target_items):
            # new_name = os.path.basename(input_item)  # Get the name from input item <- now input item it's already the name
            target_dir = os.path.dirname(target_item)  # Keep the target's directory path
            new_target_path = os.path.join(target_dir, input_item)  # Rename target item            
            try:
                # Rename the target item to the corresponding input name
                os.rename(target_item, new_target_path)
                print(f"Renamed '{target_item}' to '../{input_item}'")
            except Exception as e:
                print(f"Failed to rename '{target_item}' to '../{input_item}':\n{e}")
                print("WARNING: some files/folders may have been renamed before the process was aborted. Check the console log for more info.")
                messagebox.showerror("Error", "WARNING: some files/folders may have been renamed before the process was aborted. Check the console log for more info.")
                return
                    
        print("All items renamed successfully!")
        # self.clear_target_selection()   # not necessary, let the user decide
        self.update_rename_button_state()
    
    def get_initial_directory(self, contex_index):
        # Check if the last accessed path is valid
        if contex_index == 0 and os.path.exists(self.last_inputs_accessed_path): # Normal function: for inputs
            return self.last_inputs_accessed_path
        elif contex_index == 1 and os.path.exists(self.last_targets_accessed_path): # Normal function:  for targets
            return self.last_targets_accessed_path
        elif contex_index == 2 and os.path.exists(self.last_special_accessed_path): # Special function: same path remembered for both the input folders and the target file
            return self.last_special_accessed_path
        else:
            # If not valid, return the default path (user's desktop)
            #return os.path.expanduser("~/Desktop")
            return self.default_path
    

if __name__ == '__main__':
    try:
        root = tk.Tk()
        display_notice()
        app = BatchRenameApp(root)
        root.mainloop()
    except Exception as e:
        print(f"GENERIC EXCEPTION CAUGHT:\n{e}")
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
