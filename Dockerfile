FROM python:3.7
COPY Federated.py /Federated.py

RUN pip install --upgrade pip && \ 
    pip install pandas

CMD [“python” , “/Federated.py” , "./Data/example_data.csv"]
