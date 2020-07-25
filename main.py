#Made By Dropout
#Give Me Credit

import urllib.request, colorama, os, ctypes
from colorama import Fore

os.system('cls')
os.system("title [PROXYSCRAPE] By Dropout")

print(f'''{Fore.BLUE}
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ ███████╗██║     ██████╔╝███████║██████╔╝█████╗  
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝ {Fore.RESET}

{Fore.BLUE}╔═════════════════{Fore.RESET}Options{Fore.BLUE}═════════════════╗
{Fore.BLUE}║                                         {Fore.BLUE}║
{Fore.BLUE}║     {Fore.BLUE}[{Fore.RESET}HTTP{Fore.BLUE}]{Fore.RESET} - Scrapes HTTP Proxies       {Fore.BLUE}║
{Fore.BLUE}║     {Fore.BLUE}[{Fore.RESET}Socks4{Fore.BLUE}]{Fore.RESET} - Scrapes Socks4 Proxies   {Fore.BLUE}║
{Fore.BLUE}║     {Fore.BLUE}[{Fore.RESET}Socks5{Fore.BLUE}]{Fore.RESET} - Scrapes Socks5 Proxies   {Fore.BLUE}║
{Fore.BLUE}║                                         {Fore.BLUE}║
{Fore.BLUE}╚═════════════════════════════════════════╝
{Fore.RESET}''')

def scrape(type):
    print(f'{Fore.BLUE}> {Fore.RESET}Selected: {type}')
    urllib.request.urlretrieve(f'https://api.proxyscrape.com/?request=getproxies&proxytype={type.lower()}&timeout=10000&country=all&ssl=all&anonymity=all', f'{type}-Proxies.txt')
    print(f'{Fore.BLUE}> {Fore.RESET}Successfully Scraped {type} Proxies')
    input()
    exit()

choice = input(f'{Fore.BLUE}> {Fore.RESET}Option: ')
if(choice == "HTTP".lower() or choice == "Socks4".lower() or choice == "Socks5".lower()):
    scrape(choice)
else:
    print(f'{Fore.RED}> {Fore.RESET}INVALID Choice')
