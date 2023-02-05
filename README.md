# Smart-Attendance-Marking-System

## Problem Statement :

Develop a Smart Attendance Marking System (SAMS) that can be used by colleges,schools and various organizations to facilitate the easy maintenance of the daily attendance records of students or employees.

## Objective :

* To eliminate the tedious conventional method of manual attendance by calling out names of students by replacing it with a system which automates the process, thereby reducing the human errors.
* Facilitates the easy attendance management of students using Face Detection which is one of the most modern technologies.
* Provides a robust and stable attendance system which reduces the flaws of our existing system.

## Libraries used :

```
cmake
dlib
opencv-python
face_recognition
cvzone
numpy
pickle
firebase
```

## Steps involved so far :

* Importing the required libraries.
* Setting up the webcam and importing the required graphics.
* Creating the encoding generator.
* Implementing face recognition algorithms to show whether faces are correctly detected and matched or not.
* Setting up the database, here Firebase.
* Adding data to the database.
* Adding the images to the database.
* Updating the Real-time Database accordingly.

## Demo of the System :

### Database before starting the System -

[![1.png](https://i.postimg.cc/sX8dJXdq/1.png)](https://postimg.cc/G8k5Lbpx)

### Face Recognition & retrieving and displaying student's data from the Database -

[![2.png](https://i.postimg.cc/X7shKqf8/2.png)](https://postimg.cc/fJ0BDwgt)

### Dynamically updating the Database as the student is marked -

[![3.png](https://i.postimg.cc/JzJNrdzk/3.png)](https://postimg.cc/mPLzVjML)

### Showing that the student is marked -

[![4.png](https://i.postimg.cc/Sst27WK4/4.png)](https://postimg.cc/TLg3T5mN)

### Displaying that the student is already marked after a specific interval of time -

[![5.png](https://i.postimg.cc/J724Tr51/5.png)](https://postimg.cc/MX1SH8L4)

