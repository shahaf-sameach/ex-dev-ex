FROM python:3.6-alpine
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "-u", "server.py"]


