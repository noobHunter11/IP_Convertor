#!/usr/bin/python3
from termcolor import colored

print(colored("****************Source Code Downloader****************",'green'))
print(colored("****************Create By Stallker(*_*)*****************",'red'))
import turtel
import pyfiglet # banner package

banner = colored(pyfiglet.figlet_format("Source Code Downloader"),'cyan') # use for banner
print(banner)


import urllib.request as u

website_Domain = input("Domain Name", "Url Address:")#animation input from user

source = u.urlopen(website_Domain)
source_read = source.read()

print(source_read)

