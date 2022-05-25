import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector



class Student_Details:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x816+0+0")
        self.root.title("Student Details")
        self.root.configure(bg="light blue")

        title_lbl=Label(root,text="STUDENT DETAILS",font=("times new roman",40,"bold"),bg="orchid",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=50)


        #Variables

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        main_frame=Frame(root,bd=2 , bg="light blue")
        main_frame.place(x=30,y=50,width=1470,height=700)    

        # left label frame

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student details",bg="light blue",font=("times new roman", 14,"bold"))
        left_frame.place(x=10,y=10,width=730,height=710)


        left_img=Image.open("Images//student1.png")
        left_img=left_img.resize((720,145),Image.ANTIALIAS)
        self.lfimg=ImageTk.PhotoImage(left_img)

        f_lbl=Label(left_frame,image=self.lfimg)
        f_lbl.place(x=5,y=0,width=720,height=145)

        # Current subject information
        current_subj_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current subject :",font=("times new roman", 10,"bold"),bg="white")
        current_subj_frame.place(x=5,y=170,width=710,height=140)
       
        # Department

        dep_label=Label(current_subj_frame,text="Department ",font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_box=ttk.Combobox(current_subj_frame,textvariable=self.var_dep,state="readonly",font=("times new roman", 13, "bold"), width=20)
        dep_box["values"] = ("Select Department" , "Computer Science","IT","Civil","Mechanical","Chemical","Biotechnology","GPT","GT","Electrical","ECE")
        dep_box.current(0)       
        dep_box.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        
        # Course

        course_label=Label (current_subj_frame ,text="Course", font=("times new roman", 13, "bold"), bg="white") 
        course_label.grid(row=0, column=2, padx=10, sticky=W)
    
        course_combo=ttk.Combobox(current_subj_frame,textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly",width=20)
        course_combo["values"]=("Select Course", "FE", "SE","TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year

        year_label=Label (current_subj_frame, text="Year", font=("times new roman", 13, "bold"), bg="white") 
        year_label.grid(row=1, column=0, padx=10, sticky=W)
    
        year_combo=ttk.Combobox(current_subj_frame,textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly",width=20)
        year_combo["values"]=("Select Year", "2020-21","2021-22", "2022-23","2023-24") 
        year_combo.current(0)
        year_combo.grid (row=1,column=1, padx=2, pady=10, sticky=W)


        # Semester

        semester_label=Label(current_subj_frame, text="Semester", font=("times new roman",13, "bold"), bg="white")
        semester_label.grid(row=1,column=2, padx=10, sticky=W)

        semester_combo=ttk.Combobox (current_subj_frame,textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"]=("Select Semester", "Semester-1", "Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3, padx=2, pady=10, sticky=W)


        # Class Student information
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman", 10, "bold"),bg="white")
        class_student_frame.place(x=5,y=350,width=710,height=450)

        # Student id
        
        IDno_label=Label(class_student_frame, text="ID No:", font=("times new roman",13, "bold"),bg="white")
        IDno_label.grid(row=0,column=0, padx=10, sticky=W)
       
        IDno_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20)
        IDno_entry.grid(row=0,column=1, padx=10, sticky=W)


        # student name

        studentName_label=Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"),bg="white")
        studentName_label.grid (row=0,column=2, padx=10, pady=5, sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=15, font=("times new roman", 13, "bold")) 
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        # class division

        class_div_label=Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"),bg="white") 
        class_div_label.grid(row=1,column=0, padx=10, pady=5, sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div, font=("times new roman", 13, "bold"), state="readonly",width=15)
        div_combo["values"]=("A", "B", "C") 
        div_combo.current(0)
        div_combo.grid(row=1,column=1, padx=10, pady=5, sticky=W)


        # Roll No

        roll_no_label=Label(class_student_frame, text="Roll No: ", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid (row=1,column=2, padx=10, pady=5, sticky=W)
       
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll, width=15, font=("times new roman", 13, "bold")) 
        roll_no_entry.grid(row=1,column=3, padx=10, pady=5, sticky=W)


        # Gender

        gender_label=Label(class_student_frame, text="Gender:", font=("times new roman", 13, "bold"),bg="white")
        gender_label.grid (row=2, column=0, padx=10, pady=5, sticky=W)
    
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("times new roman", 13, "bold"), state="readonly",width=15)
        gender_combo["values"]=("Male", "Female", "Other") 
        gender_combo.current(0)
        gender_combo.grid (row=2,column=1, padx=2, pady=10, sticky=W)


        # Date of Birth

        dob_label=Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid (row=2, column=2, padx=10, pady=5, sticky=W)
    
        dob_entry=ttk.Entry(class_student_frame, textvariable=self.var_dob, width=15, font=("times new roman",13, "bold"))
        dob_entry.grid (row=2,column=3, padx=10, pady=5, sticky=W)


        # Email

        email_label=Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
    
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email, width=28, font=("times new roman", 13, "bold"))
        email_entry.grid (row=3,column=1, padx=10, pady=5, sticky=W)


        #Phone no

        phone_label=Label (class_student_frame, text="Phone No: ", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid (row=3, column=2, padx=10, pady=5,sticky=W)
    
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone, width=15, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        # Address

        address_label=Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=18, pady=5, sticky=W)


        # Teacher name

        teacher_label=Label(class_student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid (row=4, column=2,padx=10, pady=5, sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=15, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3,padx=10, pady=5, sticky=W)



        #Radio Buttons

        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo",value="Yes")
        radiobutton1.grid(row=6,column=0,padx=5,pady=5)

        
        radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo",value="No")
        radiobutton2.grid(row=6,column=1,padx=5,pady=5)



        #Button Frames

        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=220,width=700,height=60)

        save_button=Button(button_frame,text="Save",command=self.add_data,width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        update_button=Button(button_frame,text="Update",command=self.update_data,width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)

        delete_button=Button(button_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2)

        reset_button=Button(button_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)


        button_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        button_frame1.place(x=0,y=260,width=700,height=60)

        take_photo_button=Button(button_frame1,command=self.generate_dataset,text="Take Photo",width=60,font=("times new roman",15,"bold"),bg="blue",fg="white")
        take_photo_button.grid(row=0,column=0)



        # Right label frame

        Right_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",  font=("times new roman", 13, "bold"),bg="light blue")
        Right_frame.place(x=750, y=10,width=720, height=700)

        img_right=Image.open("Images//student2.jpg") 
        img_right=img_right.resize((720,200), Image. ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lb2=Label(Right_frame, image=self.photoimg_right)
        f_lb2.place(x=5, y=0,width=720, height=200)


        # =======Search System================#

        Search_frame=LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System", font=("times new roman" ,13,"bold"),bg="white")
        Search_frame.place(x=5, y=210, width=710,height=80)

        search_label=Label(Search_frame, text="Search By: ", font=("times new roman", 15, "bold"),bg="red", fg="white") 
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        #textvariable for combobox
        self.var_search_combo=StringVar()

        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_search_combo, font=("times new roman", 14, "bold"), state="readonly",width=20)
        search_combo["values"]=("Select", "Dep", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #textvariable for entrybox
        self.var_search=StringVar()

        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)


        search_button=Button(Search_frame,command=self.search_data,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=3)

        showall_button=Button(Search_frame,command=self.fetch_data,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_button.grid(row=0,column=4,padx=3)


        table_frame=Frame(Right_frame, bd=2, relief=RIDGE , bg="light blue")
        table_frame.place(x=5, y=300, width=710,height=364)


        #For scrolllbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year") 
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone") 
        self.student_table.heading("address", text="Address") 
        self.student_table.heading("teacher", text="Teacher") 
        self.student_table.heading("photo", text="PhotoStatus")
        self.student_table["show"]="headings"

     

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year", width=100) 
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=160)
        self.student_table.column("phone", width=100) 
        self.student_table.column("address", width=100) 
        self.student_table.column("teacher", width=100) 
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #***************Function declaration**************

    def add_data(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_semester.get()=="Select Semester" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" :
           messagebox.showerror("Error","!!!!!! All Fields are required !!!!!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Ishika12382",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            
                                                                                                                self.var_dep.get(),   
                                                                                                                self.var_course.get(),                                                                                                            
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()            
                conn.close()
                messagebox.showinfo("Success","Student details has been added succesfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #***************************Fetch data***************************

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Ishika12382",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    
    #***************************Update data****************************
    
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #*****************Update function***********

    def update_data(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","!!!!!! All Fields are required !!!!!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Ishika12382",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                           
                                                                                                                                                                                                                         self.var_dep.get(),
                                                                                                                                                                                                                         self.var_course.get(),
                                                                                                                                                                                                                         self.var_year.get(),
                                                                                                                                                                                                                         self.var_semester.get(),
                                                                                                                                                                                                                         self.var_std_name.get(),
                                                                                                                                                                                                                         self.var_div.get(),
                                                                                                                                                                                                                         self.var_roll.get(),
                                                                                                                                                                                                                         self.var_gender.get(),
                                                                                                                                                                                                                         self.var_dob.get(),
                                                                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                                                                         self.var_phone.get(),
                                                                                                                                                                                                                         self.var_address.get(),
                                                                                                                                                                                                                         self.var_teacher.get(),
                                                                                                                                                                                                                         self.var_radio1.get(),
                                                                                                                                                                                                                         self.var_std_id.get()
                                                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Student details successfully update completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error occurred",f"Due To:{str(es)}",parent=self.root)


    #****************Delete Function***************

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student details?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Ishika12382",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                            
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error occurred",f"Due To:{str(es)}",parent=self.root)


    #**************************Reset Data***********************

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #*************************Search Data************************

    def search_data(self):
        if self.var_search_combo.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Ishika12382",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_search_combo.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()

                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("",END,values=row)


                    conn.commit()
                conn.close()        
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    

        

    #******************************Generate dataset / Take photos *******************************

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department"or self.var_std_name.get()=="" or self.var_std_id.get()=="":
           messagebox.showerror("Error","!!!!!! All Fields are required !!!!!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Ishika12382",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                           
                                                                                                                                                                                                                         self.var_dep.get(),
                                                                                                                                                                                                                         self.var_course.get(),
                                                                                                                                                                                                                         self.var_year.get(),
                                                                                                                                                                                                                         self.var_semester.get(),
                                                                                                                                                                                                                         self.var_std_name.get(),
                                                                                                                                                                                                                         self.var_div.get(),
                                                                                                                                                                                                                         self.var_roll.get(),
                                                                                                                                                                                                                         self.var_gender.get(),
                                                                                                                                                                                                                         self.var_dob.get(),
                                                                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                                                                         self.var_phone.get(),
                                                                                                                                                                                                                         self.var_address.get(),
                                                                                                                                                                                                                         self.var_teacher.get(),
                                                                                                                                                                                                                         self.var_radio1.get(),
                                                                                                                                                                                                                         self.var_std_id.get()==id+1
                                                                                                                                                                                                                        ))                                                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #*************Haarcascade Classifier**************************

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # Used for object detection

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) # Scaling factor=1.3(by default)  Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cam=cv2.VideoCapture(0) # 0 will open primary camera
                img_id=0
                while True:
                    ret,face_frame=cam.read()  # Reading the video captures by camera frame by frame

                    if face_cropped(face_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(face_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) # Converting the image into grayscale as most of the the processing is done in gray scale format
                        file_name_path="ImagesData/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cam.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error occurred",f"Due To:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj=Student_Details(root)
    root.mainloop()        