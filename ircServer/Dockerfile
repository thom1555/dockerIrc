FROM debian:latest

WORKDIR /usr/app

COPY server.py server.py

RUN apt update
RUN apt upgrade -y
RUN apt install python3 -y

EXPOSE 5000
CMD ["python3", "server.py"]
