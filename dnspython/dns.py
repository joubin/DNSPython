#!/usr/bin/env python

import subprocess as sp
import sys
from color import *

def lookup(a,b):
    try:
        address = []
        c = "nslookup"
        cleanAddress = []
        p = sp.Popen([c, a, b], stdin=sp.PIPE, stdout=sp.PIPE, close_fds=True)

        (stdout, stdin, stderr) = (p.stdout, p.stdin, p.stderr)
        data = stdout.readline()
        while data:
            # Do stuff with data, linewise.

            data = stdout.read().split()
            for i in range(0, len(data)):
                if data[i] == "Address:":
                    address.append((data[i], data[i+1]))
        stdout.close()
        stdin.close()

        for i in address:
            if b not in i[1]:
                cleanAddress.append(i[1])

        del(address)
        return cleanAddress
    except KeyboardInterrupt:
        print "Exiting..."
        sys.exit(1)

