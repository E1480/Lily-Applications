import customtkinter as ctk

class mainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

def createApp() -> ctk.CTk:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Lily Applications")
    app.geometry("400x300")

    return app

if __name__ == "__main__":
    root = createApp()

    mainFrame(root)

    root.mainloop()
    