 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /django_docker
 WORKDIR /django_docker
 ADD django-requirements.txt /django_docker/
 RUN pip install -r django-requirements.txt
 ADD . /django_docker/