    
class GLOBALS:
    class BUTTONS:
        PRIMARY = "primary"
        SECONDARY = "secondary"
        SUCCESS = "success"
        DANGER = "danger"
        WARNING = "warning"
        INFO = "info"
        LIGHT = "light"
        DARK = "dark"
    
    class APPEARANCE_MODES:
        LIGHT = "light"
        DARK = "dark"
        SYSTEM = "system"
    
    class COLOR_THEMES:
        BLUE = "blue"
        DARK_BLUE = "dark-blue"
        GREEN = "green"
        DARK_GREEN = "dark-green"
        DARKER_GREEN = "darker-green"
        ORANGE = "orange"
        DARK_ORANGE = "dark-orange"
        DARKER_ORANGE = "darker-orange"
    
    class FONT_SIZES:
        SMALL = 10
        MEDIUM = 12
        LARGE = 14
        EXTRA_LARGE = 16

    class FONTS:
        ARIAL = "Arial"
        HELVETICA = "Helvetica"
        TIMES_NEW_ROMAN = "Times New Roman"
        COURIER_NEW = "Courier New"
        VERDANA = "Verdana"

class CURRENT:
    APPEARANCE_MODE = GLOBALS.APPEARANCE_MODES.SYSTEM
    COLOR_THEME = GLOBALS.COLOR_THEMES.BLUE
    FONT = (GLOBALS.FONTS.ARIAL, GLOBALS.FONT_SIZES.MEDIUM)