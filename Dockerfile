FROM python:3.7

RUN pip install --upgrade pip && \ 
    pip install pandas && \ 
    pip install matplotlib
RUN mkdir /FederatedPy
RUN mkdir /FederatedPy/Data

COPY . /FederatedPy
WORKDIR /FederatedPy
-v ${PWD}:/home/jovyan/work

CMD python /FederatedPy/Federated.py
