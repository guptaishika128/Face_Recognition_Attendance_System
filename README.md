# Face_Recognition_Attendance_System

The objective of this project is to process live video-stream of students entering their classroom and generate the list of students attending the class. The system is coded in Python using OpenCv , Tkinter and MySQL.
This project has been developed as a part of the Microsoft Engage 2022 program.


### Installation

## Python

- Download Python from https://www.python.org/downloads/

## MySQL

- Download MySQL from https://dev.mysql.com/downloads/installer/


## Required steps

- Clone the repo:
```$ git clone https://github.com/guptaishika128/Face_Recognition_Attendance_System.git```

**Then you need to connect to database.** 
- To do that install MySQL with **username = root** and **password = Ishika12382** and port 3306 (By default)

- Now open MySQL Workbench and click on default connection
![Image](/Screenshots/MySQL.png)

- Enter password stated above in the window
![Image](/Screenshots/mysql1.png)

- Now create two schemas one with name **face_recognizer** 
![Image](/Screenshots/schema1.png)

- Other schema with name **mydata**
![Image](/Screenshots/schema2.png)

- Now as shown below click on Data Import
![Image](/Screenshots/DataImport.png)

- Clicking on Import from Dump Project Folder find the location where you cloned this project under that click on **Database** folder 
![Image](/Screenshots/findingdatabasefolder.png)

- You will see two files select both and click on Start Import
![Image](/Screenshots/import.png)

- **You have connected**. Refreshing you will be able to see student and register sql files under schemas
![Image](/Screenshots/Connected.png)

-Now run **login.py** 


## ⚙️ HOW THE SYSTEM WORKS?

This system works accordingly with a series of step explained below:

1. **LOGIN PAGE**:
<br>
First the admin will login using either default credentials **username=user@123** and **password=user@123** or can create a new account.

![Image](/Screenshots/Login page.png)

2. After entering right credentials welcome message appears.

![Image](/Screenshots/Welcome message appears.png)

3. Now the main page of face recognition attendance system appears

![Image](/Screenshots/Face recognition main page.png)

4. First Clicking on **Student Details** opens the page to register students and see their details. Students must have unique ID 

![Image](/Screenshots/Registering students.png)

5. After saving details click on Take Image option to capture student's face . 100 samples will be taken.

![Image](/Screenshots/Capturingimage.png)

6. Next on the main page click on **Train Image** after that cick on Train Data to train samples for detection and recognition.

![Image](/Screenshots/Training data.png)

7. Now on the main page click on **Take Attendance** after that click on the button to recognize face 

![Image](/Screenshots/Taking Attendance.png)

8. Simustenously, a csv file **attendance.csv'** will be updated with the ID,Roll No, Name of the student ,Department, Date and Time at which his/her face was recognized.

![Image](/Screenshots/Attendance Saved.png)

9. On the main page click on **Attendance Report** and then import attendance.csv to view attendance report of students. Attendance can also be exported .

![Image](/Screenshots/Importing attendance.png)

<br>


## Built With

* [OpenCV](http://docs.opencv.org/3.1.0/) - Implementation of Algorithms
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - GUI Implementation
* [MySQL] - Database
* [HAAR-CASCADE CLASSIFIER](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
* [LocalBinaryPatternHistogram (LBPH) recognizer](https://docs.opencv.org/master/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html)
* [PIL](https://pillow.readthedocs.io/en/stable/)


**Following functionalities can be performed: <br>**
• Login <br>
• New User Account can also be created. <br>
• If forgotten the login credentials password can be changed <br>
• Register new students to the system. Students can be filtered by Name or Department<br>
• Take photo sample of them <br>
• Train the model <br>
• Take attendance by scanning face <br>
• View attendance report of all students by importing csv. Also attendance can be exported too. <br>

