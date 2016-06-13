#!/usr/bin/python
# coding: utf-8

__author__ = 'Usual'

import socket

def alive(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect((ip, int(port)))
        sock.shutdown(2)
        return True
    except:
        return False

if __name__ == '__main__':
    for i in range(1, 10000):
        if alive('127.0.0.1', i): print i, True