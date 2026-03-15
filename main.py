import logging
import customtkinter as ctk


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

Lhandler = logging.StreamHandler()
Lformat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
Lhandler.setFormatter(Lformat)
logger.addHandler(Lhandler)

def main():
    root = ctk.CTk()
    root.geometry("300x500")
    root.title("Lily Applications")

    rootFrame = ctk.CTkScrollableFrame(root)
    rootFrame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)
    

    ctk.CTkButton(rootFrame, text="Hello From Frame").pack(expand=True, fill=ctk.X, pady=5)


    root.mainloop()


if __name__ == "__main__":
    main()
