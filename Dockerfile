# 
FROM python:3.9

# 
WORKDIR /app

# 
COPY . .

# 
#RUN pip install -r requirements.txt

# 


# 
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8088"]