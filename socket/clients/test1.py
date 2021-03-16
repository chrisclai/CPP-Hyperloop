import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.label_var = tk.IntVar()
        label = tk.Label(self, textvariable=self.label_var) # Assigned that  variable to the label
        label.pack()

        button = tk.Button(self, width=30, height=5,
            text = "Click Me!!",
            relief="groove", command=self.add_var)
        button.pack()

    def add_var(self):
        self.label_var.set(self.label_var.get() + 1)

root = tk.Tk()
root.title("Game")
root.resizable()
game = Game(root)
game.pack()
root.mainloop()