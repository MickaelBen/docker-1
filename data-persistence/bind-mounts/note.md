docker build -t bind .

docker run -d -v $(pwd)/_data:/usr/src/app/data -p 8000:8000 bind
