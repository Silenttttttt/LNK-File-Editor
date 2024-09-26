import tkinter as tk
from tkinter import filedialog, messagebox
import pylnk3

class LnkEditorApp:
    def __init__(self, root):
        """
        Initialize the LnkEditorApp with the root window.
        """
        self.root = root
        self.root.title("LNK File Editor")

        self.lnk_file_path = None
        self.lnk_file = None

        self.create_widgets()

    def create_widgets(self):
        """
        Create and layout the widgets in the GUI.
        """
        # Label and entry for the LNK file path
        self.path_label = tk.Label(self.root, text="LNK File Path:")
        self.path_label.pack(pady=5)
        self.path_entry = tk.Entry(self.root, width=50)
        self.path_entry.pack(pady=5)
        
        # Button to browse for the LNK file
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_lnk_file)
        self.browse_button.pack(pady=5)

        # Button to load the LNK file
        self.load_button = tk.Button(self.root, text="Load .lnk File", command=self.load_lnk_file)
        self.load_button.pack(pady=10)

        # Label and entry for the target path
        self.target_path_label = tk.Label(self.root, text="Target Path:")
        self.target_path_label.pack(pady=5)
        self.target_path_entry = tk.Entry(self.root, width=50)
        self.target_path_entry.pack(pady=5)

        # Label and entry for the command line arguments
        self.arguments_label = tk.Label(self.root, text="Arguments:")
        self.arguments_label.pack(pady=5)
        self.arguments_entry = tk.Entry(self.root, width=50)
        self.arguments_entry.pack(pady=5)

        # Button to save the modified LNK file
        self.save_button = tk.Button(self.root, text="Save .lnk File", command=self.save_lnk_file)
        self.save_button.pack(pady=10)

    def browse_lnk_file(self):
        """
        Open a file dialog to select a .lnk file and update the path entry.
        """
        self.lnk_file_path = filedialog.askopenfilename(filetypes=[("LNK files", "*.lnk")])
        if self.lnk_file_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, self.lnk_file_path)

    def load_lnk_file(self):
        """
        Load the .lnk file specified in the path entry and populate the target path and arguments entries.
        """
        self.lnk_file_path = self.path_entry.get()
        if not self.lnk_file_path:
            messagebox.showerror("Error", "Please provide a valid .lnk file path.")
            return

        try:
            with open(self.lnk_file_path, 'rb') as f:
                self.lnk_file = pylnk3.parse(f)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load .lnk file: {e}")
            return

        # Populate the target path and arguments entries
        self.target_path_entry.delete(0, tk.END)
        self.target_path_entry.insert(0, self.lnk_file.link_info.local_base_path)

        self.arguments_entry.delete(0, tk.END)
        self.arguments_entry.insert(0, self.lnk_file.arguments)

    def save_lnk_file(self):
        """
        Save the modified .lnk file with the new target path and arguments.
        """
        if not self.lnk_file:
            messagebox.showerror("Error", "No .lnk file loaded.")
            return

        new_target_path = self.target_path_entry.get()
        new_arguments = self.arguments_entry.get()

        # Update the LNK file with the new values
        self.lnk_file.link_info.local_base_path = new_target_path
        self.lnk_file.arguments = new_arguments

        try:
            with open(self.lnk_file_path, 'wb') as f:
                self.lnk_file.save(f)
            messagebox.showinfo("Success", "LNK file saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save .lnk file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LnkEditorApp(root)
    root.mainloop()