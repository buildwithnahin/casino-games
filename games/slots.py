import random
import time

def play_slots(bet):
    symbols = ['🍒', '🍋', '🍉', '⭐', '🔔', '💎']
    print("\n🎰 Spinning the Slot Machine...")
    time.sleep(1)
    
    result = [random.choice(symbols) for _ in range(3)]
    print(f"\n   [{result[0]}] [{result[1]}] [{result[2]}]   \n")

    if result[0] == result[1] == result[2]:
        winnings = bet * 10
        print(f"🎉 JACKPOT! All three match! You won ${winnings}!")
        return winnings
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        winnings = bet * 2
        print(f"Nice! Two of a kind. You won ${winnings}!")
        return winnings
    else:
        print(f"No match. You lost ${bet}.")
        return -bet
