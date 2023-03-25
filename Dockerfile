# Eigenentwicklung
FROM python:3.9-slim-buster

RUN useradd fitnessapp

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install --upgrade pip

COPY . .
ENV FLASK_APP fitnessapp.py

RUN chown -R fitnessapp:fitnessapp ./
USER fitnessapp

EXPOSE 8000
ENTRYPOINT ["gunicorn","-b", "0.0.0.0:8000","-w","4", "fitnessapp:app"]


