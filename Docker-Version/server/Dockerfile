FROM ubuntu

RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*

ADD server.py /root/server.py
ADD server_app.py /root/server_app.py

CMD python -u /root/server_app.py $LISTEN_HOST $LISTEN_PORT
