# Face_Recognition_Attendance_System

The objective of this project is to process live video-stream of students entering their classroom and generate the list of students attending the class.
The system is coded in Python using OpenCv , Tkinter and Numpy libraries.
The file in the directory are:

* main.py: This is the main  script of the project.
                    It implements the GUI of the project and calls functions from the modules package developed.

* haarcascade_frontalface_default.xml: This file is taken from the OpenCV library and contains trained configurations for detecting faces.



## Getting Started
### Prerequisites

The system needs Python 2.7 installed along with OpenCV libraries.
The face module of OpenCv is used for implementing Fisherfaces and Local Binary Pattern Histogram. The library is also used to implement Viola-Jones Face detection technique.

### Installing

The steps to install OpenCV with the extra module can be found [here](https://github.com/opencv/opencv_contrib).
The project also requires [Tkinter](https://docs.python.org/2/library/tkinter.html) and [Numpy](http://www.numpy.org/).


## Built With

* [OpenCV](http://docs.opencv.org/3.1.0/) - Implementation of Algorithms
* [Tkinter](https://docs.python.org/2/library/tkinter.html) - GUI Implementation
* [Numpy](http://www.numpy.org/) - Used to manage computaions.

**Following functionalities can be performed by the admin: <br>**
• Login <br>
• Register new employees to the system <br>
• Add employee photos to the training data set <br>
• Train the model <br>
• View attendance report of all employees. Attendance can be filtered by date or employee. <br>

**Following functionalities can be performed by the employee: <br>**
• Login <br>
• Mark his/her time-in and time-out by scanning their face <br>
• View attendance report of self <br>