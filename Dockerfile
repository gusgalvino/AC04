FROM python:3.6.1-alpine
RUN pip install flask
COPY sequencia_fibonacci.py /sequencia_fibonacci.py
CMD ["python","sequencia_fibonacci.py"]
