import tkinter as tk

root = tk.Tk()
root.title("My Window")

winWidth = 300
winHeight = 200

scrWidth = root.winfo_screenwidth()
scrHeight = root.winfo_screenheight()

centerX = int(scrWidth/2 - winWidth/2)
centerY = int(scrHeight/2 - winHeight/2)

#formatted templates "f" prefix before ''
root.geometry(f'{winWidth}x{winHeight}+{centerX}+{centerY}')
root.resizable(False, False)

root.mainloop()