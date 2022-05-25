import cv2
from platform import release
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x816+0+0")
        self.root.title("Help")


        title_lbl=Label(root,text="HELP",font=("times new roman",40,"bold"),bg="orchid",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=50)

        img_1=Image.open("Images//help1.jpeg")
        img_1=img_1.resize((1536,750),Image.ANTIALIAS)
        self.lfimg=ImageTk.PhotoImage(img_1)

        f_lbl=Label(root,image=self.lfimg)
        f_lbl.place(x=0,y=55,width=1536,height=750)


        dev_lbl=Label(root,text="Email: guptaishika992@gmail.com",font=("times new roman",35,"bold"),bg="white",fg="blue")
        dev_lbl.place(x=0,y=380,width=1536,height=60)




if __name__ == "__main__":
    root = Tk()
    obj=Help(root)
    root.mainloop()            