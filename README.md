

## Build
### DB
 - docker build -t fusiondb:1 infra/db
 - docker run -dit -p 5432:5432 --name=fusion_db fusiondb:1

## Run app
 - manage makemigrations
 - manage migrate
 - manage runserver
 