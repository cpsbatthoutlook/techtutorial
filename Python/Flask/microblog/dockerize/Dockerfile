FROM python:3.8.2-alpine3.10
LABEL maintainer="Chander Batth"
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py
COPY ./prepare.sh /tmp/perpare.sh   
RUN sh /tmp/perpare.sh
EXPOSE 5000
# ENTRYPOINT ["python", "/app/app.py"]
