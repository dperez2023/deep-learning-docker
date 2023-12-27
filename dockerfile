FROM python:3.8
RUN apt-get update && apt-get install -y libgl1-mesa-glx

WORKDIR /app

RUN git clone https://github.com/ultralytics/yolov5.git /app/ultralytics

COPY . /app

RUN pip install -r requirements.txt
RUN pip install ultralytics

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
