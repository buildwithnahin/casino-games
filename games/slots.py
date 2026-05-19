import random
import time
from colorama import Fore, Style

def play_slots(bet):
    symbols = ['🍒', '🍋', '🍉', '⭐', '🔔', '💎']
    print(f"\n{Fore.MAGENTA}🎰 Spinning the Slot Machine...{Style.RESET_ALL}")
    time.sleep(1)
    
    result = [random.choice(symbols) for _ in range(3)]
    print(f"\n   {Fore.WHITE}[{result[0]}] [{result[1]}] [{result[2]}]{Style.RESET_ALL}   \n")

    if result[0] == result[1] == result[2]:
        winnings = bet * 10
        print(f"{Fore.GREEN}🎉 JACKPOT! All three match! You won ${winnings}!{Style.RESET_ALL}")
        return winnings
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        winnings = bet * 2
        print(f"{Fore.YELLOW}Nice! Two of a kind. You won ${winnings}!{Style.RESET_ALL}")
        return winnings
    else:
        print(f"{Fore.RED}No match. You lost ${bet}.{Style.RESET_ALL}")
        return -bet
