FROM python:3.6.1-alpine
RUN pip install flask
COPY sequencia_fibonacci.py /app.py
CMD ["python","app.py"]
