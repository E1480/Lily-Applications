import customtkinter as ctk

def _addPID(master):
    from os import getpid
    ctk.CTkLabel(master, text=f"PID: {getpid()}").pack(side=ctk.TOP, anchor=ctk.NE, padx=5)


root = ctk.CTk()
root.geometry("500x500")
root.title(__file__)

_addPID(root)

root.mainloop()

