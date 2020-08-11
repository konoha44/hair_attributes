FROM python:3.8-slim

COPY . /root

WORKDIR /root

RUN pip install flask gunicorn flask_wtf boto3 tqdm
RUN pip install numpy==1.18.5
RUN pip install tensorflow==2.2.0 onnxruntime==1.4.0