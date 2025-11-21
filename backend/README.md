installed
alembic


Report on bugs:

[SQL: SELECT periods.period_id AS periods_period_id, periods.period_number AS periods_period_number, periods.start_time AS periods_start_time, periods.end_time AS periods_end_time
FROM periods
WHERE periods.start_time >= %(start_time_1)s AND periods.end_time <= %(end_time_1)s
 LIMIT %(param_1)s]

[parameters: {'start_time_1': datetime.datetime(2025, 11, 15, 15, 11, 46, 708983), 'end_time_1': datetime.datetime(2025, 11, 15, 15, 11, 46, 
708983), 'param_1': 1}]
(Background on this error at: https://sqlalche.me/e/20/f405)

Solve this when usign student_list endpoint 
the is period table issue




/student_list

{
  "department": "Computer Science and Engineering",
  "semester": 1,
  "section": "B"
}


Keyword,Level,Meaning,When to use in your Backend
logger.debug(...),Lowest,"""I'm just checking variables.""","Variables, loop counters, SQL queries."
logger.info(...),Normal,"""Everything is working fine.""","User logged in, Data saved, Server started."
logger.warning(...),Medium,"""This is weird, but I handled it.""","Invalid password, User not found, Retrying connection."
logger.error(...),High,"""A function failed.""","Database offline, Payment failed, Bug in code."
logger.critical(...),Highest,"""The whole app is dying.""","Disk full, Memory leak, System crash."





[
  {
    "user_id": 1,
    "user_name": "Aju",
    "created_at": "2025-11-20T09:00:46.833170",
    "role": "student",
    "email": "Aju@gmail.com",
    "password_hash": "aju123"
  },
  {
    "user_id": 3,
    "user_name": "Aju",
    "created_at": "2025-11-20T09:00:46.833170",
    "role": "student",
    "email": "Aju123@gmail.com",
    "password_hash": "aju123"
  },
  {
    "user_id": 36,
    "user_name": "Boby",
    "created_at": "2025-11-20T09:00:46.833170",
    "role": "teacher",
    "email": "boby@gmail.com",
    "password_hash": "boby123"
  }
]