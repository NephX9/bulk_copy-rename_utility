# Bulk Copy-Rename Utility  Copyright (C)   2024    NephX9 (original author)
# Licensed under the GNU General Public License, Version 3 (GPL-3.0)


import tkinter as tk
import os
import shutil
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
        self.master.geometry("300x320")
        self.center_window(self.master)

        self.input_items = []
        self.target_items = []
        self.default_path = os.path.expanduser("~/Desktop")  # Default to user desktop
        self.last_accessed_path = self.default_path  # Initial last accessed path

        # Custom function related attributes
        self.special_input_list = []  # Holds special input folder paths
        self.special_output_file = None  # Holds the special output filename

        # Main Buttons
        self.select_input_button = tk.Button(master, text="Select Input", command=self.open_input_dialog)
        self.select_input_button.pack(pady=10)

        self.select_target_button = tk.Button(master, text="Select Target", command=self.open_target_dialog)
        self.select_target_button.pack(pady=10)

        self.show_selected_button = tk.Button(master, text="Show Selected Items", command=self.show_selected_items)
        self.show_selected_button.pack(pady=10)

        self.clear_selection_button = tk.Button(master, text="Clear Selection", command=self.open_clear_dialog)
        #only clear all at once?
        self.clear_selection_button.pack(pady=10)

        self.clear_console_button = tk.Button(master, text="Clear Console", command=self.clear_console)
        self.clear_console_button.pack(pady=10)

        self.rename_button = tk.Button(master, text="Rename", command=self.rename_items, state=tk.DISABLED)
        self.rename_button.pack(pady=10)
        
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
        dialog.geometry("300x200")
        self.center_window(dialog)
        dialog.geometry("+{}+{}".format(self.master.winfo_x() - 250, self.master.winfo_y() + 50))  # Shift to the left        

        select_files_button = tk.Button(dialog, text="Select Input Files", command=self.select_input_files)
        select_files_button.pack(pady=10)

        select_folders_button = tk.Button(dialog, text="Select Input Folders", command=self.select_input_folders)
        select_folders_button.pack(pady=10)

    def open_target_dialog(self):
        self.close_sub_dialogs()
        dialog = tk.Toplevel(self.master)
        dialog.title("Select Target")
        dialog.geometry("300x200")
        self.center_window(dialog)
        dialog.geometry("+{}+{}".format(self.master.winfo_x() + 250, self.master.winfo_y() + 50))  # Shift to the right        

        select_files_button = tk.Button(dialog, text="Select Target Files", command=self.select_target_files)
        select_files_button.pack(pady=10)

        select_folders_button = tk.Button(dialog, text="Select Target Folders", command=self.select_target_folders)
        select_folders_button.pack(pady=10)

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

    def open_special_function_dialog(self):
        self.close_sub_dialogs()
        dialog = tk.Toplevel(self.master)
        dialog.title("Custom Function")
        dialog.geometry("300x300")
        self.center_window(dialog)
        dialog.geometry("+{}+{}".format(self.master.winfo_x(), self.master.winfo_y() + 30))

        special_input_button = tk.Button(dialog, text="SPECIAL INPUT", command=self.special_input_dialog)
        special_input_button.pack(pady=10)

        special_output_button = tk.Button(dialog, text="SPECIAL OUTPUT", command=self.special_output_dialog)
        special_output_button.pack(pady=10)

        special_data_button = tk.Button(dialog, text="SPECIAL DATA", command=self.special_data)
        special_data_button.pack(pady=10)
        
        special_clear_data_button = tk.Button(dialog, text="SPECIAL CLEAR DATA", command=self.special_clear_data)
        special_clear_data_button.pack(pady=10)

        special_run_button = tk.Button(dialog, text="SPECIAL RUN", command=self.special_run)
        special_run_button.pack(pady=10)

    def special_input_dialog(self):
        folders = askopendirnames(title="Select Folders", initialdir=self.get_initial_directory())
        if folders:
            self.special_input_list.extend(folders)  # Add folders to the special input list
        for folder in self.special_input_list:
            print(f"Adding {folder}")

    def special_output_dialog(self):
        file = askopenfilenames(title="Select Output File", filetypes=[("All files", "*.*")], initialdir=self.get_initial_directory())
        if file:
            self.special_output_file = os.path.basename(file[0])  # Store only the filename
            print(f"Selected special output file: {self.special_output_file}")

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

    def special_run(self):
        if not self.special_input_list or not self.special_output_file:
            print("No special input paths or special output file specified.")
            return

        for folder in self.special_input_list:
            for root, dirs, files in os.walk(folder):
                if self.special_output_file in files:
                    found_file_path = os.path.join(root, self.special_output_file)
                    path_parts = found_file_path.split(os.sep)[-6:]  # Last 6 steps of the path
                    with open(found_file_path, 'a') as f:
                        f.write("\n" + os.sep.join(path_parts))  # Append last 6 steps of the path to the file
                    print(f"Updated '{found_file_path}' with path: {os.sep.join(path_parts)}")

    def select_input_files(self):
        try:
            files = askopenfilenames(title="Select Input Files", filetypes=[("All files", "*.*")],
                                     initialdir=self.get_initial_directory())
            if files:
                for file in files:
                    if file in self.input_items or file in self.target_items:
                        print(f"Cannot add '{os.path.basename(file)}': already selected as input or target.")
                    else:
                        self.input_items.append(file)
                        print(f"'{os.path.basename(file)}' file added as input")
                self.last_accessed_path = os.path.dirname(files[0])  # Update last accessed path
            self.update_rename_button_state()
        except Exception as e:
            print(f"Error selecting input files: {e}")

    def select_input_folders(self):
        try:
            folders = askopendirnames(title="Select Input Folders", initialdir=self.get_initial_directory())
            if folders:
                for folder in folders:
                    if folder in self.input_items or folder in self.target_items:
                        print(f"Cannot add '{os.path.basename(folder)}': already selected as input or target.")
                    else:
                        self.input_items.append(folder)
                        print(f"'{os.path.basename(folder)}' folder added as input")
                self.last_accessed_path = os.path.dirname(folders[0])  # Update last accessed path
            self.update_rename_button_state()
        except Exception as e:
            print(f"Error selecting input folders: {e}")

    def select_target_files(self):
        try:
            files = askopenfilenames(title="Select Target Files", filetypes=[("All files", "*.*")],
                                     initialdir=self.get_initial_directory())
            if files:
                for file in files:
                    if file in self.input_items or file in self.target_items:
                        print(f"Cannot add '{os.path.basename(file)}': already selected as input or target.")
                    else:
                        self.target_items.append(file)
                        print(f"'{os.path.basename(file)}' file added as target")
                self.last_accessed_path = os.path.dirname(files[0])  # Update last accessed path
            self.update_rename_button_state()
        except Exception as e:
            print(f"Error selecting target files: {e}")

    def select_target_folders(self):
        try:
            folders = askopendirnames(title="Select Target Folders", initialdir=self.get_initial_directory())
            if folders:
                for folder in folders:
                    if folder in self.input_items or folder in self.target_items:
                        print(f"Cannot add '{os.path.basename(folder)}': already selected as input or target.")
                    else:
                        self.target_items.append(folder)
                        print(f"'{os.path.basename(folder)}' folder added as target")
                self.last_accessed_path = os.path.dirname(folders[0])  # Update last accessed path
            self.update_rename_button_state()
        except Exception as e:
            print(f"Error selecting target folders: {e}")

    def show_selected_items(self):
        self.close_sub_dialogs()
        if not self.input_items and not self.target_items:
            print("No items have been selected.")
            return

        input_names = "\n".join(os.path.basename(item) for item in self.input_items)
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

    def clear_console(self):
        self.close_sub_dialogs()
        print("\n" * 100)  # Clear console output by printing new lines
        display_notice()

    def close_sub_dialogs(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()

    #When not in SAFE MODE allow for len(self.input_items) < len(self.target_items)  ;   when it is so, cycle self.input_items list when "assigning" names on targets
    #Never allow for len(self.input_items)=1, use the application suggested on my github for that
    def update_rename_button_state(self):
        if len(self.input_items) == len(self.target_items) and self.input_items:
            self.rename_button.config(state=tk.NORMAL)
        else:
            self.rename_button.config(state=tk.DISABLED)

    #PLACEHOLDER FUNCTION TO PREVENT DUPLICATES IN A TARGET DIRECTORY
    #Takes a single input name and a single target (path)
    #Returns false if any file/folder in the target directory has the same name as the input, return true otherwise
    def validate_target_dir(self):
        print("PLACEHOLDER FUNCTION CALLED")
        validated = False        
        #Logic to check dir -- START
        validated = True 
        #Logic to check dir -- END
        if not validated:
            print("CHECK FAILED:") #move and improve this message to the caller when implemented
        
        return validated        

    def rename_items(self):
        self.close_sub_dialogs()
        if len(self.input_items) != len(self.target_items):
            print("The number of input and target items must be the same!")
            return

        for input_item, target_item in zip(self.input_items, self.target_items):
            new_name = os.path.basename(input_item)  # Get the name from input item
            target_dir = os.path.dirname(target_item)  # Keep the target's directory path
            new_target_path = os.path.join(target_dir, new_name)  # Rename target item

            try:
                # Rename the target item to match the input item
                os.rename(target_item, new_target_path)
                print(f"Renamed '{target_item}' to '{new_name}'")
            except Exception as e:
                print(f"Failed to rename '{target_item}' to '{new_name}': {e}")
                return

        print("Items renamed successfully!")
        self.clear_target_selection()  # Only clear the target items after renaming

    def get_initial_directory(self):
        # Check if the last accessed path is valid
        if os.path.exists(self.last_accessed_path):
            return self.last_accessed_path
        else:
            # If not valid, return the default path (user's desktop)
            return os.path.expanduser("~/Desktop")


if __name__ == '__main__':
    root = tk.Tk()
    display_notice()
    app = BatchRenameApp(root)
    root.mainloop()
