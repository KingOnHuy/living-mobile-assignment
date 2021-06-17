FROM python:3.8-slim
WORKDIR /backend_rest_drf
RUN apt update && apt upgrade -y
# RUN apt install gettext -y
ADD ./requirements.txt /backend_rest_drf/requirements.txt
RUN pip3 install -r /backend_rest_drf/requirements.txt
COPY . /backend_rest_drf/
