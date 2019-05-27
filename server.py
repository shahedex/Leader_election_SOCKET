import socket
import csv
import os
import sys
import subprocess
import random

host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

pi_list = {}

try:
    s.bind((host,port))
except:
    print 'Bind failed!'

while True:
    s.listen(2)
    (conn,addr) = s.accept()
    data = conn.recv(1024)
    key = addr[0][11:]
    pi_list[key] = int(data)
    if data != '':
        print 'Data form pi '+str(key)+' : '+str(pi_list[key])
	if len(pi_list)==2:
	    keys = pi_list.keys()
	    with open('txpowers.csv','w') as txp:
	        writer = csv.writer(txp)
	        writer.writerow((keys[0],keys[1]))
		writer.writerow((pi_list[keys[0]],pi_list[keys[1]]))
		print "CSV writing done!!!"
		break
        
	conn.close()

print "Getting the txpower of this pi..."
subprocess.call(['sudo','bash','changetx.sh'])
#subprocess.call(['iwlist','txpower'])
os.system('hostname -I > host.txt')

hostfile = open('host.txt','r')
selfip = hostfile.read()
selfip =  selfip[11:].strip()
hostfile.close()
txfile = open('txpower_leader.txt','r')
selftx = int(txfile.read().strip())
txfile.close()
print 'Data from pi '+str(selfip)+' : '+str(selftx)
print ''
pi_list[selfip] = selftx
print pi_list
print ''
newleader = random.choice(pi_list.keys())
print 'The pi '+str(newleader)+' which has txpower '+str(pi_list[newleader])+' should be the new leader'
print ''
