FROM python:3.10

WORKDIR /applicacion

COPY . .

RUN pip install PyPDF2
RUN pip install wordCloud
RUN pip install matplotlib
RUN pip install PyPDF2
Run pip install grobid_client
RUN pip install requests

CMD ["python", "entrega.py"]