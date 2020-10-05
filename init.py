
from db import db

emp = db.select("SELECT * FROM EMP")
print(emp)
emp.to_csv('emp.csv', index=False)

dept = db.select("SELECT * FROM DEPT")
print(dept)
dept.to_csv('dept.csv', index=False)
