FROM python:3.8

COPY . /python-advanced

WORKDIR /python-advanced

RUN pip install pipenv

RUN pipenv install

RUN pipenv run pytest test_framework