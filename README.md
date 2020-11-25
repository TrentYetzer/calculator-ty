# Calculator

Calculator web app that gives live updates to history across browsers and hold it has persistant data.

## Technologies

- Django
- Django Channels
- Redis
- PostgreSQL
- Docker

## Issues

Currently, I am having an issue with the django channels because the websocket
immediatly closes on the deployed Heroku app. I play to fix it soon, but I need to go home for Thanksgiving.

## Deployment
    - git clone https://github.com/TrentYetzer/calculator-ty.git
    - cd calculator-ty
    - python -m venv calcenv
    - calcenv\Scripts\activate

    *** Local Deployment Only ***
    - python -m pip install --upgrade pip
    - python -m pip install -r requirements.txt

    - docker-compose build
    - docker-compose up -d
    - docker-compose exec web python manage.py migrate
