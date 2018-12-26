#!/usr/bin/env python

import argparse
import csv
from future.standard_library import install_aliases
install_aliases()

from threading import Thread
from queue import Empty

from dnslookup.Domain import Domain
from dnslookup.NameServer import NameServer
from dnslookup.NameServerCollection import NameServerCollection
from dnslookup.dns import *



collection = None
urlArgument = 1
args = None
parse = None


def commandLineInt():
    global args
    global parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", "-l", default="1",
                        help="This option allows you to: (1) use a large database of DNS Servers from public-dns.info "
                             "(2) Use just the google DNS Servers. (3) Use your own server list. <Requires properly "
                             "formatted file> ")
    parser.add_argument("--file", "-f",
                        help="If provided, it will output to the file instead of console. File must be a csv")

    parser.add_argument("domain", help="The domain that you would like to use. ")
    parser.add_argument("--url", help="URL to use with option (3) of level. It could be a file or a url")
    args = parser.parse_args()

    if args.level == "3" and args.url is None:
        parser.print_help()
        sys.exit(-1)

    if args.file is not None:
        if not str(args.file).endswith("csv"):
            parser.print_help()
            sys.exit(-1)


def setup():
    global args
    global collection
    if args.level == "1":
        collection = NameServerCollection.CollectionFromCSVURL(url="https://public-dns.info/nameservers.csv")
    elif args.level == "2":
        collection = NameServerCollection()
        collection.add_server(NameServer(ip="8.8.8.8", name="Google 1", country_id="US"))
        collection.add_server(NameServer(ip="8.8.4.4", name="Google 2", country_id="US"))
    elif args.level == "3":
        print(args.url)
        collection = NameServerCollection.CollectionFromCSVURL(url=args.url)
    else:
        parser.print_help()
        sys.exit(-1)


def console(domain):
    print("Result for {0}".format(str(domain.url)))
    print("{country} {ip} {result}".format(country="Country".rjust(7),
                                           ip="DNS Server".rjust(24),
                                           result="Result".rjust(22)))
    while domain.status.empty():
        try:
            mapping = domain.results.get(block=True, timeout=2)
            if mapping is not None:
                for record in mapping.records:
                    print(
                        "{country} \t{ip} \t\t{Result}".format(country=str(mapping.name_server.country_id).rjust(7),
                                                               ip=str(mapping.name_server.ip).rjust(20),
                                                               Result=str(record).rjust(15)))
        except Empty:
            pass


def output_csv(domain):
    with open(args.file, 'w') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(["Country", "DNS Server", "Result", "Response Timne"])
        while domain.status.empty():
            try:
                mapping = domain.results.get(block=True, timeout=2)
                if mapping is not None:
                    for record in mapping.records:
                        writer.writerow(
                            [mapping.name_server.country_id, mapping.name_server.ip, record, mapping.response_time])
            except Empty:
                pass


def main():
    commandLineInt()
    setup()
    domain = Domain(url=args.domain)
    t = Thread(target=domain.lookup, args=(collection,))
    t.daemon = True
    t.start()
    try:
        if args.file is None:
            console(domain=domain)
        else:
            output_csv(domain=domain)

    except KeyboardInterrupt:
        t.join(timeout=1)
        sys.exit(-1)
    t.join()


if __name__ == '__main__':
    main()
