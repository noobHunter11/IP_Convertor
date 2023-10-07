#!/usr/bin/python3
from termcolor import colored

print(colored("****************Source Code Downloader****************",'green'))
print(colored("****************Create By Stallker(*_*)*****************",'red'))

import pyfiglet # banner package

banner = colored(pyfiglet.figlet_format("Source Code Downloader"),'cyan') # use fo>
print(banner)


import urllib.request as u
import turtle


website_Domain =turtle.textinput("Domain Name","Url Address :")

source = u.urlopen(website_Domain)
source_read = source.read()

print(source_read)
