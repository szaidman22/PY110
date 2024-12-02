import random
import os

def initialize_deck():
    values =  ['Two', 'Three', 'Four', 'Five',
               'Six', 'Seven', 'Eight', 'Nine', 
               'Ten', 'Jack', 'Queen', 'King', 'Ace']
    points =  [2, 3, 4, 5,
               6, 7, 8, 9, 
               10, 10, 10, 10, (1,11)]
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    cards = []

    for value, point in zip(values, points):
        for suit in suits:
            cards.append([f"{value} of {suit}", point])

    random.shuffle(cards)

    deck = {card[0] : card[1] for card in cards}
    return deck

def deal_hand(deck):
    hand = [deck.popitem(), deck.popitem()]
    return hand

def hit(hand, deck):
    hand.append(deck.popitem())

def calculate_hand(hand):
    ace_count = sum([1 for card in hand
                    if card[0][:3] == "Ace"])

    running_total = sum([card[1] for card in hand
                        if card[0][:3] != "Ace"])
    
    while ace_count and running_total < 11:
        running_total += 11
        ace_count -= 1

    while ace_count and running_total >= 11:
        running_total += 1
        ace_count -= 1

    return running_total

def calculate_low_hand(hand):
    ace_count = sum([1 for card in hand
                    if card[0][:3] == "Ace"])

    running_total = sum([card[1] for card in hand
                        if card[0][:3] != "Ace"])

    while ace_count:
        running_total += 1
        ace_count -= 1

    return running_total

def bust(hand):
    return calculate_hand(hand) > 21

def print_player_hand(hand, name):
    if name.casefold() == "you":
        verb = "have"
    else:
        verb = "has"

    cards = ', '.join([card[0] for card in hand])
    score = calculate_hand(hand)
    low_score = calculate_low_hand(hand)

    if score == low_score:
        text = f"{name.title()} {verb}: {cards}. Total: {score}."
    else:
        text = f"{name.title()} {verb}: {cards}. Total: {score} or {low_score}."

    print(text)

def print_dealer_hand(hand):
    text = f"Dealer has: {hand[0][0]} and {len(hand) - 1} unknown card(s)."
    print(text)

def hit_or_stay():
    player_input = input("Hit (h) or stay (s)?\n")

    while player_input.casefold().strip() not in ['h','s','hit','stay']:
        player_input = input("Hit (h) or stay (s)?\n")
    
    return player_input[0]

def bust(hand):
    return calculate_low_hand(hand) > 21

def get_final_score(hand):
    hand_high = calculate_hand(hand)
    hand_low = calculate_low_hand(hand)

    return hand_high if hand_low <= 21 else hand_low

def determine_winner(hand_1, hand_2):
    score_1 = get_final_score(hand_1)
    score_2 = get_final_score(hand_2)

    if score_1 > score_2:
        return "first"
    if score_2 > score_1:
        return "second"
    else:
        return None
    
'''MAIN PROGRAM'''

os.system('clear')
print("Welcome to 21!\n")

deck = initialize_deck()

player_hand = deal_hand(deck)
dealer_hand = deal_hand(deck)

print_dealer_hand(dealer_hand)
print_player_hand(player_hand, "Sofia")
print("\n")

while calculate_low_hand(player_hand) < 21 and calculate_hand(player_hand) != 21:
    match hit_or_stay():
        case 'h':
            hit(player_hand, deck)
        case 's':
            break
    print("\n")
    print_player_hand(player_hand, "Sofia")

if bust(player_hand):
    print("\nOh no, you've busted! Game over.")
else:
    while calculate_hand(dealer_hand) < 17:
        hit(dealer_hand, deck)

    if bust(dealer_hand):
        print("\nThe dealer has busted. You win!")
    else:
        match determine_winner(player_hand, dealer_hand):
            case "first":
                print(f"\nCongratulations, you win with "
                      f"{get_final_score(player_hand)} points!")
            case "second":
                print(f"\nDealer wins with {get_final_score(dealer_hand)} points.")
            case _:
                print(f"\nIt's a tie! You both have {get_final_score(player_hand)} points!")

print("\nFinal hands:")
print_player_hand(player_hand, "Sofia")
print_player_hand(dealer_hand, "Dealer")
