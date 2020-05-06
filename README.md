### How to run project

__Build image:__

`docker build . --tag django_demo`

__Run image:__

`docker run -it -v "$(pwd)":/app -p 8000:8000 --rm django_demo`
