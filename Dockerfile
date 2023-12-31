FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app/app
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt
