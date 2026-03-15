import customtkinter as ctk
from tkinter import ttk
import psutil

def _addPID(master):
    from os import getpid  # noqa: F811
    ctk.CTkLabel(master, text=f"PID: {getpid()}").pack(side=ctk.TOP, anchor=ctk.NE, padx=5)


class ProcTree(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("Process")
        self.geometry("500x400")

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
        if self.Pid.get() != "":
            for item in self.tree.get_children():
                if self.tree.item(item, "text") == int(self.Pid.get()):
                    self.tree.selection_set(item)
                    self.tree.see(item)
                    break
        elif self.procName.get() != "":
            for item in self.tree.get_children():
                if str(self.tree.item(item, "values")[0]).lower() == self.procName.get().lower():
                    self.tree.selection_set(item)
                    self.tree.see(item)
                    break


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
                self.tree.insert("", ctk.END, text=p.info["pid"], values=(p.info["name"], p.info["status"]))
            except psutil.NoSuchProcess:
                pass

        next_index = index + chunk_size
        if next_index < len(self._procs):
            self.after(10, lambda: self._loadChunk(next_index))  # load next chunk after 10ms


if __name__ == "__main__":
    # all_pids = psutil.pids()
    # print(all_pids)
    ProcTree()