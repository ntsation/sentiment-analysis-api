FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY api ./api

EXPOSE 8000

CMD ["python", "api/main.py"]
