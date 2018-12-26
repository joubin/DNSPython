# encoding=utf8

from dnslookup.DNSLookupBase import DNSLookupBase
from dnslookup.NameServer import NameServer


class NameServerCollection(DNSLookupBase):
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
        if str(url).lower().startswith("http"):
           response = cls.get_url_content(url)

        else:
            with open(url, 'r') as input_file:
                response = input_file.readlines()



        return cls.CollectionFromCSV(csv_data=response)
