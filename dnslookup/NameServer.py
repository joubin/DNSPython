from dnslookup.DNSLookupBase import DNSLookupBase


class NameServer(DNSLookupBase):
    def __init__(self, ip, name, country_id, city=None, version=None, error=None, dnssec=None, reliability=None,
                 checked_at=None, created_at=None):
        self.ip = ip
        self.name = name
        self.country_id = country_id
        self.city = city
        self.version = version
        self.error = error
        self.dnssec = dnssec
        self.reliability = reliability
        self.checked_at = checked_at
        self.created_at = created_at

    @classmethod
    def BuildFromCSV(cls, csv_row):
        try:
            return NameServer(ip=csv_row['ip'], name=csv_row['name'], country_id=csv_row['country_id'],
                              city=csv_row['city'], version=csv_row['version'], error=csv_row['error'],
                              dnssec=csv_row['dnssec'], reliability=csv_row['reliability'],
                              checked_at=csv_row['checked_at'], created_at=csv_row['created_at'])
        except Exception:
            raise RuntimeWarning("Couldn't get the right headers out of the CSV when creating a NameServer "
                                 "Object\nMake sure that the supplied URL has the following headers:\n\tip,name,"
                                 "country_id,city,version,error,dnssec,reliability,checked_at,created_at")
