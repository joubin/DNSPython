from dnspython import dns
from dnspython.DNSPythonBase import DNSPythonBase
import queue

class DomainDNSRecord(DNSPythonBase):
    def __init__(self, name_server, records, response_time):
        self.name_server = name_server
        self.records = records
        self.response_time = response_time


class Domain(DNSPythonBase):
    def __init__(self, url):
        self.url = url
        self.results = queue.Queue()
        self.status = queue.Queue()

    def lookup(self, name_server_collection):
        for key, name_server in name_server_collection.collection.items():
            ips, time = dns.nslookup(domain=self.url, nameserver_ip=name_server.ip)
            self.results.put(DomainDNSRecord(name_server=name_server, records=ips, response_time=time))
        self.status.put("Finished")
