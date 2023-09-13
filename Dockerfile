FROM python:3.11

WORKDIR /app
COPY pipeline.py pipeline_copy.py 
RUN pip install pandas

ENTRYPOINT [ "bash" ]
