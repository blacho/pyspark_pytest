FROM apache/spark-py:v3.3.1

USER root

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /app
WORKDIR /app
