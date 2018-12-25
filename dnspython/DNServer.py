#!/usr/bin/env python


class DNServer(object):
    """docstring for DNServer"""

    def __init__(self, arg):
        self.arg = arg
        self.info = {}
        self.unpack()

    def unpack(self):
        for k, v in self.arg.items():
            if v != "" or v != '' or v is not None:
                self.info[k] = v

    def isValid(self):
        if self.info["state"] == "valid" or self.info["state"] == "Valid":
            return True
        else:
            return False

    def get_country(self):
        return self.info["country_id"]

    def get_ip(self):
        return self.info["ip"]
