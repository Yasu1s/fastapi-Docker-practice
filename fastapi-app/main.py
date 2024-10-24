from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Load the model from the pickle file
with open("fastapi-app/model/model.pkl", "rb") as f:
    model = pickle.load(f)

class InputData(BaseModel):
    input: list

@app.get("/")
def read_root():
    return {"message": "API is working"}


@app.post("/predict")
def predict(data: InputData):
    # Reshape input for the model
    input_data = [data.input]
    prediction = model.predict(input_data)
    return {"prediction": prediction.tolist()}