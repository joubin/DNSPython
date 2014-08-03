#!/usr/bin/env python

from dns import *
import argparse
import signal
import sys, os
import ServerListParser



dnsList = {}
urlArgument = 1
args = None
os.chdir(os.path.dirname(os.path.realpath(__file__)))
def commandLineInt():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", "-l", default="1", help="This option allows you to: (1) use a large database of DNS Servers. (2) Use just the google DNS Servers. (3) Use your own server list. <Requires properly formatted file> ")
    parser.add_argument("domain", help="The domain that you would like to use. ")
    parser.add_argument("--file", help="Name of the file to use with option (3) of level")
    args = parser.parse_args()
    print args.file
    print os.path.dirname(os.path.realpath(__file__))
    if args.level == "3" and  args.file == None:
        parser.print_help()
        sys.exit()
def setup(level):
    global dnsList
    if level == "1":
        import json
        import urllib2
        import DNServer
        data = urllib2.urlopen('http://joubin.me/nameservers.json')

        j = json.load(data)
        server = []
        for i in j:
            tmp = DNServer.DNServer(i)
            server.append(tmp)

        for i in server:
            if i.isValid():
                dnsList[i.getCountry()] = i.getIP()
    elif level == "2":
        dnsList["Google 1"] = "8.8.8.8"
        dnsList["Google 2"] = "8.8.4.4"
    elif level == "3":
        slp = ServerListParser.ServerListParser(args.file)
        dnsList = slp.getList()
    else:
        print bcolors.FAIL + str("Unknown option \"%s\"" % level) + bcolors.ENDC
        sys.exit(1)
        


def main():
    global dnsList
    setup(args.level)
    print "Result for " + str(args.domain)
    print "Servers", "\t\tDNS IP", "\t\tResult"
    for k,v in dnsList.items():
        try:
            num = lookup(str(args.domain), v)[0]
            print "%4s" % bcolors.OKGREEN + str(k) + bcolors.ENDC,"\t", "%15s" %str(v),"\t", "%12s" % num
        except Exception, e:
            if e == KeyboardInterrupt:
                sys.exit(1)
            print "%4s" % bcolors.FAIL + str(k) + bcolors.ENDC,"\t", "%15s" %str(v),"\t",  "%12s" % num




commandLineInt()
main()