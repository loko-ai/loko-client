FROM python:3.6-slim
ARG user
ARG password
ADD requirements.lock /
RUN pip install --upgrade --extra-index-url https://$user:$password@distribution.livetech.site -r /requirements.lock
ADD . /loko-client
ENV PYTHONPATH=$PYTHONPATH:/loko-client
WORKDIR /loko-client/loko_client/services
CMD python services.py
