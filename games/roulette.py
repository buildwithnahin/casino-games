import random
import time
from colorama import Fore, Style

def play_roulette(bet):
    print(f"\n{Fore.CYAN}🎲 Welcome to the Roulette Table!{Style.RESET_ALL}")
    print("1. Bet on a specific number (Pays 35:1)")
    print("2. Bet on Even/Odd (Pays 1:1)")
    
    bet_type = input(f"{Fore.YELLOW}Choose bet type (1-2): {Style.RESET_ALL}")
    
    winning_num = random.randint(0, 36)
    
    if bet_type == '1':
        try:
            target = int(input(f"{Fore.YELLOW}Choose a number between 0 and 36: {Style.RESET_ALL}"))
            if target < 0 or target > 36:
                print(f"{Fore.RED}Invalid number.{Style.RESET_ALL}")
                return 0
        except ValueError:
            print(f"{Fore.RED}Invalid input.{Style.RESET_ALL}")
            return 0
            
        print(f"\n{Fore.LIGHTBLACK_EX}The dealer spins the wheel...{Style.RESET_ALL}")
        time.sleep(1.5)
        print(f"{Fore.WHITE}The ball lands on: {winning_num}!{Style.RESET_ALL}")
        
        if target == winning_num:
            winnings = bet * 35
            print(f"{Fore.GREEN}🎉 INCREDIBLE! You guessed the exact number! You win ${winnings}!{Style.RESET_ALL}")
            return winnings
        else:
            print(f"{Fore.RED}Tough luck. You lost your ${bet} bet.{Style.RESET_ALL}")
            return -bet
            
    elif bet_type == '2':
        eo_choice = input(f"{Fore.YELLOW}Bet on Even (E) or Odd (O)? {Style.RESET_ALL}").upper()
        if eo_choice not in ['E', 'O']:
            print(f"{Fore.RED}Invalid choice.{Style.RESET_ALL}")
            return 0
            
        print(f"\n{Fore.LIGHTBLACK_EX}The dealer spins the wheel...{Style.RESET_ALL}")
        time.sleep(1.5)
        print(f"{Fore.WHITE}The ball lands on: {winning_num}!{Style.RESET_ALL}")
            
        if winning_num == 0:
            print(f"{Fore.RED}Zero! The House wins. You lost.{Style.RESET_ALL}")
            return -bet
            
        is_even = (winning_num % 2 == 0)
        
        if (eo_choice == 'E' and is_even) or (eo_choice == 'O' and not is_even):
            print(f"{Fore.GREEN}🎉 You win! It pays 1:1. You won ${bet}!{Style.RESET_ALL}")
            return bet
        else:
            print(f"{Fore.RED}You lost your ${bet} bet.{Style.RESET_ALL}")
            return -bet
            
    else:
        print(f"{Fore.RED}Invalid bet type.{Style.RESET_ALL}")
        return 0
