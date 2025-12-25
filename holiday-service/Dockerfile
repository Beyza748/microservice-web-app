FROM python:3.10-slim
WORKDIR /app

RUN pip install flask requests gunicorn

COPY app.py .

CMD ["gunicorn", "--bind", "0.0.0.0:5002", "app:app"]

