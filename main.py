from ultralytics import YOLO
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def test(file: UploadFile ,epoch: int = 200, batch: int = 64, weight_decay: float = 0.001):
    error = {}
    if epoch != 100 and epoch != 150 and epoch != 200:
        error["Error epoch"] = "Invalid value: {}, choose between 100, 150 or 200".format(epoch)
    if batch != 16 and batch != 32 and batch != 64:
        error["Error batch"] = "Invalid value: {}, choose between 16, 32 or 64".format(batch)
    if weight_decay != 0.01 and weight_decay != 0.001 and weight_decay != 0.005:
        error["Error weigth_decay"] = "Invalid value: {}, choose between 0.01, 0.001 or 0.005".format(weight_decay)
    if error:
        return error

    path_model = "models\e" + str(epoch) + "b" + str(batch) + "w" + str(weight_decay)[2:] + ".pt"
    file_path = f"files/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    model = YOLO(path_model)

    results = model(f"files/{file.filename}",save=True, line_width=2, project="files", name="results", exist_ok=True)

    item = {"epoch": str(epoch), "batch": str(batch), "weight_decay": str(weight_decay), "model": path_model}

    return FileResponse(f"files/results/{file.filename}", headers=item)
