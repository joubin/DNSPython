#!/usr/bin/env python
import subprocess as sp
import sys
import re
import time

nslookup_regex = re.compile(r"(Address):(\t| )?(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})$")
ip_address = re.compile('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')


def nslookup(domain, nameserver_ip):
    try:

        command = "nslookup"
        start = time.time()
        process = sp.Popen([command, domain, nameserver_ip], stdin=sp.PIPE, stdout=sp.PIPE, close_fds=True)
        end = time.time()

        (stdout, stdin, stderr) = (process.stdout, process.stdin, process.stderr)

        data = stdout.readlines()
        data = [line.decode('utf-8') for line in data]
        data = list(filter(nslookup_regex.match, data))
        ips = []

        for response in data:
            match = ip_address.search(response)
            if match:
                try:
                    ips.append(match.groups(1)[0])
                except IndexError:
                    pass # We don't care if we cant get some of the ips, but this really should happen
        return list(set(ips)), end - start

    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(1)


if __name__ == '__main__':
    result = nslookup("google.com", "8.8.8.8")
    print(result)
