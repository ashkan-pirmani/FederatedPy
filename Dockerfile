FROM python:3.7
COPY Federated.py /Federated.py
COPY example_data.csv /example_data.csv
CMD [“python” , “/Federated.py” , "./Data/example_data.csv"]
