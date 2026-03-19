import customtkinter as ctk
import psutil
from datetime import datetime
if __name__ == "__main__":
    from info import _addCredits
else:
    from .info import _addCredits

def _addPID(master):
    from os import getpid  # noqa: F811
    ctk.CTkLabel(master, text=f"PID: {getpid()}").pack(side=ctk.TOP, anchor=ctk.NE, padx=5)


class Prockiller(ctk.CTk):
    def __init__(self, fg_color=None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self.proc = None
        self.geometry("500x350")
        self.title("Process Killer")
        _addCredits(self)

        self.actionFrame = ctk.CTkFrame(self)
        self.actionFrame.pack()

        # sub-frame to hold everything on one line
        rowFrame = ctk.CTkFrame(self.actionFrame)
        rowFrame.pack(anchor=ctk.NW, padx=5, pady=6)

        ctk.CTkLabel(rowFrame, text="Enter PID:").pack(side=ctk.LEFT, padx=5)
        self.entry = ctk.CTkEntry(rowFrame)
        self.entry.pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(rowFrame, text="Kill", command=self._kill).pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(rowFrame, text="Find", command=self._findPID).pack(side=ctk.LEFT, padx=5)

        self.textFrame = ctk.CTkScrollableFrame(self, label_text="Console")
        self.textFrame.pack(fill=ctk.BOTH, expand=True, padx=5, pady=6)



        _addPID(self)

        self.mainloop()


    def _findPID(self):
        if self.entry.get() == "":
            self._message("Please Enter PID...")
        else:
            pid = int(self.entry.get())
            try:
                self.proc = psutil.Process(pid)
                self._message(f"Found Process with PID {pid}")
                self._message(self.proc.name())
            except psutil.NoSuchProcess:
                self._message(f"No Process with PID {pid}")

    def _kill(self):
        if self.entry.get() == "":
            self._message("Please Enter PID...")
        else:
            pid = int(self.entry.get())
            try:
                self.proc = psutil.Process(pid)
                self.proc.kill()
                self._message(f"Killed Process with PID {pid}")
            except psutil.NoSuchProcess:
                self._message(f"No Process with PID {pid}")

    def _message(self, message):
        log = datetime.now().strftime("%Y/%m/%d | %H:%M.%S")
        ctk.CTkLabel(self.textFrame, text=f"[{log}]  {message}", anchor=ctk.W, height=10).pack(fill=ctk.X, expand=True, padx=1, pady=1)


if __name__ == "__main__":
    Prockiller()