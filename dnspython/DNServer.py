#!/usr/bin/env python


class DNServer(object):
    """docstring for DNServer"""
    def __init__(self, arg):
        super(DNServer, self).__init__()
        self.arg = arg
        self.info = {}
        self.unPack()
    
    def unPack(self):
        for k, v in self.arg.items():
            if v != "" or v != '' or v != None:
                self.info[k] = v

    def isValid(self):
        if self.info["state"] == "valid" or self.info["state"] == "Valid":
            return True
        else:
            return False

    def getCountry(self):
        return self.info["country_id"]

    def getIP(self):
        return self.info["ip"]