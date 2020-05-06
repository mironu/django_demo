How to run project
Build image:
docker build . --tag django_demo

Run image:
docker run -it -v "$(pwd)":/app -p 8000:8000 --rm django_demo