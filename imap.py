from imaplib import *
from string import *

configfile = "/home/larstobi/imap/config"
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
    elif var == 'folder':
        folder = strip(val)

server = IMAP4(host,port)
server.login(user,password)
mboxes = server.list()[1]
r = server.select(folder)
r, data = server.search(None, "(ALL)")

tmpdata = data[0]
uids = tmpdata.split()

for uid in data[0].split():
    r, data = server.fetch(uid, '(RFC822)')
    file = open('/home/larstobi/imap/INBOX/cur/'+uid, 'w')
    file.write(data[0][1])
    file.close()

server.close()
server.logout()
