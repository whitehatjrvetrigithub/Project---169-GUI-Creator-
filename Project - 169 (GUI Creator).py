from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Classes")
root.geometry("900x600")

gui_elements = ["Label", "Button", "Combo Box", "Radio Button", "Entry Box"]

dropdown = ttk.Combobox(root, state = "readonly", values = gui_elements)
dropdown.pack()

class createElements:
    
    def __init__(self):
        print("This is Create Elements Class")
        
    def createLbl(self):
        lbl = Label(root, text = "Label")
        lbl.pack()
        
    def createBtn(self):
        btn = Button(root, text = "Button", command = self.message)
        btn.pack(padx = 20, pady = 10)
        
    def createCB(self):
        val = [1, 2, 3, 4, 5]
        
        cb = ttk.Combobox(root, state = "readonly", values = val)
        cb.pack()
        
    def createRB(self):
        var = IntVar()
        
        rb = Radiobutton(root, text = "Radio Button", variable = var, value = 1)
        rb.pack()
        
    def createEB(self):
        eb = Entry(root)
        eb.pack()
        
    def choose(self):
        global dropdown
        
        element = dropdown.get()
        
        if(element == "Label"):
            self.createLbl()
            
        elif(element == "Button"):
            self.createBtn()
            
        elif(element == "Combo Box"):
            self.createCB()
            
        elif(element == "Radio Button"):
            self.createRB()
            
        elif(element == "Entry Box"):
            self.createEB()
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the Button using Class.")
        
obj = createElements()

main_btn = Button(root, text = "Create Element", command = obj.choose)
main_btn.pack(padx = 20, pady = 10)

root.mainloop()