FROM python:3.7

RUN rm -rf /flask && mkdir -p /flask
WORKDIR /flask
VOLUME /flask


COPY requirements.txt .
RUN pip install -r requirements.txt

ENV FLASK_APP demo.py
EXPOSE 5000
CMD flask run
