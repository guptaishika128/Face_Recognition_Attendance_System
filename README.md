# Face_Recognition_Attendance_System

The objective of this project is to process live video-stream of students entering their classroom and generate the list of students attending the class. The system is coded in Python using OpenCv , Tkinter and Numpy libraries.
This project has been developed as a part of the Microsoft Engage 2022 program.


### Installation

## Python

- Download Python from https://www.python.org/downloads/

## MySQL

- Download MySQL from https://dev.mysql.com/downloads/installer/


## Demo

**First you need to connect to database.** 
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

**


  





## Built With

* [OpenCV](http://docs.opencv.org/3.1.0/) - Implementation of Algorithms
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - GUI Implementation
* [MySQL]

**Following functionalities can be performed: <br>**
• Login <br>
• New User Account can also be created. <br>
• If forgotten the login credentials password can be changed <br>
• Register new students to the system. Students can be filtered by Name or Department<br>
• Take photo sample of them <br>
• Train the model <br>
• Take attendance by scanning face <br>
• View attendance report of all students by importing csv. Also attendance can be exported too. <br>

