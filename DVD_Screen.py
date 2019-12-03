import tkinter as tk
from sys import path
import random
path.append(".\src")

def controlsMenu():
    with open(r".\src\txt_files\controls.txt", "r") as CF:
        CTRLSRoot = tk.Tk()

        mainL = tk.Label(CTRLSRoot, text=CF.read(), font=("Consolas", 13))
        mainL.pack()

        CTRLSRoot.mainloop()

def infoMenu():
    with open(r".\src\txt_files/info.txt", "r") as IF:
        IFRoot = tk.Tk()

        mainL = tk.Label(IFRoot, text=IF.read(), font=("Consolas", 13))
        mainL.pack()

        IFRoot.mainloop()

class Menu:
    with open("DEFAULTS.txt", "r") as RF:
        text = (RF.read()).split(" ")
        winWidth, winHeight = text[1], text[2]
    def __init__(self):

        self.root = tk.Tk()

        self.root.configure(background="#ffffff")

        self.root.title(random.choice(["DVD Screen", "Main Menu", "Cool Title Here", "I'm Surprised You Read This", "New And Improved"]))
        self.root.iconbitmap(r".\src\ico_files\Main_Menu_ICO.ico")
        
        self.winHeightE = tk.Entry()
        self.winHeightE.insert(0, Menu.winHeight)
        
        self.winWidthE = tk.Entry()
        self.winWidthE.insert(0, Menu.winWidth)

        self.picHeightE = tk.Entry()
        self.picHeightE.insert(0, 43)

        self.picWidthE = tk.Entry()
        self.picWidthE.insert(0, 97)

        self.root.bind("<F10>", lambda x: self.done("secret"))

    def done(self, version): #LAUNCH
        Menu.winHeight, Menu.winWidth = int(self.winHeightE.get()), int(self.winWidthE.get())

        picWidth, picHeight = int(self.picWidthE.get()), int(self.picHeightE.get())

        self.root.destroy()

        print("Loading...")
        if version == "main":
            from Main import mainInit
            print("Loading... 50%")
            mainInit(Menu.winWidth, Menu.winHeight, picHeight, picWidth)

        elif version == "featureless":
            from Featureless import main
            print("Loading... 50%")
            main(Menu.winWidth, Menu.winHeight, picHeight, picWidth)

        elif version == "secret":
            from Secret import main as m
            m(random.randint(15, 25), picHeight, picWidth, Menu.winWidth, Menu.winHeight)

    def mainMenu(self):

        tk.Label(text="Window height", font=("MS Reference Sans Serif", 15), bg="#ffffff").grid(column=1, row=1)
        self.winHeightE.grid(column=1, row=2)

        tk.Label(text="Window width", font=("MS Reference Sans Serif", 15), bg="#ffffff").grid(column=1, row=3)
        self.winWidthE.grid(column=1, row=4)

        tk.Label(text="picture width\n(recommended 97)", font=("MS Reference Sans Serif", 10), bg="#ffffff").grid(column=2, row=1)
        self.picWidthE.grid(column=2, row=2)

        tk.Label(text="picture height\n(recommended 43)", font=("MS Reference Sans Serif", 10), bg="#ffffff").grid(column=2, row=3)
        self.picHeightE.grid(column=2, row=4)

        tk.Button(self.root, command=lambda: self.done("main"), text="run main version", font=("arial", 15), bg="#1cdb15").grid(column=3, row=6)
        tk.Button(self.root, text="run featureless version", font=("arial", 15), command=lambda: self.done("featureless"), bg="#1cdb15").grid(column=1, row=6)

        tk.Button(text="Controls", font=("MS Reference Sans Serif", 12), command=lambda: controlsMenu(), bg="#e324ea").grid(column=3, row=1)
        tk.Button(text="Info", font=("MS Reference Sans Serif", 12), command=lambda: infoMenu(), bg="#e324ea").grid(column=3, row=3)

        self.root.update_idletasks()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        size = tuple(int(_) for _ in self.root.geometry().split("+")[0].split("x"))
        x, y = w / 2 - size[0] / 2, h / 2 - size[1] / 2
        self.root.geometry("%dx%d+%d+%d" %(size + (x, y)))

        self.root.mainloop()
if __name__ == '__main__':
    Menu().mainMenu()