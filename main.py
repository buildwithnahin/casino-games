from games.slots import play_slots
from games.roulette import play_roulette
from games.blackjack import play_blackjack
import json
import os
from colorama import init, Fore, Style

# Initialize colorama for cross-platform color support
init(autoreset=True)

SAVE_FILE = "save_data.json"

def load_balance():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                return data.get("balance", 1000)
        except Exception:
            pass
    return 1000

def save_balance(balance):
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump({"balance": balance}, f)
    except Exception:
        pass

def main():
    balance = load_balance()
    print(f"{Fore.CYAN}=============================={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}🎰 Welcome to Terminal Casino! 🎲{Style.RESET_ALL}")
    print(f"{Fore.CYAN}=============================={Style.RESET_ALL}")
    
    while balance > 0:
        print(f"\n{Fore.GREEN}💰 Current Balance: ${balance}{Style.RESET_ALL}")
        print("1. Play Slots")
        print("2. Play Roulette")
        print("3. Play Blackjack")
        print("4. Cash Out and Quit")
        
        choice = input(f"\n{Fore.CYAN}Choose a game (1-4): {Style.RESET_ALL}")
        
        if choice in ['1', '2', '3']:
            try:
                bet_input = input(f"{Fore.YELLOW}Enter bet amount (Max ${balance}): ${Style.RESET_ALL}")
                bet = int(bet_input)
                if bet <= 0:
                    print(f"{Fore.RED}Bet must be greater than 0!{Style.RESET_ALL}")
                    continue
                if bet > balance:
                    print(f"{Fore.RED}Insufficient funds!{Style.RESET_ALL}")
                    continue
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a valid number.{Style.RESET_ALL}")
                continue

            if choice == '1':
                balance += int(play_slots(bet))
            elif choice == '2':
                balance += int(play_roulette(bet))
            elif choice == '3':
                balance += int(play_blackjack(bet))
                
            save_balance(balance)
                
        elif choice == '4':
            print(f"\n{Fore.GREEN}Thanks for playing! Cashing out: ${balance}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}See you next time! 👋{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid choice, please select 1, 2, 3, or 4.{Style.RESET_ALL}")
            
    if balance <= 0:
        print(f"\n{Fore.RED}💸 You are broke! The House always wins. Game over.{Style.RESET_ALL}")
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Thanks for stopping by! Exiting casino...{Style.RESET_ALL}")
