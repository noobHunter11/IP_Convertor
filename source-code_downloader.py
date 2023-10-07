
from termcolor import colored

print(colored("****************Source Code Downloader****************",'green'))
print(colored("****************Create By Stallker(*_*)*****************",'red'))

import pyfiglet # banner package

banner = colored(pyfiglet.figlet_format("Source Code Downloader"),'cyan') # use for banner
print(banner)


import urllib.request as u

webssite_name = input("Enter the terget website :")

source = u.urlopen(webssite_name)
source_read = source.read()

print(source_read)

