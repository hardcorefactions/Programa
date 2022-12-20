import requests
from colorama import Fore
import os
username = input("Username: ")
url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
response = requests.get(url)
uuid = response.json()['id']
os.system("cls")

print(Fore.YELLOW + "Username".center(50, " "))
print(Fore.WHITE + username.center(50, " "))
print("")
print(Fore.YELLOW + "UUID".center(50, " "))
print(Fore.WHITE + uuid.center(50, " "))
print(Fore.WHITE + "")


