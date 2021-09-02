from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class StudentDetail(BaseModel):
    name : str
    address: str
    email: str
    age: int

class StudentDetailUpdate(BaseModel):
    name : Optional[str]
    address: Optional[str]
    email: Optional[str]
    age: Optional[int]



students = {}

@app.get('/get-student')
def get_by_id(id : int = Query(None, title='Student Id')):
    for student_id in students:
        if student_id == id:
            return students[student_id]
        return {'Msg': 'Student Id Doesnot Exists'}
    return {'Msg': 'No Entries Found'}

@app.get('/get-by-name')
def get_by_name(name : str = Query(None, title='Name', description='Name of Student')):
    for student_id in students:
        if students[student_id].name == name:
            return students[student_id]
        return {'Msg': 'Student Name Doesnot Exists'}
    return {'Msg': 'No Entries Found'}

@app.post('/create-student/{student_id}')
def create_student(student_id : int, student:StudentDetail):
    if student_id in students:
        return {'Error': 'Student Id Already Exists'}
    students[student_id] = student
    return students[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id : int, student: StudentDetailUpdate):
    if student_id not in students:
        return {'Error': 'Student Id Doesnot Exists'}
    if student.name != None:
        students[student_id].name = student.name
    if student.address != None:
        students[student_id].address = student.address
    if student.email != None:
        students[student_id].email = student.email
    if student.age != None:
        students[student_id].age = student.age
    return students[student_id]

@app.delete('/delete-student/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {'Error': 'Student Id Doesnot Exists'}
    del students[student_id]
    return {'Msg': 'Student Delete Sucessfully'}




