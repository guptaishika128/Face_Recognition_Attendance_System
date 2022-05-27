import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog


mydata=[]
class Student_Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x816+0+0")
        self.root.title("Attendance Details")
        self.root.configure(bg="light blue")

        title_lbl=Label(root,text="ATTENDANCE REPORT",font=("times new roman",40,"bold"),bg="orchid",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=50)


        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()

        main_frame=Frame(root,bd=2,bg="light blue")
        main_frame.place(x=20,y=50,width=1480,height=630)    


        # left label frame

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("times new roman", 13, "bold"),bg="light blue")
        left_frame.place(x=10,y=50,width=720,height=560)   


        left_img=Image.open("Images//student-attendance-form.png")
        left_img=left_img.resize((720,150),Image.ANTIALIAS)
        self.lfimg=ImageTk.PhotoImage(left_img)

        f_lbl=Label(left_frame,image=self.lfimg)
        f_lbl.place(x=0,y=0,width=720,height=150)


        inside_left_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        inside_left_frame.place(x=0,y=135,width=720,height=400)

        # Attendance id

        IDno_label=Label(inside_left_frame, text="AttendanceId:",bg="white", font=("times new roman",13, "bold"))
        IDno_label.grid(row=0,column=0, padx=10, pady=10, sticky=W)
    
        IDno_entry=ttk.Entry(inside_left_frame,textvariable=self.var_attend_id,width=20,font=("times new roman",13, "bold"))
        IDno_entry.grid(row=0,column=1, padx=10, pady=10, sticky=W)

        #Roll No

        rollLabel=Label(inside_left_frame, text="Roll No:", bg="white", font=("comicsansns" ,11 ,"bold")) 
        rollLabel.grid(row=0,column=2, padx=4, pady=8)

        atten_roll=ttk.Entry(inside_left_frame,textvariable=self.var_attend_roll, width=22, font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=3, pady=8)

        #Name

        nameLabel=Label(inside_left_frame, text="Name:",bg="white", font="comicsansns 11 bold") 
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(inside_left_frame,width=22,textvariable=self.var_attend_name, font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1, pady=8)


        #Department

        depLabel=Label(inside_left_frame, text="Department:", bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(inside_left_frame,width=22,textvariable=self.var_attend_dep, font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3, pady=8)


        # Time


        timelabel=Label(inside_left_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        timelabel.grid(row=2,column=0)

        atten_time=ttk.Entry(inside_left_frame,textvariable=self.var_attend_time, width=22, font="comicsansns 11 bold") 
        atten_time.grid(row=2, column=1, pady=8)


        # Date

        dateLabel=Label(inside_left_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(inside_left_frame,textvariable=self.var_attend_date, width=22, font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3, pady=8)

        #attendance

        attendanceLabel=Label(inside_left_frame, text="Attendance Status", bg="white", font="comicsansns 11 bold") 
        attendanceLabel.grid(row=3, column=0)

        self.atten_status=ttk.Combobox(inside_left_frame,textvariable=self.var_attend_attendance, width=20, font="comicsansns 11 bold", state="readonly") 
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3,column=1, pady=8) 
        self.atten_status.current(0)


        #Button Frames

        button_frame=Frame(inside_left_frame,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=270,width=700,height=120)

        import_button=Button(button_frame,text="Import Attendance csv",command=self.importcsv,width=60,font=("times new roman",15,"bold"),bg="blue",fg="white")
        import_button.grid(row=0,column=0)

        export_button=Button(button_frame,text="Export Attendance csv",command=self.exportcsv,width=60,font=("times new roman",15,"bold"),bg="blue",fg="white")
        export_button.grid(row=1,column=0)

        reset_button=Button(button_frame,text="Reset",command=self.reset_data,width=60,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_button.grid(row=2,column=0)




        # Right label frame

        Right_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details",  font=("times new roman", 13, "bold"),bg="light blue")
        Right_frame.place(x=750, y=170,width=720, height=440) 


        table_frame=Frame(Right_frame,bd=2,relief=RIDGE , bg="white")
        table_frame.place(x=5,y=5,width=700,height=410)


        #For scrolllbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReport=ttk.Treeview(table_frame,column=("id","rollno","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReport.xview)
        scroll_y.config(command=self.AttendanceReport.yview)

        self.AttendanceReport.heading("id",text="Attendance ID")
        self.AttendanceReport.heading("rollno", text="Roll No")
        self.AttendanceReport.heading("name", text="Name") 
        self.AttendanceReport.heading ("department", text="Department")
        self.AttendanceReport.heading ("time", text="Time")
        self.AttendanceReport.heading("date", text="Date")
        self.AttendanceReport.heading("attendance", text="Attendance")

        self.AttendanceReport["show"]="headings"

        self.AttendanceReport.column("id",width=100)
        self.AttendanceReport.column("rollno", width=100)
        self.AttendanceReport.column("name", width=100) 
        self.AttendanceReport.column("department", width=110)
        self.AttendanceReport.column("time", width=100)
        self.AttendanceReport.column("date", width=100)
        self.AttendanceReport.column("attendance", width=100)

        self.AttendanceReport.pack(fill=BOTH,expand=1)

        self.AttendanceReport.bind("<ButtonRelease>",self.get_cursor)

     #**************Fetch data*********************


    def fetchData(self,rows):
        self.AttendanceReport.delete(*self.AttendanceReport.get_children())
        for i in rows:
            self.AttendanceReport.insert("",END,values=i)

   #*******Import csv************

    def importcsv(self):
        global mydata
        mydata.clear()
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(filename) as myfile:
            read_csv=csv.reader(myfile,delimiter=",")
            for i in read_csv:
                mydata.append(i)
            self.fetchData(mydata)    

    #**********Export csv**********

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data found to export",parent=self.root)
                return False
            filename=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)    
            with open(filename,mode="w",newline="") as myfile:
                write_csv=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    write_csv.writerow(i)
                messagebox.showinfo("Export Data","Your data has been exported to "+os.path.basename(filename)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)        


    def get_cursor(self,arg=""):
        cursor_row=self.AttendanceReport.focus()
        content=self.AttendanceReport.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])



    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")


    












if __name__ == "__main__":
    root = Tk()
    obj=Student_Attendance(root)
    root.mainloop()                