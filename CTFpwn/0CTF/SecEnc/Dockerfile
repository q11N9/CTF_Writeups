FROM ubuntu:22.04

RUN sed -i s:/archive.ubuntu.com:/mirrors.tuna.tsinghua.edu.cn/ubuntu:g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get -y update --fix-missing

RUN apt-get install -y socat liblzo2-2 libcapstone4 libsndio7.0 curl qemu-system-aarch64

COPY files /teespace
COPY ./start.sh /

WORKDIR /teespace

CMD ["/start.sh"]
