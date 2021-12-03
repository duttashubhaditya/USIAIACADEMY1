FROM ubuntu:latest

RUN mkdir -p /app/src

WORKDIR /app/src

RUN apt update


RUN apt install -y python3-pip
RUN pip3 install Flask==2.0.2

COPY app.py .
EXPOSE 3000
CMD ["python3", "app.py"]

