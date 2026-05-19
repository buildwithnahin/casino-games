from games.slots import play_slots
from games.roulette import play_roulette

def main():
    balance = 1000
    print("==============================")
    print("🎰 Welcome to Terminal Casino! 🎲")
    print("==============================")
    
    while balance > 0:
        print(f"\n💰 Current Balance: ${balance}")
        print("1. Play Slots")
        print("2. Play Roulette")
        print("3. Cash Out and Quit")
        
        choice = input("\nChoose a game (1-3): ")
        
        if choice in ['1', '2']:
            try:
                bet = int(input(f"Enter bet amount (Max ${balance}): $"))
                if bet <= 0:
                    print("Bet must be greater than 0!")
                    continue
                if bet > balance:
                    print("Insufficient funds!")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if choice == '1':
                balance += play_slots(bet)
            elif choice == '2':
                balance += play_roulette(bet)
                
        elif choice == '3':
            print(f"\nThanks for playing! Cashing out: ${balance}")
            print("See you next time! 👋")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")
            
    if balance <= 0:
        print("\n💸 You are broke! The House always wins. Game over.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nThanks for stopping by! Exiting casino...")
