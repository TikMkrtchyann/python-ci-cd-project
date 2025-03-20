FROM python:3.11-slim
WORKDIR /app
COPY requrements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
