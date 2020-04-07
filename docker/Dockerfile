FROM python:3.8-slim
WORKDIR /tmp
COPY . ./iosbackup/
RUN pip3 install ./iosbackup && rm -rf /tmp/iosbackup
WORKDIR /backup
CMD ["iosbackup"]


