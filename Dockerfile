FROM python:3.7
COPY Federated.py /Federated.py
COPY example_data.csv ./Data/example_data.csv

RUN pip install --upgrade pip && \ 
    pip install pandas

CMD [“python” , “/Federated.py” , "./Data/example_data.csv"]
