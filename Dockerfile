FROM python:3.7

RUN pip install --upgrade pip && \ 
    pip install pandas
RUN mkdir /federatedpy
RUN mkdir /federatedpy/data

COPY ./federatedpy
WORKDIR ./federatedpy

CMD [ "python", "/prelim_analysis.py" ]
