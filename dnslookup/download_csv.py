import sys
if(int(sys.version[0]) >= 3):
    print("python 3")
    from urllib import request
    this_response = request.urlopen("https://jabbari.io/nameservers.csv")
    this_response = [item.decode("utf-8") for item in this_response]
else:
    from urllib import urlopen
    this_response = urlopen("https://jabbari.io/nameservers.csv").readlines()
final = []
# for line in this_response:
#     try:
#         final.append(str(line.decode('utf-8').encode('utf-8')))
#     except (UnicodeDecodeError, UnicodeEncodeError) as e:
#         pass  # We cant decode something
import csv

reader = csv.DictReader(this_response)

for r in reader:
    print(r)