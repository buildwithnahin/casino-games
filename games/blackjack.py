import random
import time
from colorama import Fore, Style

def calculate_hand(hand):
    value = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            aces += 1
            value += 11
        else:
            value += int(card)
            
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
        
    return value

def play_blackjack(bet):
    print(f"\n{Fore.CYAN}🃏 Welcome to the Blackjack Table!{Style.RESET_ALL}")
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(deck)
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    while True:
        player_val = calculate_hand(player_hand)
        print(f"\n{Fore.LIGHTYELLOW_EX}Your hand: {player_hand} (Value: {player_val}){Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLACK_EX}Dealer's visible card: [{dealer_hand[0]}]{Style.RESET_ALL}")
        
        if player_val == 21:
            print(f"{Fore.GREEN}🎉 BLACKJACK! You win!{Style.RESET_ALL}")
            return bet * 1.5
        elif player_val > 21:
            print(f"{Fore.RED}💥 BUST! You went over 21. You lose.{Style.RESET_ALL}")
            return -bet
            
        action = input(f"{Fore.CYAN}Do you want to (H)it or (S)tand? {Style.RESET_ALL}").upper()
        if action == 'H':
            card = deck.pop()
            print(f"You drew a [{card}]")
            time.sleep(1)
            player_hand.append(card)
        elif action == 'S':
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please enter H or S.{Style.RESET_ALL}")
            
    print(f"\n{Fore.LIGHTBLACK_EX}Dealer reveals hand: {dealer_hand} (Value: {calculate_hand(dealer_hand)}){Style.RESET_ALL}")
    time.sleep(1)
    
    while calculate_hand(dealer_hand) < 17:
        card = deck.pop()
        print(f"{Fore.LIGHTBLACK_EX}Dealer hits and draws [{card}]{Style.RESET_ALL}")
        dealer_hand.append(card)
        time.sleep(1)
        
    dealer_val = calculate_hand(dealer_hand)
    print(f"\n{Fore.LIGHTBLUE_EX}Final Hands - You: {player_val} | Dealer: {dealer_val}{Style.RESET_ALL}")
    
    if dealer_val > 21:
        print(f"{Fore.GREEN}🎉 Dealer BUSTS! You win!{Style.RESET_ALL}")
        return bet
    elif player_val > dealer_val:
        print(f"{Fore.GREEN}🎉 You beat the dealer! You win!{Style.RESET_ALL}")
        return bet
    elif player_val < dealer_val:
        print(f"{Fore.RED}💥 Dealer wins. You lose.{Style.RESET_ALL}")
        return -bet
    else:
        print(f"{Fore.YELLOW}🤝 It's a tie (Push). You get your bet back.{Style.RESET_ALL}")
        return 0