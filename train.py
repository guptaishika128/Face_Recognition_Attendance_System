import cv2
from platform import release
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x816+0+0")
        self.root.title("Train Image")


        title_lbl=Label(root,text="TRAIN IMAGE",font=("times new roman",40,"bold"),bg="orchid",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=50)

        img_1=Image.open("Images//train1.jpg")
        img_1=img_1.resize((1536,750),Image.ANTIALIAS)
        self.lfimg=ImageTk.PhotoImage(img_1)

        f_lbl=Label(root,image=self.lfimg)
        f_lbl.place(x=0,y=55,width=1536,height=750)


        b1_1=Button(root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="blue",fg="black")
        b1_1.place(x=550,y=600,width=470,height=60)



    def train_classifier(self):
        data_dir=("ImagesData")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') # Converting to gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13 
        ids=np.array(ids)

        #**************Train the classifier*************************

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Trainner.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!!!!!",parent=self.root)    




if __name__ == "__main__":
    root = Tk()
    obj=Train(root)
    root.mainloop()                