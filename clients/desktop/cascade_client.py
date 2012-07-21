#!/usr/bin/env python

# MIT License
# ===========

# Copyright (c) 2012 Paul Ollivier <paul.ollivier.contact@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import socket as socket
import sys
import os
import logging as log


log.basicConfig(filename="sendfile.log", level=log.DEBUG)


class FileToSend:
    """One instance per file to upload"""

    def __init__(self, filepath, serv_addr="localhost:22222"):
        log.debug("Initializing new FileToSend")
        self.filepath = filepath
        self.server_addr = tuple(serv_addr.split(':'))
        print self.server_addr
        log.debug("serv_addr: %s port: %s" % tuple(self.server_addr))
        with open(self.filepath, 'rb') as f:
            self.file_data = f.read()
            self.file_size = os.path.getsize(self.filepath)
        self.send()

    def send(self):
        # here send the file. Must include all work done between server
        # and client.
        log.info("Begining file sending")
        log.debug("Opening Socket...")
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log.debug("Connecting...")
        self.s.connect((self.server_addr[0], int(self.server_addr[1])))
        log.debug("Sending message : %s" % "PUT %s %s" % (
            self.filepath,
            str(self.file_size)
            ))
        self.s.sendall("PUT %s %s" % (
            self.filepath,
            str(self.file_size)
            ))
        log.debug("recieved: %s" % self.s.recv(1024))
        self.s.sendall(self.file_data)
        log.debug("recieved: %s" % self.s.recv(1024))


if __name__ == '__main__':
    f = FileToSend(sys.argv[1])
