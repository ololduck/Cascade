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
import logging as log


class FileToSend:
    """One instance per file to upload"""

    def __init__(self, filepath, serv_addr="localhost:22222"):
        self.filepath = filepath
        self.server_addr = serv_addr.split(':')
        log.debug("serv_addr: %s port: %s" % self.server_addr)
        with open(self.filepath, 'r') as f:
            self.file_data = f.readlines()
        self.send()

    def send(self):
        # here send the file. Must include all work done between server
        # and client.
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(self.server_addr)
        self.s.sendall("PUT %s %s" % (self.filepath, str(self.file_data.size())
        log.debug("recieved: %s" % self.s.recv(1024))
        self.s.sendall(self.file_data)
        log.debug("recieved: %s" % self.s.recv(1024))



if __name__ == '__main__':
    pass
