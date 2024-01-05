### YOLO Accuracy with Global WHEAT Dataset (Wheat prediction in an image)

By default, the best accuracy combination is selected:  
- Epoch: **200**
- Batch: **64**
- Weight: **0.001**

However, it can be combined in several ways with the following values:

- Epoch: **100, 150, 200**
- Batch: **16, 32, 64**
- Weight: **0.01, 0.001, 0.005**

---
### Demo images
Within the repository in 'files' folder there are examples ready to use.

---
### Docker steps

Note: Docker Daemon must be running (Ex. Docker Desktop)

1. Clone the repository

2. Within the folder, execute the following:

```bash
# Run
make run

# Build (optional)
make build

```
  
  3. Use an image File (JPG) via cURL to test response

  ```bash
  # Test connection
  curl -X GET http://localhost:80/ping

  # Make a predict (Global Wheat Dataset)
  curl -X POST \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/image.jpg" \
  -F "epoch=200" \
  -F "batch=64" \
  -F "weight_decay=0.001" \
  http://localhost:80/predict \
  --output path/to/image-results.jpg
  ```
  

