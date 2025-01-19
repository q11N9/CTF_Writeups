FROM ubuntu:latest

RUN apt update && apt install -y socat && apt-get update && apt-get install -y libcjson-dev


RUN useradd --no-create-home -u 1000 ctf

COPY flag.txt /home/ctf/flag.txt
COPY shellcode /home/ctf/shellcode
WORKDIR /home/ctf/
RUN chmod 444 /home/ctf/flag.txt
USER ctf
CMD ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:\"/home/ctf/shellcode\""]
