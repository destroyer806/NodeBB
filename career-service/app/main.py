from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel, Field

app = FastAPI()

# Model Setup
class Student(BaseModel):
    student_id: str = Field(alias="Student ID")
    gender: str = Field(alias="Gender")
    age: str = Field(alias="Age")
    major: str = Field(alias="Major")
    gpa: str = Field(alias="GPA")
    extra_curricular: str = Field(alias="Extra Curricular")
    num_programming_languages: str = Field(alias="Num Programming Languages")
    num_past_internships: str = Field(alias="Num Past Internships")

    class Config:
        allow_population_by_field_name = True

class PredictionResult(BaseModel):
    good_employee: int

# Routes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict(student: Student) -> PredictionResult:
    # TODO: Validate student
    clf = joblib.load('app/model.pkl')
    
    student = student.dict(by_alias=True)
    try:
        query = pd.DataFrame(student, index=[0])
        prediction = clf.predict(query)
        return PredictionResult(good_employee=prediction[0])
    except Exception as e: 
        # TODO: Properly handle errors
        print(e)
        raise HTTPException(status_code=500, detail=e)
