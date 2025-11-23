# Detailed Documentation on API

`/api/v1/teacher/student_list`

### Sample Input

     {
      "department": "Computer Science and Engineering",
      "semester": 1,
      "section": "B"
     }


### Sample Output
    {
        "message": "Successfully loaded the list of students",
        "students": students,
        "session_id": session_id_current  
    }

#### Note
here students is a list of student



`/api/v1/auth/user_registeration`

### Sample input
    { "user_name": "Boby", 
      "email": "boby@gmail.com", 
      "role": "teacher", 
      "password": "boby123", 
      "register_number": "string", 
      "employee_id": "EMP1007" }

### Output
    { "message": "STUDENT data created succesfully"}


`/api/v1/auth/login`

### Sample data
    {
      "user_name": "Aju",
      "password": "aju123"
    }

### Output
    {
        "message": "User Aju has successfully logged in"
    }
