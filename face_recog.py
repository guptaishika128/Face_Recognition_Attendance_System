import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import os
import numpy as np



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x816+0+0")
        self.root.title("Face Recognition")
        self.root.configure(bg="light blue")

        title_lbl=Label(root,text="FACE RECOGNITION ",font=("times new roman",40,"bold"),bg="orchid",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=50)

        
        img_11=Image.open("Images//FACERECOG1.jpg")
        img_11=img_11.resize((1200,800),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img_11)

        lb1=Label(self.root,image=self.img1)
        lb1.place(x=190,y=50,width=1200,height=800)

        b1_1=Button(root,text="Face Recognition",command=self.face_recogn,cursor="hand2",font=("times new roman",30,"bold"),bg="blue",fg="white")
        b1_1.place(x=390,y=720,width=800,height=50)

    #****************Attendance*****************************

    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    #*****************Face Recognition******************************
    def face_recogn(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coordi=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="Ishika12382",database="face_recognizer")
                my_cursor=conn.cursor()                

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence>75:
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(128, 0, 0),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(128, 0, 0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(128, 0, 0),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(128, 0, 0),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-7),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 

                coordi=[x,y,w,h]

            return coordi

        def recognize(img,clf,faceCascade):
            coordi=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("Trainner.xml")

        videocam=cv2.VideoCapture(0)

        while True:
            ret,img=videocam.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        videocam.release()
        cv2.destroyAllWindows()                      

                    

if __name__ == "__main__":
    root = Tk()
    obj=Face_Recognition(root)
    root.mainloop()              