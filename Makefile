build:
	docker build -t glardies/group03_api_image:latest .

push:
	docker push glardies/group03_api_image:latest

run:
	docker run -itd --name group03_api_image -p 80:80 glardies/group03_api_image:latest

delete:
	docker rm -f group03_api_image


