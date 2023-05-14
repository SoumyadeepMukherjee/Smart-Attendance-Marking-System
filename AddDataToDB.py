import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://smart-attendance-system-c2a01-default-rtdb.firebaseio.com/"
})

ref=db.reference('Students')

data={
    "1":
        {
            "name":"Soumyadeep Mukherjee",
            "major":"IT",
            "starting_year":2019,
            "total_attendance":7,
            "grade": "O",
            "year":4,
            "last_attendance_time":"2023-01-10 12:30:00"
        },
    "2":
        {
            "name":"Sundar Pichai",
            "major":"Computer Science",
            "starting_year":2020,
            "total_attendance":7,
            "grade": "O",
            "year":3,
            "last_attendance_time":"2023-01-10 11:30:00"
        },
    "3":
        {
            "name":"Elon Musk",
            "major":"Physics",
            "starting_year":2021,
            "total_attendance":4,
            "grade": "E",
            "year":2,
            "last_attendance_time":"2023-01-10 11:30:00"
        },
    "4":
        {
            "name":"Sparsh Singh",
            "major":"IT",
            "starting_year":2019,
            "total_attendance":2,
            "grade": "A",
            "year":4,
            "last_attendance_time":"2023-01-10 11:30:00"
        },
    "5":
        {
            "name":"Tannistha Muhuri",
            "major":"IT",
            "starting_year":2019,
            "total_attendance":6,
            "grade": "E",
            "year":4,
            "last_attendance_time":"2023-01-10 11:30:00"
        }
}

for key,value in data.items():
    ref.child(key).set(value)
