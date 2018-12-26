import sys



class DNSLookupBase:

    @classmethod
    def get_url_content(cls, url):
        if int(sys.version[0]) >= 3:
            from urllib import request
            this_response = request.urlopen(url)
            this_response = [item.decode("utf-8") for item in this_response]
        else:
            from urllib import urlopen
            this_response = urlopen(url).readlines()
        return this_response
