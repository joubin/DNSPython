from dns import *

dnsList = {}
urlArgument = 1
def setup():
    global dnsList
    global urlArgument
    dnsList = {'West Coast':'68.87.85.98', 'East Coast': '68.87.64.146'}
    dnsList['Australia'] = '192.189.54.33'
    dnsList['New Zealand'] = '202.27.158.40'
    dnsList['United Kingdom'] = '195.7.224.57'
    dnsList['Google Main'] = '8.8.8.8'
    dnsList['Google Backup'] = '8.8.4.4'
    if sys.argv[1] == "-d":
        dnsList = {}
        myFile = sys.argv[2]
        f = open(myFile, 'r')
        read = f.read()
        for i in read:
            pass
def main():
    setup()
    print "Result for " + sys.argv[urlArgument]
    for k,v in dnsList.items():
        try:
            num = lookup(sys.argv[urlArgument], v)[0]
            print bcolors.OKGREEN + k + bcolors.ENDC,'\t', v, "\thas ", num
        except:
            print bcolors.FAIL + k + bcolors.ENDC,'\t', v, "\thas\t  -"

main()