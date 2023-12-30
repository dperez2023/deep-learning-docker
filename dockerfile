FROM ultralytics/ultralytics:latest
WORKDIR /app

COPY requirements.txt .
RUN pip install -r /app/requirements.txt

COPY . .

EXPOSE 80

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
