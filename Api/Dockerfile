# 
FROM python:3.9


COPY requirements.txt .

RUN pip install -r requirements.txt

Run mkdir Img

Run mkdir Videos


COPY . .




EXPOSE 5001

CMD ["uvicorn", "main:app","--reload" ,"--host", "0.0.0.0", "--port", "5001"]
