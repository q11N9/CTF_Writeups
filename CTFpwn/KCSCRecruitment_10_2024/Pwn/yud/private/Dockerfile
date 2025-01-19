FROM ubuntu:22.04

MAINTAINER anonymous
RUN apt-get update

RUN useradd -m yud

RUN apt-get update --fix-missing -y

RUN apt-get install -y apt-utils software-properties-common

RUN apt-get install -y build-essential \
        socat \
        netcat 

WORKDIR /home/yud

ADD ./flag /home/yud
ADD ./yudbet /home/yud

ENTRYPOINT ["sh", "-c", "exec socat -s TCP-LISTEN:1337,reuseaddr,fork EXEC:/home/yud/yud,stderr"]

EXPOSE 1337