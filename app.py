from fastapi import FastAPI
from pydantic import BaseModel

from src.project_01_sentimental_analysis.components.model_prediction import ModelPredictionPipeline

class UserInput(BaseModel):
    input_text:str

class ApiOutput(BaseModel):
    input_text:str
    predicted:str
    score:float

def prediction(text):
    init=ModelPredictionPipeline()
    predictor=init.initiate_prediction_pipeline()
    return predictor.predict(text)

app=FastAPI()

@app.get("/home")
def get_home():
    return "Welcome to home page"

@app.get("/health")
def get_health():
    return {
        "status":"OK"
    }

@app.post("/predict",response_model=ApiOutput)
def get_predict(input:UserInput):
    text=input.input_text

    output=prediction(text)
    

    return {
        "input_text":text,
        "predicted": output[0]['label'],
        "score":output[0]['score']

    }

