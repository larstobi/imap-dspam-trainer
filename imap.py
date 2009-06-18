from imaplib import *
from string import *
import sys
import getopt

configfile = "/home/larstobi/imap/config"
opts, args = getopt.getopt(sys.argv[1:], "c:", ["conf="])
for opt, arg in opts:
    if opt in ("-c", "--conf"):
        configfile = arg

file = open(configfile, 'r')
while file:
    line = file.readline()
    if not line:
        break
    var, val = line.split("=")
    if var == 'host':
        host = strip(val)
    elif var == 'port':
        port = int(strip(val))
    elif var == 'user':
        user = strip(val)
    elif var == 'password':
        password = strip(val)
    elif var == 'imapfolder':
        imapfolder = strip(val)
    elif var == 'localfolder':
        localfolder = strip(val)

server = IMAP4(host,port)
server.login(user,password)
r = server.select(imapfolder)
r, data = server.search(None, "(ALL)")

tmpdata = data[0]
uids = tmpdata.split()

for uid in data[0].split():
    r, data = server.fetch(uid, '(RFC822)')
    file = open(localfolder+'/'+uid, 'w')
    file.write(data[0][1])
    file.close()

server.close()
server.logout()
