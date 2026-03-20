from typing import Any
import customtkinter as ctk
from PIL import Image, ImageDraw
import webbrowser

class Credits(ctk.CTkToplevel):

    """You don't need to know what this is
    I mean just know that this is a CTkTopLevel that's it lmao
     and if you have time you can read if you want.
    """

    def __init__(self, *args, fg_color=None, image_path="src/img/349187009_644874610828926_2501659095251803168_n.jpg", **kwargs):

        super().__init__(*args, fg_color=fg_color, **kwargs)

        self.title("Credits")
        self.geometry("500x500")
        self.image_path = image_path

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        ctk.CTkLabel(self.frame, text="Credits:").pack()

        circular = self._makeCircle(self.image_path, 230)
        self.pfp = ctk.CTkImage(circular, size=(230, 230))
        self.lb = ctk.CTkLabel(self.frame, image=self.pfp, text="")
        self.lb.pack()

        ctk.CTkLabel(self.frame, text="Program by: E1480").pack()

        self.lif = ctk.CTkFrame(self.frame, bg_color="#2b2b2b")
        self.lif.pack()
        gl = ctk.CTkLabel(self.lif, text="Github: ", bg_color="#2b2b2b")
        gl.pack(side=ctk.LEFT)
        link = ctk.CTkLabel(self.lif, text="https://github.com/E1480", text_color="#1a9fff", cursor="hand2", font=ctk.CTkFont(size=13, underline=True), bg_color="#2b2b2b")
        link.pack(side=ctk.LEFT)
        link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/E1480"))

    def _makeCircle(self, path, size):
        img = Image.open(path).resize((size, size))
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        img.putalpha(mask)
        return img


def _addCredits(master: Any):
    
    def _run():
        Credits(master)

    import CTkMenuBar as MenuBar
    menu = MenuBar.CTkMenuBar(master)
    infoMenu = menu.add_cascade("info")
    infoMenuDrop = MenuBar.CustomDropdownMenu(infoMenu)
    infoMenuDrop.add_option("Credits", _run)

def __wrapper__(**kwargs):
    required = {'master', 'menu'}
    
    if not required.issubset(kwargs):
        raise ValueError("Missing required fields")
    
    import CTkMenuBar as MenuBar
    def _addCreditsDropDown(master: Any, menu: MenuBar):
        
        def _run():
            Credits(master)
        
        infoMenu = menu.add_cascade("info")
        infoMenuDrop = MenuBar.CustomDropdownMenu(infoMenu)
        infoMenuDrop.add_option("Credits", _run)
    
    _addCreditsDropDown(kwargs.get("master"), kwargs.get("menu"))
