import logging
from os import curdir, listdir, path
import customtkinter as ctk
from subprocess import Popen
from tkinter import filedialog as fd
import CTkMenuBar as MenuBar
from multiprocessing import Process

logger = logging.getLogger("Lily")
logger.setLevel(logging.DEBUG)

Lhandler = logging.StreamHandler()
Lformat = logging.Formatter('%(asctime)s :: <%(levelname)s> :: %(name)s :| %(message)s',datefmt="[%Y/%M/%D] %H:%M:%S")
Lhandler.setFormatter(Lformat)
logger.addHandler(Lhandler)


def _addPID(master):
    from os import getpid  # noqa: F811
    ctk.CTkLabel(master, text=f"PID: {getpid()}").pack(side=ctk.TOP, anchor=ctk.NE, padx=5)



class Lily(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.apps = []
        self._hasApps = False
        self.geometry("300x500")
        self.title("Lily Applications")
        self._initalizeMenuBar()
        self._addFileMenu()

        self.rootFrame = ctk.CTkScrollableFrame(self)
        self.rootFrame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        self.helpLbl = ctk.CTkLabel(self.rootFrame, text="""Welcome to Lily Laucher!
                        
        go to the top left
        and click on \"File\" to get started!
                        
        Select a folder 
        containing files with \".lily.py\"
        as the extension
    """)
        self.helpLbl.pack(expand=True, fill=ctk.X, pady=5)

        _addPID(self)

        self.mainloop()
    
    def _initalizeMenuBar(self):
        self.menu = MenuBar.CTkMenuBar(self)

    def _addFileMenu(self):
        fileMenu = self.menu.add_cascade("File")
        fileDropDownMenu = MenuBar.CustomDropdownMenu(fileMenu)
        fileDropDownMenu.add_option("Open", self._readFolder)
        fileDropDownMenu.add_separator()
        fileDropDownMenu.add_option("Exit", lambda: exit(0))

    def _readFolder(self):
        self._hasApps = False
        self.apps.clear()
        try:
            fdir = fd.askdirectory(initialdir=curdir)
            logger.log(logging.INFO, f"OPENED FOLDER: {fdir}")
            files = listdir(fdir)
            _loaded = 0
            _Rloaded = 0
            for file in files:
                if file.endswith(".lily.py"):
                    # logger.log(logging.INFO, f"FILE : {file}")
                    _loaded += 1
                    self.apps.append((f"{file}" , f"{path.join(fdir, file)}"))
                else:
                    _Rloaded += 1
            logger.log(logging.INFO, f"{" ":20}{"COUNT":2}")
            logger.log(logging.INFO, f"{"FILES LOADED":20} {len(files):2}")
            logger.log(logging.INFO, f"{"LILY FILES":20} {_loaded:2}")
            logger.log(logging.INFO, f"{"RANDOM FILES":20} {_Rloaded:2}")
            if(_loaded > 0):
                self.helpLbl.pack_forget()
                self._addButtons()
        except Exception as e:
            logger.log(logging.ERROR, f"{e}")
    
    def _addButtons(self):
        for i in self.apps:
            def _run(app=i):
                logger.log(logging.DEBUG, f"RUNNING : {app[0]}")
                proc = Popen(["uv", "run", f"{app[1]}"])
                logger.log(logging.DEBUG, f"PID : {proc.pid}")


            ctk.CTkButton(self.rootFrame,
                          text=f"{i[0].removesuffix(".lily.py")}",
                          command=_run).pack(expand=True, fill=ctk.X, pady=5)


if __name__ == "__main__":
    from procKiller import Prockiller
    lily = Process(target=Lily)
    procKill = Process(target=Prockiller)

    lily.start()
    procKill.start()

    lily.join()
    procKill.join()
    