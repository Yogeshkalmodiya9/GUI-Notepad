
# im yogesh kalmodiya 
from tkinter import *

from tkinter.messagebox import showinfo

from tkinter.filedialog import askopenfilename,asksaveasfilename

import os

def newFile():
    global File
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
def OpenFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "."),("Text Documents", "*.txt")])
    if file=="":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close ()

def SaveFile():
    global file 
    
    if file == None:
        file = asksaveasfilename(initialfile= 'Untitled.txt',defaultextension=".txt",
                                 filetypes=[("All Files", "."),("Text Documents","*.txt")])
        if file =="":
            file= None

        else:
            #save us a new file 
            f= open(file, "w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad" )

    else:
         #Save the File
        f= open(file, "w")
        f.write(TextArea.get(1.0,END))
        f.close()


    
    


def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad", "Notepad create by Yogesh Kalmodiya")

if __name__ == '__main__':
    #basic  tkinter  setup

    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("") 
    root.geometry("388x444")

    # text area

    TextArea = Text(root, font="lucida 13")
    file = None

    TextArea.pack(expand=True,fill=BOTH)

    #lets create a Number 
    MenuBar =  Menu(root)

    #Starts File Menu 
    FileMenu = Menu(MenuBar, tearoff=0 )
    # to open new file 
    FileMenu.add_command (label="New", command=newFile)

    #to Open Alredy File 
    FileMenu.add_command(label="Open",command= OpenFile)

    #to Save the Current File 
    FileMenu.add_command(label="Save",command= SaveFile)
    FileMenu.add_separator()
    
    MenuBar.add_cascade(label= "File",menu= FileMenu)
    #End  File Menu 
    
    #ScrolBar in text area

    ScrollBar =  Scrollbar(TextArea)
    ScrollBar.pack(side=RIGHT,fill=Y)
    ScrollBar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand= ScrollBar.set)

    #Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #ti give a feature of cut 
    EditMenu.add_command(label="Copy",command=copy)

    EditMenu.add_command(label="Cut",command=cut)
    
    EditMenu.add_command(label="paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu= EditMenu)
    #Edit Menu Ends

    #Help Menu starts
    HelpMenu =  Menu(MenuBar,tearoff=0 )
    HelpMenu.add_command(label= "About Notepaad",command= about)
    MenuBar.add_cascade(label="Help",menu= HelpMenu)
    #Help Menu End

    root.config(menu=MenuBar)

    
root.mainloop()
