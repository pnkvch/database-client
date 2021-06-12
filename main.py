from tkinter import Tk
from mainInterface import MainInterface


class Application:
    def __init__(self, master):
        self.root = master
        self.interface = MainInterface(self.root)
        self.interface.createMainInterface()


if __name__ == "__main__":
    root = Tk()
    ox = root.winfo_screenwidth() / 2
    oy = root.winfo_screenheight() / 2
    root.geometry(f'+{int(ox - 550)}+{int(oy - 400)}')
    apk = Application(root)
    root.mainloop()
