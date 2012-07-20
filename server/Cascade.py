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

import socket
import os
import subprocess
import logging as log

log.basicConfig(filename="CascadeServer.log", level=log.DEBUG)


class CascadeServer:
    """Main Cascade Server class. Handles the file upload, and adding it to btcli"""
    def __init__(self, port):
        log.debug("Initializing CascadeServer...")
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        log.info("Server initialized, on port %s" % (self.port))

    def serve_forever(self):
        """Launches the server: SERVE FOREVER"""
        log.debug("Asked to serve forever")
        self.configure()
        self.mainloop()

    def configure(self):
        log.debug("Entering configuration")
        log.debug("Binding...")
        self.s.bind(('', self.port))
        self.s.listen(1)
        log.info("Successfully bound to port %s" % (self.port))

    def send_to_btcli(self, file_to_add=""):
        if(file_to_add != ""):
            log.info("Adding file %s to btcli" % (file_to_add))
            log.debug(subprocess.check_output(["btcli", "add", file_to_add]))
        else:
            log.error("no filename given to add to btcli!")

    def mainloop(self):
        log.debug("Entering mainloop")
        while True:
            # client receptionning loop
            conn, addr = self.s.accept()
            log.info("Client connected")
            while True:
                data = conn.recv(1024)
                if not data:
                    log.debug("No data recieved, assuming client disconnected")
                    break
                if data[0:2] == "PUT":
                    log.debug("Recieved put request")
                    conn.send("200 OK Proceed to file upload")
                    _, file_name, file_length = data.split(' ')
                    torrent = conn.recv(file_length)
                    log.debug("recieved file")
                    conn.send("200 OK File uploaded")

                    if not os.path.exists(os.path.abspath() + "/torrents"):
                        log.info("Torrent files directory not found, creating...")
                        os.makedirs(os.path.abspath() + "/torrents")
                        log.info("torrent directory successfully created")

                    with open(os.path.abspath() + "/torrents/" + file_name, 'wb') as f:
                        f.write(torrent)
                        log.debug("Successfully written torrent file")

                    self.send_to_btcli(os.path.abspath() + "/torrents/" + file_name)

            conn.close()

if __name__ == '__main__':
    try:
        CascadeServer(22222).serve_forever()
    except KeyboardInterrupt:
        print "Stopping..."
        print "OK"
