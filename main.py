from booster import *
import time, json, os
import fade

if os.name == 'nt':
    import ctypes

def cls():
    os.system('cls' if os.name =='nt' else 'clear')

if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f"Cypher Booster | Discord.gg/m74UnnrVts")
else:
    pass
    
config = json.load(open("config.json", encoding="utf-8"))



def getinvite(invite_input):
    if "discord.gg" not in invite_input:
        return invite_input
    if "discord.gg" in invite_input:
        invite = invite_input.split("discord.gg/")[1]
        return invite
    if "https://discord.gg" in invite_input:
        invite = invite_input.split("https://discord.gg/")[1]
        return invite
    if "invite" in invite_input:
        invite = invite_input.split("/invite/")[1]
        return invite

def menu():
    text = '''
                               _____            _               
                              / ____|          | |              
                             | |    _   _ _ __ | |__   ___ _ __ 
                             | |   | | | | '_ \| '_ \ / _ \ '__|
                             | |___| |_| | |_) | | | |  __/ |   
                              \_____\__, | .__/|_| |_|\___|_|   
                                     __/ | |                    
                                    |___/|_|   
                                                     
                                     [1] Boost Servers
                                     [2] Check Stock
                                     [3] Quit  
'''
    
    faded_text = fade.water(text)
    print(faded_text)
    choice = input(f"\n{Style.BRIGHT}{Fore.BLUE}Choice {Fore.ARROW} " + Fore.RESET)
    
    

    if choice == "1":
        invite = getinvite(input(f"{Style.BRIGHT + Fore.BLUE}Invite Code (discord.gg/): {Fore.RESET}"))
        amount = input(f"{Style.BRIGHT + Fore.BLUE}Boosts Amount: {Fore.RESET}")
        while amount.isdigit() != True:
            print(Fore.BLUE + "Amount cannot be 0." + Fore.RESET)
            amount = input(f"{Style.BRIGHT + Fore.BLUE}Boost Amount: {Fore.RESET}")
        months = input(f"{Style.BRIGHT + Fore.BLUE}Duration (1 or 3): {Fore.RESET}")
        while amount.isdigit() != True:
            print(Fore.BLUE + "Duration must be 1 or 3." + Fore.RESET)
            months = input(f"{Style.BRIGHT + Fore.BLUE}Duration (1 or 3): {Fore.RESET}")
        start = time.time()
        boosted = thread_boost(invite, int(amount), int(months), config['nickname'], config["bio"])
        end = time.time()
        print()
        sprint(f"Boosted https://discord.gg/{invite} {variables.boosts_done} times in {round(end - start, 2)} seconds.", True)
        print()
        input(Style.BRIGHT + Fore.WHITE + "Press enter to return to menu" + Fore.RESET)
        cls()
        menu()
        
    if choice == "2":
        print(f'{Style.BRIGHT + Fore.BLUE}1 Month Nitro Tokens {Fore.WHITE} > {len(open("input/1m_tokens.txt", "r").readlines())}{Fore.RESET}')
        print(f'{Style.BRIGHT + Fore.BLUE}1 Month Boosts {Fore.WHITE} > {len(open("input/1m_tokens.txt", "r").readlines())*2}{Fore.RESET}')
        print()
        print(f'{Style.BRIGHT + Fore.BLUE}3 Month Nitro Tokens {Fore.WHITE} > {len(open("input/3m_tokens.txt", "r").readlines())}{Fore.RESET}')
        print(f'{Style.BRIGHT + Fore.BLUE}3 Month Boosts {Fore.WHITE} > {len(open("input/3m_tokens.txt", "r").readlines())*2}{Fore.RESET}')
        print()
        input(Style.BRIGHT + Fore.WHITE+ "Press enter to return to menu" + Fore.RESET)
        cls()
        menu()
        
    if choice == "3":
        quit()
        
if __name__ == "__main__":
    cls()
    menu()