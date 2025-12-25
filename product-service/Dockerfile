FROM python:3.10-slim
WORKDIR /app

RUN pip install flask requests gunicorn

COPY app.py .

# Gunicorn ile çalıştır
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
