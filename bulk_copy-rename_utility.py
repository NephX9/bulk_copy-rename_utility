# Bulk Copy-Rename Utility  Copyright (C)   2024    NephX9 (original author)
# Licensed under the GNU General Public License, Version 3 (GPL-3.0)


import tkinter as tk
from tkinter import messagebox
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
        self.default_path = os.path.expanduser("~/Desktop")  # Default to user home directory
        self.last_accessed_path = self.default_path  # Initial last accessed path is user home

        # Main Buttons
        self.select_input_button = tk.Button(master, text="Select Input", command=self.open_input_dialog)
        self.select_input_button.pack(pady=10)

        self.select_target_button = tk.Button(master, text="Select Target", command=self.open_target_dialog)
        self.select_target_button.pack(pady=10)

        self.show_selected_button = tk.Button(master, text="Show Selected Items", command=self.show_selected_items)
        self.show_selected_button.pack(pady=10)

        self.clear_selection_button = tk.Button(master, text="Clear Selection", command=self.open_clear_dialog)
        self.clear_selection_button.pack(pady=10)

        self.clear_console_button = tk.Button(master, text="Clear Console", command=self.clear_console)
        self.clear_console_button.pack(pady=10)

        self.rename_button = tk.Button(master, text="Rename", command=self.rename_items, state=tk.DISABLED)
        self.rename_button.pack(pady=10)

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
        dialog.geometry("+{}+{}".format(self.master.winfo_x(), self.master.winfo_y() + 300))

        clear_input_button = tk.Button(dialog, text="Clear Input Selection", command=self.clear_input_selection)
        clear_input_button.pack(pady=10)

        clear_target_button = tk.Button(dialog, text="Clear Target Selection", command=self.clear_target_selection)
        clear_target_button.pack(pady=10)

        clear_both_button = tk.Button(dialog, text="Clear Both Selections", command=self.clear_both_selection)
        clear_both_button.pack(pady=10)

    def select_input_files(self):
        try:
            files = askopenfilenames(title="Select Input Files", filetypes=[("All files", "*.*")],
                                     initialdir=self.get_initial_directory())
            if files:
                for file in files:
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
                    self.target_items.append(folder)
                    print(f"'{os.path.basename(folder)}' folder added as target")
                self.last_accessed_path = os.path.dirname(folders[0])  # Update last accessed path
            self.update_rename_button_state()
        except Exception as e:
            print(f"Error selecting target folders: {e}")

    def show_selected_items(self):
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
        print("\n" * 60)  # Clear console output by printing new lines
        display_notice()

    def close_sub_dialogs(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()

    def update_rename_button_state(self):
        if len(self.input_items) == len(self.target_items) and self.input_items:
            self.rename_button.config(state=tk.NORMAL)
        else:
            self.rename_button.config(state=tk.DISABLED)

    def rename_items(self):
        if len(self.input_items) != len(self.target_items):
            print("The number of input and target items must be the same!")
            return

        for input_item in self.input_items:
            new_name = os.path.basename(input_item)
            if any(os.path.basename(target_item) == new_name for target_item in self.target_items):
                print(f"A file or folder named '{new_name}' already exists in the target directory!")
                return

        for input_item, target_item in zip(self.input_items, self.target_items):
            new_name = os.path.basename(input_item)
            target_dir = os.path.dirname(target_item)
            new_target_path = os.path.join(target_dir, new_name)

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
