#!/usr/bin/python3
# Domain to ip

from termcolor import colored

print(colored("****************Domain To IP Convertor****************",'green'))
print(colored("****************Create By Stallker(*_*)*****************",'red'))

import pyfiglet # banner package
import socket
banner = colored(pyfiglet.figlet_format("IP Convertor"),'cyan') # use for banner
print(banner)

domain_Name = input("Enter You target Domain:")\

ip = socket.gethostbyname(domain_Name)

print("IP For {} : {}".format(domain_Name,ip))

