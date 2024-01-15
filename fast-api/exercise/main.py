from fastapi import FastAPI
from mongoengine import (
    connect,
    disconnect,
    Document,
    StringField,
    ReferenceField,
    ListField,
    IntField
)
import json
from pydantic import BaseModel

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    connect('fast-api-database', host="mongo", port=27017)


@app.on_event("shutdown")
def shutdown_db_client():
    disconnect("mongo")


# Helper functions to convert MongeEngine documents to json

def course_to_json(course):
    course = json.loads(course.to_json())
    course["students"] = list(map(lambda dbref: str(dbref["$oid"]), course["students"]))
    course["id"] = str(course["_id"]["$oid"])
    course.pop("_id")
    return course


def student_to_json(student):
    student = json.loads(student.to_json())
    student["id"] = str(student["_id"]["$oid"])
    student.pop("_id")
    return student

# Schema

class Student(Document):
    name = StringField(required=True)
    student_number = IntField()
    

class Course(Document):
    name = StringField(required=True)
    description = StringField()
    tags = ListField(StringField())
    students = ListField(ReferenceField(Student))

# Input Validators

class CourseData(BaseModel):
    name: str
    description: str | None
    tags: list[str] | None
    students: list[str] | None


class StudentData(BaseModel):
    name: str
    student_number: int | None


# Student routes
@app.post("/students", status_code=201)
def create_student(student: StudentData):
    new_student = Student(**student.dict()).save()
    return {"message": "Student successfully created", "id": student_to_json(new_student)["id"] }

@app.get("/students", status_code=200)
def read_students():
    students = Student.objects()
    return json.loads(students.to_json())

@app.get("/students/{student_id}", status_code=200)
def read_student(student_id: str):
    student = Student.objects.get(id=student_id)
    jsonstudent = student_to_json(student)
    return jsonstudent
    
@app.put("/students/{student_id}", status_code=200)
def update_student(student_id: str, studentData: StudentData):
    Student.objects.get(id=student_id).update(**studentData.dict())
    return {"message": "Student successfully updated"}

@app.delete("/students/{student_id}", status_code=200)
def delete_student(student_id: str):
    Student.objects(id=student_id).delete()
    return {"message": "Student successfully deleted"}


# Course routes
@app.post("/courses", status_code=201)
def create_course(course: CourseData):
    new_course = Course(**course.dict()).save()
    return {"message": "Course successfully created", "id": course_to_json(new_course)["id"] }

@app.get("/courses", status_code=200)
def read_courses(tag: str = '', studentName: str = ''):
    if tag and studentName:
        json_courses = []
        courses = Course.objects(tags=tag, students__in=Student.objects(name=studentName))
        for course in courses:
            json_course = course_to_json(course)
            json_courses.append(json_course)
        return json_courses
    elif tag:
        json_courses = []
        courses_by_tag = Course.objects(tags=tag)
        for course in courses_by_tag:
            json_course = course_to_json(course)
            json_courses.append(json_course)
        return json_courses
    elif studentName:
        json_courses = []
        courses_by_studentName = Course.objects(students__in=Student.objects(name=studentName))
        for course in courses_by_studentName:
            json_course = course_to_json(course)
            json_courses.append(json_course)
        return json_courses

@app.get("/courses/{course_id}", status_code=200)
def read_course(course_id: str):
    course = Course.objects.get(id=course_id)
    return course_to_json(course)

@app.put("/courses/{course_id}", status_code=200)
def update_student(course_id: str, courseData: CourseData):
    Course.objects.get(id=course_id).update(**courseData.dict())
    return {"message": "Course successfully updated"}

@app.delete("/courses/{course_id}", status_code=200)
def delete_course(course_id: str):
    Course.objects(id=course_id).delete()
    return {"message": "Course successfully deleted"}