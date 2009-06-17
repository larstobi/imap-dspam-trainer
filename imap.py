from imaplib import *

server = IMAP4("")
server.login("", "")
mboxes = server.list()[1]
r = server.select("INBOX")
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
