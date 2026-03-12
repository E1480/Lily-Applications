import customtkinter as ctk
from customtkinter import CTkButton, CTkEntry, CTkLabel, CTkFrame
from .. import CURRENT, GLOBALS  # noqa: F401
import logging

ctk.FontManager.load_font("UIComponents/Fonts/Sonia.otf")
# ctk.FontManager.load_font("UIComponents/Fonts/WARFIELD-Bold.ttf")
ctk.FontManager.load_font("UIComponents/Fonts/WARFIELD-Regular.ttf")

logging.basicConfig(level=logging.DEBUG)

CURRENT.FONT += ("SONIA", CURRENT.FONT[1])
CURRENT.FONT += ("WARFIELD", CURRENT.FONT[1])
print(CURRENT.FONT)

class UIButton(CTkButton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=(CURRENT.FONT[0], CURRENT.FONT[1]))

class UILabel(CTkLabel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=("WARFIELD", GLOBALS.FONT_SIZES.EXTRA_LARGE * 5))

class UIEntry(CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=(CURRENT.FONT[0], CURRENT.FONT[1]))

class UIFrame(CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

