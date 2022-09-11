from tkinter import *
from tkinter import ttk
#start code

class todo: 
    def __init__(self, root):
        self.root = root
        self.root.title('To Do List')
        self.root.geometry('500x350+300+150')

        self.label = Label(self.root, text = "To Do List", font = 'ariel, 25 bold', width = 7, bd = 4, bg = 'black', fg = 'white')
        self.label.pack(side = 'top', fill = BOTH)

        self.label2 = Label(self.root, text = "add task", font = 'ariel, 16 bold', width = 7, bd = 4, bg = 'black', fg = 'white')
        self.label2.pack(side = 'top', fill = BOTH)
        self.label2.place(x = 60, y = 64)
        
        self.label3 = Label(self.root, text = "tasks", font = 'ariel, 16 bold', width = 7, bd = 4, bg = 'black', fg = 'white')
        self.label3.pack(side = 'top', fill = BOTH)
        self.label3.place(x = 350, y = 54)

        self.main_input = Listbox(self.root, height = 13, bd = 5, width = 30, font = 'ariel, 10 bold' )
        self.main_input.place(x = 260, y = 100)

        self.text = Text(self.root, bd = 5, height = 2, width = 30, font = 'ariel, 10 bold')
        self.text.place(x = 20, y = 120)


        def add():
            content = self.text.get(1.0, END)
            self.main_input.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, END)

        def delete():
            delete_ = self.main_input.curselection()
            look = self.main_input.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_input.delete(delete_)
        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_input.insert(END, ready)
            file.close()

        self.button = Button(self.root, text = "ADD", font = 'ariel, 16 bold', width = 10, bd = 5, bg= 'black', fg = 'white', command = add)
        self.button.place(x = 50, y = 180)

        self.button = Button(self.root, text ="DELETE", font = 'ariel, 16 bold', width = 10, bd = 5, bg= 'black', fg = 'white', command = delete)
        self.button.place(x = 50, y = 280)



def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
