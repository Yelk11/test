from tkinter import Tk, Label, Button

class MyFrame:
    def __init__(self, master):
        self.master = master
        master.title("Asidro")

        

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_frame = MyFrame(root)
root.mainloop()
