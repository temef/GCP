# Enter your code below 
FROM python:3.11-alpine3.18
WORKDIR /usr/app
COPY requirements.txt ./
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY main.py ./
EXPOSE 5000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]