FROM python:3.7.3
WORKDIR /web-api 

ADD . /web-api
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
