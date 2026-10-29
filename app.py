from fastapi import FastAPI
from pydantic import BaseModel
import os
import uvicorn
from starlette.responses import RedirectResponse
from fastapi.responses import Response
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

@app.get("/")
def get_home():
    return RedirectResponse(url="/docs")

@app.get("/health")
def get_health():
    return {
        "status":"OK"
    }

@app.get("/train")
def training():
    try:
        os.system("python main.py")
        return Response("Training done")
    except Exception as e:
        return Response(f"Error Occured {e}")



@app.post("/predict",response_model=ApiOutput)
def get_predict(input:UserInput):
    text=input.input_text
    try:

        output=prediction(text)
        return {
            "input_text":text,
            "predicted": output[0]['label'],
            "score":output[0]['score']
        
            }
    except Exception as e:
        raise e
    

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)
    

   

