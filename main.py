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

choice = input(f'{Fore.BLUE}> {Fore.RESET}Option: ')

if choice == "HTTP" in choice:
    print()
    print(f'{Fore.BLUE}> {Fore.RESET}Selected: HTTP')
    print()
    urllib.request.urlretrieve('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all', 'HTTP-Proxies.txt')
    print(f'{Fore.BLUE}> {Fore.RESET}Successfully Scraped HTTP Proxies')
    input()
    exit()

if choice == "Socks4" in choice:
    print()
    print(f'{Fore.BLUE}> {Fore.RESET}Selected: Socks4')
    print()
    urllib.request.urlretrieve('https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all', 'Socks4-Proxies.txt')
    print(f'{Fore.BLUE}> {Fore.RESET}Successfully Scraped Socks4 Proxies')
    input()
    exit()

if choice == "Socks5" in choice:
    print()
    print(f'{Fore.BLUE}> {Fore.RESET}Selected: Socks5')
    print()
    urllib.request.urlretrieve('https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all', 'Socks5-Proxies.txt')
    print(f'{Fore.BLUE}> {Fore.RESET}Successfully Scraped Socks5 Proxies')
    input()
    exit()
else:
    print(f'{Fore.RED}> {Fore.RESET}INVALID Choice')
