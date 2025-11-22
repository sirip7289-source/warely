FROM python:3.10-slim

WORKDIR /code

COPY requirements.txt .

# Upgrade pip first, then install with a long timeout
RUN pip install --upgrade pip && \
    pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
