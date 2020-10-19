from netmiko import ConnectHandler
from getpass import getpass

device1 = {
   "host": 'cisco1.lasthop.io',
   "username": 'pyclass',
   "password": "88newclass",
   "device_type": 'cisco_ios',
   "global_delay_factor": 2, 
   # "session_log": 'my-session.txt',
}
net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip int brief")
print (output)

