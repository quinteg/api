FROM python:3.9.1
WORKDIR /ikt-API 

ADD . /ikt-API
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]