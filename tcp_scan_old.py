import ipaddress
import subprocess
mynet = ipaddress.ip_network('192.168.1.0/24') #create an ipaddress object for 192.168.1.0/24
for host in mynet.hosts():                    #loop through each host of 192.168.1.0/24
    host = str(host)                          #change from ipaddress object to string to hand to ping command
    proc = subprocess.run(                    #use subprocess to call ping command, split to multiple lines cuz its long
        ['ping', host, '-c', '1'],            #calling ping here, putting in host to ping
        stderr=subprocess.DEVNULL,            #silence ping command errors
        stdout=subprocess.DEVNULL             #silence ping command output
        )
    if  proc.returncode == 0:                 #return code of 0 from ping command means it got a reply
        print(f'{host} is alive!')            #say this host is alive if we got a reply
