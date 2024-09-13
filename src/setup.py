import socket
import subprocess

command = [
    'netsh', 'advfirewall', 'firewall', 'add', 'rule', 
    'name="Open Port 22"', 
    'protocol=TCP', 'dir=in', 'localport=22', 'action=allow'
]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1',22))
if result == 0:
   print "Le port est ouvert"
	SSHhoneypot()
else:
   print "Port is not open"
   subprocess.run(command, shell=True, check=True)
   print("Le port 22 est maintenant ouvert.")
   SSHhoneypot()
	
sock.close()
