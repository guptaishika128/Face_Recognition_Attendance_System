"""
Main Script
Start the GUI of the application and calls the required modules for necessary functionality

"""

from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student_Details
from train import Train
from face_recog import Face_Recognition
from Student_attendance import Student_Attendance
from about_developer import About_Developer
from help import Help
from time import strftime
from datetime import datetime
import os


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x816+0+0")
        self.root.title("Face Recognition")
        self.root.configure(bg="light blue")
       

        title_lbl=Label(root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",40,"bold"),bg="orchid",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=80)



        # To display current time 
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after (1000, time)

        lbl = Label(title_lbl, font=('times new roman',14, 'bold'), background='black', foreground ='orchid')
        lbl.place(x=5, y=10,width=120,height=50)
        time()


        
        #************Student details button************

        student_img=Image.open("Images//student.jpg")
        student_img=student_img.resize((220,220),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(student_img)

        b1=Button(root,image=self.img1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=150,width=220,height=220)

        b1_1=Button(root,text="Student Details",font=("arial",15,"bold"),bg="blue",fg="white",command=self.student_details,cursor="hand2")
        b1_1.place(x=200,y=350,width=220,height=40)



        #***************For Train Face button*****************

        train_img=Image.open("Images//a.jpg")
        train_img=train_img.resize((220,220),Image.ANTIALIAS)
        self.trainimg=ImageTk.PhotoImage(train_img)

        b1=Button(root,image=self.trainimg,command=self.train_data,cursor="hand2")
        b1.place(x=500,y=150,width=220,height=220)

        b1_1=Button(root,text="Train Image",font=("arial",15,"bold"),bg="blue",fg="white",command=self.train_data,cursor="hand2")
        b1_1.place(x=500,y=350,width=220,height=40)



        #****************Take Attendance/Face Recognize button***********

        detectface_img=Image.open("Images//facedetect.jpg")
        detectface_img=detectface_img.resize((220,220),Image.ANTIALIAS)
        self.dfimg=ImageTk.PhotoImage(detectface_img)

        b1=Button(root,image=self.dfimg,cursor="hand2",command=self.face_data)
        b1.place(x=800,y=150,width=220,height=220)

        b1_1=Button(root,text="Take Attendance",font=("arial",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.face_data)
        b1_1.place(x=800,y=350,width=220,height=40)



        #******************For Viewing Attendance Report button **************

        att_img=Image.open("Images//attendance.jpg")
        att_img=att_img.resize((220,220),Image.ANTIALIAS)
        self.attimg=ImageTk.PhotoImage(att_img)

        b1=Button(root,image=self.attimg,cursor="hand2",command=self.attendance_data)
        b1.place(x=1100,y=150,width=220,height=220)

        b1_1=Button(root,text="Attendance Report",font=("arial",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.attendance_data)
        b1_1.place(x=1100,y=350,width=220,height=40)



        #*******************For Photos button******************

        photo_img=Image.open("Images//photo.jpg")
        photo_img=photo_img.resize((220,220),Image.ANTIALIAS)
        self.picimg=ImageTk.PhotoImage(photo_img)

        b1=Button(root,image=self.picimg,cursor="hand2",command=self.open_image)
        b1.place(x=200,y=450,width=220,height=220)

        b1_1=Button(root,text="Photos",font=("arial",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.open_image)
        b1_1.place(x=200,y=650,width=220,height=40)



        #*******************For About Developer button**********

        about_img=Image.open("Images//about.jpg")
        about_img=about_img.resize((220,220),Image.ANTIALIAS)
        self.aboutimg=ImageTk.PhotoImage(about_img)

        b1=Button(root,image=self.aboutimg,command=self.about_developer_data,cursor="hand2")
        b1.place(x=500,y=450,width=220,height=220)

        b1_1=Button(root,text="About Developer",font=("arial",15,"bold"),bg="blue",fg="white",command=self.about_developer_data,cursor="hand2")
        b1_1.place(x=500,y=650,width=220,height=40)



        #*******************For Help button******************

        help_img=Image.open("Images//help.jpeg")
        help_img=help_img.resize((220,220),Image.ANTIALIAS)
        self.helpimg=ImageTk.PhotoImage(help_img)

        b1=Button(root,image=self.helpimg,cursor="hand2",command=self.help_data)
        b1.place(x=800,y=450,width=220,height=220)

        b1_1=Button(root,text="Help",font=("arial",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.help_data)
        b1_1.place(x=800,y=650,width=220,height=40)



        #********************For Exit button****************

        exit_img=Image.open("Images//exit.jpg")
        exit_img=exit_img.resize((220,220),Image.ANTIALIAS)
        self.exitimg=ImageTk.PhotoImage(exit_img)

        b1=Button(root,image=self.exitimg,cursor="hand2",command=self.exit_win)
        b1.place(x=1100,y=450,width=220,height=220)

        b1_1=Button(root,text="Exit",font=("arial",15,"bold"),bg="blue",fg="white",cursor="hand2",command=self.exit_win)
        b1_1.place(x=1100,y=650,width=220,height=40)



    def open_image(self):
        os.startfile("ImagesData")


    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Details(self.new_window)
       

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)   


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 


    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Attendance(self.new_window)


    def about_developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=About_Developer(self.new_window)


    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


    def exit_win(self):
        self.exit_win=tkinter.messagebox.askyesno("Exit Window","Are you sure you want to exit?",parent=self.root)
        if self.exit_win>0:
            self.root.destroy()
        else:
            return




if __name__ == "__main__":
    root = Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        