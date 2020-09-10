FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /mehrgan
WORKDIR /mehrgan
COPY requirements.txt /mehrgan/
RUN pip install -r requirements.txt
COPY . /mehrgan/