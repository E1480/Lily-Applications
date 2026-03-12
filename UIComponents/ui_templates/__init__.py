import customtkinter as ctk
from .. import CURRENT  # noqa: F401

class Application(ctk.CTk):
    def __init__(self, geometry, title):
        super().__init__()
        # Set the appearance mode and color theme for the application
        ctk.set_appearance_mode(CURRENT.APPEARANCE_MODE)
        ctk.set_default_color_theme(CURRENT.COLOR_THEME)


        self.geometry(geometry)
        self.title(title)
    

    def mainloop(self, *args, **kwargs):
        return super().mainloop(*args, **kwargs)