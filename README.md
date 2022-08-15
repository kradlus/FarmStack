# **FarmStackWithVue** - Just a boilerplate

This repository uses FastAPI [FastAPI](https://github.com/tiangolo/fastapi) for the backend environment. The environment includes mongodb interaction and JWT authentication. For the frontend part the code uses [VueJS](https://vuejs.org/) which is a great frontend framework that helps building frontend application in a secure and fast way.

## **Usage**

Clone the repository

```bash
    git clone https://github.com/kradlus/FarmStackWithVue
```

### **Backend**

To install backend dependencies:

```bash
    cd backend
    python3 -m pip install pipenv
    pipenv install --ignore-pipfile
```

`--ignore-pipfile` here is used in order to force pipenv to not download the latest versions of the packages from the pipfile, and instead take the fixed versions in the file `Pipfile.lock` and avoid compatibility issues.

Also the backend needs a mongodb server to store data; for test purposes I used the mongodb docker container from https://hub.docker.com/_/mongo.

Below the files to reproduce the docker environment:

> 1. Create a `docker-compose.yml` file
> ```yaml
> version: "2.4"
> 
> services:
>  mongo:
>     build: mongo
>     ports:
>       - 27017
>     mem_limit: 512 MB
>     cpus: 0.2
> ```
> 
> 2. Create a folder named `mongo`
> 
> ```bash
>   mkdir mongo
> ```
> 
> 3. Create a mongo docker file
> 
> ```dockerfile
> FROM mongo:focal
> 
> ENV MONGO_INITDB_ROOT_USERNAME <USERNAME>
> ENV MONGO_INITDB_ROOT_PASSWORD <PASSWORD>
> 
> RUN echo -n 'db.createCollection("farm")' > /docker-entrypoint-initdb.d/coll.js
> RUN echo -n 'db.createCollection("dashboard")' > /docker-entrypoint-initdb.d/coll2.js
> ```
> executing `docker-compose up --build` a mongodb container will start and two collections ("farm", "dashboard"), will be created

In order to work the backend needs a `.env` where to store `MONGO_USERNAME`, `MONGO_PASSWORD` and `MONGO_HOST`. The file will be then loaded by `python-dotenv` ( installed in the previous step as dependency in the Pipfile ).

To execute the backend environment after the database is started:

```bash
    cd backend/src
    pipenv run hypercorn asgi:application --reload 
```

This will start the hypercorn server and any change done to the code will be updated in real time due to the `--reload` flag

### **Frontend**

To install frontend dependencies:

```bash
    cd frontend/app
    npm i
```

To execute the frontend environment 

```bash
    npm run serve
```