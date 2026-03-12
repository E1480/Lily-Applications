from UIComponents.ui_lib import *  # noqa: F403
from UIComponents.ui_templates import Application  # noqa: F403

if __name__ == "__main__":
    app = Application(geometry="400x240", title="Lily")
    
    
    UIButton(app, text="Hello World").pack(pady=20)
    UILabel(app, text="Welcome to Lily!", font=(CURRENT.FONT[0], CURRENT.FONT[1])).pack(pady=20)  # noqa: F405

    app.mainloop()