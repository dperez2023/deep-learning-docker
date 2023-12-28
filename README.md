### YOLO Accuracy:

By default, the best accuracy combination is selected:
epoch: 200
batch: 64
weight: 0.001

However, it can be combined in several ways with the following values:

Epoch: 100, 150, 200
Batch: 16, 32, 64
Weight: 0.01, 0.001, 0.005

### Demo images:
Within the repository in 'files' folder there are examples ready to use.

### Docker steps:

Note: Docker Daemon must be running (Ex. Docker Desktop)

# 1. Clone the repository

# 2. Build:
docker build -t group03_api_image .

# 3. Run:
docker run -d -p 80:80 group03_api_image

# 4. Use an image File (JPG) via cURL to test response
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@path/to/image/image.jpg" -F "epoch=200" -F "batch=64" -F "weight_decay=0.001" http://localhost:80/ --output -

