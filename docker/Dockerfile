FROM python:3.8
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python", "src/data_ingestao.py"]
