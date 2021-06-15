def h():
    import game1




#GUI
from tkinter import *
r = Tk()
r.title("Space Invaders")
r.geometry("800x600")
r.resizable(False,False)
l1 = Label(r,text="PLayer Name").grid(row=0,column=0)
t1 = Entry(r,width = 16).grid(row=0,column=1) 
b = Button(r,text="Submit",command = h,activebackground="blue").grid(row=2,column=2)
r.mainloop()