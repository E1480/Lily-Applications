import customtkinter as ctk
from tkinter import ttk, Menu

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("CustomTkinter Treeview Right-Click Menu")
        self.root.geometry("500x400")

        # Create Treeview
        self.tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.insert("", "end", values=("Alice", "30"))
        self.tree.insert("", "end", values=("Bob", "25"))
        self.tree.insert("", "end", values=("Charlie", "35"))
        self.tree.pack(pady=20, fill="both", expand=True)

        # Create context menu
        self.context_menu = Menu(root, tearoff=0)
        self.context_menu.add_command(label="Edit", command=self.edit_item)
        self.context_menu.add_command(label="Delete", command=self.delete_item)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Quit", command=root.quit)

        # Bind right-click event
        self.tree.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        # Get the row under the cursor
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
        else:
            self.context_menu.post(event.x_root, event.y_root)

    def edit_item(self):
        selected = self.tree.selection()
        if selected:
            print(f"Editing item: {self.tree.item(selected[0])['values']}")

    def delete_item(self):
        selected = self.tree.selection()
        if selected:
            self.tree.delete(selected[0])

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    root = ctk.CTk()
    app = App(root)
    root.mainloop()  