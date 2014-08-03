import os, sys

class ServerListParser(object):
    """docstring for ServerListParser"""
    def __init__(self, fileName):
        super(ServerListParser, self).__init__()
        self.fileName = fileName
        self.localDict = {}
        self.readFile()
    
    def validIP(self, address):
        parts = address.split(".")
        if len(parts) != 4:
            return False
        for item in parts:
            if not 0 <= int(item) <= 255:
                return False
        return True

    def readFile(self):
        if not os.path.isfile(self.fileName):
            sys.exit()
        lines = tuple(open(self.fileName, 'r'))
        for line in lines:
            try:
                tmp = line.split(":")
                if self.validIP(tmp[1].strip()):
                    self.localDict[tmp[0]] = tmp[1].strip()
            except Exception, e:
                pass
    
    def getList(self):
        return self.localDict


if __name__ == '__main__':
    slp = ServerListParser("sample.input")
    print slp.getList()