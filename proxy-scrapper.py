import time
from colorama import *
from termcolor import *
import bs4
import requests
url = "https://www.socks-proxy.net/"
headers = {"User-agent":"Mozilla/5.1"}
banner = '''
    ____  _________  _  ____  __   ___________________ _____  ____  ___  _____
   / __ \/ ___/ __ \| |/_/ / / /  / ___/ ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
  / /_/ / /  / /_/ />  </ /_/ /  (__  ) /__/ /  / /_/ / /_/ / /_/ /  __/ /    
 / .___/_/   \____/_/|_|\__, /  /____/\___/_/   \__,_/ .___/ .___/\___/_/     
/_/                    /____/                       /_/   /_/             '''

print(colored(banner,"yellow"))
banner2 = '''
+-+-+-+ +-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+
|g|e|t| |f|r|e|e| |p|r|o|x|y| |l|i|s|t|
+-+-+-+ +-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+'''
print(colored(banner2,"green"))
print(colored("[+] Written by Romeos CyberGypsy","blue"))
data = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN}Would you like to save your output to a text file?(Y/n){Fore.YELLOW}")
if data == "Y" or data == "y":
	filename = input(f"{Fore.YELLOW}[{Fore.RED}*{Fore.YELLOW}]{Fore.GREEN}Enter a file name:{Fore.YELLOW}")
	file = open(filename+".txt","a")

if data == "N" or data == "n":
	print(colored("[+]Continuing without saving output","green"))
	pass

print(colored("[!] Hold on as we scrap some free proxies for you...","green"))
data = requests.get("https://www.socks-proxy.net/", headers = headers)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
finding = soup.find_all("td")

x = 0
y = 0
labels = ["IP","Port","Code","Country","Version","Anonymity","HTTPS?","Last checked"]
while x<=599:
	print(f"{Fore.GREEN}{labels[y]} : {Fore.YELLOW}{finding[x].get_text()}")
	data_to_write = labels[y] + ":" + finding[x].get_text()
	try:
		file.write(data_to_write)
	except:
		pass

	x+=1
	y+=1
	if y%8==0:
		print("\n")
		print(f"{Fore.BLUE}Next Proxy")
		y = 0
	time.sleep(0.01)

try:
	file.close()
except:
	pass
