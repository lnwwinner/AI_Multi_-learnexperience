FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install flask python-dotenv iqoptionapi

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
