from ultralytics import YOLO
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from PIL import Image
import shutil
import os

app = FastAPI(debug=True)

@app.get("/ping", summary="Ping endpoint to test connection")
def _ping():
    return "pong"

@app.post("/predict", summary="Endpoint that GET an image file and returns it with the identified image with YOLO model's "
                       "best parameters combination")
async def _test(file: UploadFile, epoch: int = 200, batch: int = 64, weight_decay: float = 0.001):
    error = {}
    if not epoch in [100, 150, 200]:
        error["Error epoch"] = f"Invalid value: {epoch}, choose between 100, 150 or 200"
    if not batch in [16, 32, 64]: 
        error["Error batch"] = f"Invalid value: {batch}, choose between 16, 32 or 64"
    if not weight_decay in [0.01, 0.001, 0.0005]:
        error["Error weight_decay"] = f"Invalid value: {weight_decay}, choose between 0.01, 0.001 or 0.005"
    
    if error:
        return error

    os.makedirs("files/results", exist_ok=True)
    save_path = f"files/results/{file.filename}"
    with open(save_path, "wb") as saved_image:
        shutil.copyfileobj(file.file, saved_image)

    path_model =f"models/e{epoch}b{batch}w{str(weight_decay)[2:]}.pt"
    model = YOLO(path_model)
    results = model(save_path)

    if results:
        annotated_image = results[0].plot() # We accept just 1 image
        im = Image.fromarray(annotated_image[..., ::-1])
        im.save(save_path)
        
    response_headers = {"epoch": str(epoch), "batch": str(batch), "weight_decay": str(weight_decay), "model": path_model}

    return FileResponse(save_path, headers=response_headers)
