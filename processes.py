import customtkinter as ctk
from tkinter import ttk
import psutil
import CTkMenuBar as MenuBar
from dataclasses import dataclass
from fuzzysearch import find_near_matches

def _addPID(master):
    from os import getpid  # noqa: F811
    ctk.CTkLabel(master, text=f"PID: {getpid()}").pack(side=ctk.TOP, anchor=ctk.NE, padx=5)

@dataclass
class PROCESSES:
    PID : int
    NAME : str

class ProcTree(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.processes : list[PROCESSES] = []
        self._procs : list = []

        self.title("Process")
        self.geometry("500x400")
        # self._menu()

        self.processTree = ctk.CTkFrame(self)
        self.processTree.pack(fill=ctk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self.processTree)
        scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

        self.tree = ttk.Treeview(self.processTree, columns=("name", "status"), yscrollcommand=scrollbar.set)
        self.tree.pack(fill=ctk.BOTH, expand=True, padx=5, pady=4)

        scrollbar.config(command=self.tree.yview)
            
        self.processTree.pack(fill=ctk.BOTH)

        self._addTree()

        self._addActionFrame()

        _addPID(self)
        self.mainloop()
    
    def _menu(self):
        menubar = MenuBar.CTkMenuBar(self)

        sort_menu = menubar.add_cascade("Sort")
        sort_menu_dropDown = MenuBar.CustomDropdownMenu(sort_menu)
        sort_menu_dropDown.add_option("Name", self._sort())
        sort_menu_dropDown.add_option("PID", lambda: print("PID"))

    def _sort(self):
        self._procs = sorted(self._procs)

    def _addActionFrame(self):
        self.actionFrame = ctk.CTkFrame(self)
        self.actionFrame.pack(fill=ctk.BOTH)
        padX = 10

        row1 = ctk.CTkFrame(self.actionFrame)
        row1.pack(fill=ctk.X, padx=5, pady=5)

        ctk.CTkLabel(row1, text=f"{"PID":30}").pack(side=ctk.LEFT, padx=padX)
        self.Pid = ctk.CTkEntry(row1)
        self.Pid.pack(side=ctk.LEFT, padx=padX, expand=True, fill=ctk.X)

        row2 = ctk.CTkFrame(self.actionFrame)
        row2.pack(fill=ctk.X, padx=5, pady=5)

        ctk.CTkLabel(row2, text=f"{"Proc Name":22}").pack(side=ctk.LEFT, padx=padX)
        self.procName = ctk.CTkEntry(row2)
        self.procName.pack(side=ctk.LEFT, padx=padX, expand=True, fill=ctk.X)

        ctk.CTkButton(self.actionFrame, text="Search", command=self._search).pack(pady=5)

    def _search(self):
        query = self.procName.get()
        results = []
        try:
            for p in self.processes:
                if find_near_matches(query, p.NAME, max_l_dist=1):
                    results.append(p)
        except Exception as e:  # noqa: F841
            pass

        if self.Pid.get() != "":
            matched_pids = {p.PID for p in self.processes if str(p.PID) == self.Pid.get()}
            matched_items = []

            for item in self.tree.get_children():
                if self.tree.item(item, "text") in matched_pids:
                    matched_items.append(item)

            if matched_items:
                self.tree.selection_set(matched_items)
                self.tree.see(matched_items[0])

        elif self.procName.get() != "":
            matched_names = {p.NAME for p in results}
            matched_items = []

            for item in self.tree.get_children():
                if self.tree.item(item, "values")[0] in matched_names:
                    matched_items.append(item)

            if matched_items:
                self.tree.selection_set(matched_items)
                self.tree.see(matched_items[0])

    def _addTree(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
            background="#2b2b2b",
            foreground="white",
            fieldbackground="#2b2b2b",
            rowheight=25,
            font=("Arial", 15)
        )
        style.configure("Treeview.Heading",
            background="#1f1f1f",
            foreground="white",
            font=("Arial", 15, "bold")
        )
        style.map("Treeview",
            background=[("selected", "#144870")],
            foreground=[("selected", "white")]
        )

        self.tree.tag_configure("odd", background="#2b2b2b")
        self.tree.tag_configure("even", background="#1f1f1f")

        self.tree.heading("#0", text="PID")
        self.tree.heading("name", text="Name")
        self.tree.heading("status", text="Status")
        
        self.tree.column("#0", width=100)
        self.tree.column("name", width=300)
        self.tree.column("status", width=100)

        self._procs = list(psutil.process_iter(["pid", "name", "status"]))
        self._loadChunk(0, 5)

        
    def _loadChunk(self, index, chunk_size=10):
        for p in self._procs[index:index + chunk_size]:
            try:
                self.processes.append(PROCESSES(p.info["pid"],p.info["name"]))
                self.tree.insert("", ctk.END, text=p.info["pid"], values=(p.info["name"], p.info["status"]))
            except psutil.NoSuchProcess:
                pass

        next_index = index + chunk_size
        if next_index < len(self._procs):
            self.after(10, lambda: self._loadChunk(next_index))  # load next chunk after 10ms

if __name__ == "__main__":
    app = ProcTree()
