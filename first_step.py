from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    apple = "apple"
    phone = "phone"
    bag = "bag"


app = FastAPI()


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.apple:
        return {
            "model_name": model_name,
            "message": "This is apple"
        }
    if model_name.value == "phone":
        return {
            "phone": model_name,
            "message": "This phone is mine"
        }
    return {
        "model_name": model_name,
        "message": "This is my bag"
    }
