FROM ubuntu

RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

ADD client.py /root/client.py
ADD client_app.py /root/client_app.py


CMD python -u /root/client_app.py $SEND_HOST $SEND_PORT