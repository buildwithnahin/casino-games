import random
import time

def play_roulette(bet):
    print("\n🎲 Welcome to the Roulette Table!")
    print("1. Bet on a specific number (Pays 35:1)")
    print("2. Bet on Even/Odd (Pays 1:1)")
    
    bet_type = input("Choose bet type (1-2): ")
    
    winning_num = random.randint(0, 36)
    
    if bet_type == '1':
        try:
            target = int(input("Choose a number between 0 and 36: "))
            if target < 0 or target > 36:
                print("Invalid number.")
                return 0
        except ValueError:
            print("Invalid input.")
            return 0
            
        print("\nThe dealer spins the wheel...")
        time.sleep(1.5)
        print(f"The ball lands on: {winning_num}!")
        
        if target == winning_num:
            winnings = bet * 35
            print(f"🎉 INCREDIBLE! You guessed the exact number! You win ${winnings}!")
            return winnings
        else:
            print(f"Tough luck. You lost your ${bet} bet.")
            return -bet
            
    elif bet_type == '2':
        eo_choice = input("Bet on Even (E) or Odd (O)? ").upper()
        if eo_choice not in ['E', 'O']:
            print("Invalid choice.")
            return 0
            
        print("\nThe dealer spins the wheel...")
        time.sleep(1.5)
        print(f"The ball lands on: {winning_num}!")
            
        if winning_num == 0:
            print("Zero! The House wins. You lost.")
            return -bet
            
        is_even = (winning_num % 2 == 0)
        
        if (eo_choice == 'E' and is_even) or (eo_choice == 'O' and not is_even):
            print(f"🎉 You win! It pays 1:1. You won ${bet}!")
            return bet
        else:
            print(f"You lost your ${bet} bet.")
            return -bet
            
    else:
        print("Invalid bet type.")
        return 0
