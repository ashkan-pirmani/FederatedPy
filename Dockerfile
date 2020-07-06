FROM python:3.7


RUN mkdir /FederatedPy
RUN mkdir /FederatedPy/Data

COPY . /FederatedPy
WORKDIR /FederatedPy

RUN pip install --upgrade pip && \ 
    pip install pandas && \ 
    pip install matplotlib

CMD python /FederatedPy/Federated.py
