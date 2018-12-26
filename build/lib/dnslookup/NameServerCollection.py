# encoding=utf8

from dnslookup.DNSPythonBase import DNSPythonBase
from dnslookup.NameServer import NameServer


class NameServerCollection(DNSPythonBase):
    def __init__(self):
        self.collection = {}

    def add_server(self, name_server):
        self.collection[name_server.ip] = name_server

    def lookup(self, domain):
        import dnslookup.dns as dns
        for name_server in self.collection:
            ips = dns.nslookup(domain=domain, nameserver_ip=name_server.ip)

    @classmethod
    def CollectionFromCSV(cls, csv_data):
        import csv
        collection = cls()
        reader = csv.DictReader(csv_data)
        try:
            for row in reader:
                collection.add_server(NameServer.BuildFromCSV(csv_row=row))
        except Exception as e:
            pass
        return collection

    @classmethod
    def CollectionFromCSVURL(cls, url):
        from future.standard_library import install_aliases
        install_aliases()
        from urllib.request import urlopen
        response = urlopen(url)
        # response = [str(line.decode('utf-8')) for line in response.readlines()]
        final = []
        for line in response.readlines():
            try:
                final.append(line.decode('utf-8').encode('utf-8'))
            except (UnicodeDecodeError, UnicodeEncodeError) as e:
                pass  # We cant decode something
        return cls.CollectionFromCSV(csv_data=final)
