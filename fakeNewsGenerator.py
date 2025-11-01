"""
Multi-Function Entertainment Program
This program provides various entertainment functions including:
1. Fake News Generator
2. Daily Horoscope
3. Math Problem Generator
4. Blackjack Game

"""

import random
from datetime import datetime
from typing import List, Tuple, Set, Optional, Union

# ============================================================================
# CONSTANTS AND DATA
# ============================================================================

# Blackjack related constants
SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# News generator related data
subjects = [
    'Donald Trump', 'Vladimir Putin', 'Barrack Obama', 'Member of the FBI',
    'A group of Los Angelenos', 'Bill Gates', 'A dog named Spike'
]

actions = [
    'launches attack on rabies', 'cancels tour', 'fights a walrus',
    'eats worms', 'declares war on spiders', 'orders a bowl of cereal',
    'celebrates their Emmy award'
]

places = [
    'at Olive Garden', 'in Grand Central Park', 'on a Disney Cruise',
    'inside the White House', 'at Coachella', 'during a baseball game',
    'at the Grand Canyon'
]

news_outlets = [
    'CNN', 'Fox News', 'NBC News', 'ABC News', 'CBS News',
    'The New York Times', 'The Washington Post', 'USA Today',
    'Associated Press', 'Reuters', 'NPR', 'Bloomberg',
    'The Wall Street Journal', 'Politico', 'BBC News America'
]

# Horoscope related data
signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

predictions = [
    "Today brings new opportunities your way",
    "You'll find unexpected joy in small moments",
    "A conversation will lead to important insights",
    "Your creativity is especially strong today",
    "Financial matters require careful attention",
    "Romance is in the air for you",
    "Trust your intuition in decision-making",
    "A challenge will become a blessing in disguise",
    "Your leadership qualities will shine",
    "Take time for self-reflection today"
]

# Track unique generations
total_headlines = len(subjects) * len(actions) * len(places)
total_horoscopes = len(signs) * len(predictions)
seen_horoscopes: Set[str] = set()
seen_headlines: Set[str] = set()
seen_math_problems: Set[str] = set()

# ============================================================================
# BLACKJACK RELATED FUNCTIONS
# ============================================================================

def create_deck() -> List[Tuple[str, str]]:
    """
    Creates a standard deck of 52 playing cards.
    
    Returns:
        List[Tuple[str, str]]: List of (rank, suit) pairs representing cards
    """
    return [(rank, suit) for suit in SUITS for rank in RANKS]

def calculate_hand_value(hand: List[Tuple[str, str]]) -> int:
    """
    Calculates the value of a blackjack hand, handling aces optimally.
    
    Args:
        hand: List of (rank, suit) tuples representing cards
        
    Returns:
        int: Total value of the hand with aces counted as 1 or 11
    """
    value = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank == 'A':
            aces += 1
        else:
            value += CARD_VALUES[rank]
    
    # Add aces
    for _ in range(aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
    
    return value

def display_hand(hand: List[Tuple[str, str]], hide_first: bool = False) -> str:
    """
    Creates a string representation of a hand of cards.
    
    Args:
        hand: List of (rank, suit) tuples representing cards
        hide_first: If True, shows the first card as hidden
        
    Returns:
        str: String representation of the hand with cards separated by spaces
    """
    cards = []
    for i, (rank, suit) in enumerate(hand):
        if i == 0 and hide_first:
            cards.append('🂠')  # Hidden card
        else:
            cards.append(f"{rank}{suit}")
    return ' '.join(cards)

def play_blackjack() -> None:
    """
    Runs an interactive game of Blackjack.
    
    The game follows standard casino rules:
    - Dealer must hit on 16 and stand on 17
    - Aces are worth 1 or 11
    - Face cards are worth 10
    """
    print("\nWelcome to Blackjack!")
    print("Try to get as close to 21 as possible without going over.")
    
    # Initialize deck and shuffle
    deck = create_deck()
    random.shuffle(deck)
    
    # Deal initial cards
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    while True:
        # Show hands
        print(f"\nDealer's hand: {display_hand(dealer_hand, hide_first=True)}")
        print(f"Your hand: {display_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})")
        
        # Player's turn
        if calculate_hand_value(player_hand) == 21:
            print("Blackjack! You win!")
            return
        
        while calculate_hand_value(player_hand) < 21:
            action = input("\nWould you like to (H)it or (S)tand? ").strip().upper()
            if action == 'H':
                player_hand.append(deck.pop())
                print(f"\nYour hand: {display_hand(player_hand)} (Value: {calculate_hand_value(player_hand)})")
                if calculate_hand_value(player_hand) > 21:
                    print("Bust! You lose!")
                    return
            elif action == 'S':
                break
        
        if calculate_hand_value(player_hand) <= 21:
            # Dealer's turn
            print(f"\nDealer's full hand: {display_hand(dealer_hand)}")
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
                print(f"Dealer hits: {display_hand(dealer_hand)}")
            
            dealer_value = calculate_hand_value(dealer_hand)
            player_value = calculate_hand_value(player_hand)
            
            print(f"\nDealer's final hand: {display_hand(dealer_hand)} (Value: {dealer_value})")
            print(f"Your final hand: {display_hand(player_hand)} (Value: {player_value})")
            
            if dealer_value > 21:
                print("Dealer busts! You win!")
            elif dealer_value > player_value:
                print("Dealer wins!")
            elif dealer_value < player_value:
                print("You win!")
            else:
                print("It's a tie!")
        return

# ============================================================================
# NEWS HEADLINE RELATED FUNCTIONS
# ============================================================================

def generate_unique_headline() -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Generates a unique fake news headline with news outlet and timestamp.
    
    Combines random subjects, actions, and places to create unique headlines.
    Makes 50 random attempts before falling back to deterministic generation.
    
    Returns:
        Tuple containing (headline, news outlet, timestamp)
        or (None, None, None) when all possibilities are exhausted
    """
    for _ in range(50):
        subject = random.choice(subjects)
        action = random.choice(actions)
        place = random.choice(places)
        outlet = random.choice(news_outlets)

        # Get current date and time
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%B %d, %Y at %I:%M %p")

        headline = f'BREAKING NEWS : {subject} {action} {place}'
        if headline not in seen_headlines:
            return headline, outlet, formatted_datetime

    # Fallback: enumerate deterministically to find the next unseen combo
    for s in subjects:
        for a in actions:
            for p in places:
                headline = f'BREAKING NEWS : {s} {a} {p}'
                if headline not in seen_headlines:
                    outlet = random.choice(news_outlets)
                    current_datetime = datetime.now()
                    formatted_datetime = current_datetime.strftime("%B %d, %Y at %I:%M %p")
                    return headline, outlet, formatted_datetime

    return None, None, None

# ============================================================================
# HOROSCOPE RELATED FUNCTIONS
# ============================================================================

def generate_unique_horoscope_for_sign(user_sign: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Generates a unique horoscope for the given zodiac sign.
    
    Args:
        user_sign: The zodiac sign to generate a horoscope for
        
    Returns:
        Tuple containing (horoscope string, sign, prediction) or (None, None, None) if exhausted
    """
    # Only generate horoscopes for the user's sign
    for _ in range(50):
        prediction = random.choice(predictions)
        horoscope = f"{user_sign}: {prediction}"
        if horoscope not in seen_horoscopes:
            return horoscope, user_sign, prediction

    # Fallback: enumerate deterministically to find the next unseen combo
    for p in predictions:
        horoscope = f"{user_sign}: {p}"
        if horoscope not in seen_horoscopes:
            return horoscope, user_sign, p

    return None, None, None

# ============================================================================
# MATH PROBLEM RELATED FUNCTIONS
# ============================================================================

def generate_unique_math_problem() -> Tuple[Optional[str], Optional[str], Optional[int], Optional[int]]:
    """
    Generate a simple arithmetic problem not seen before.
    
    Supports operations:
    - Addition (+): Numbers 0-50
    - Subtraction (-): Ensures non-negative results
    - Multiplication (*): Numbers 0-12
    - Division (/): Ensures integer results
    
    Returns:
        Tuple containing (problem string, operator, first number, second number)
        or (None, None, None, None) when all possibilities are exhausted
    """
    ops = ['+', '-', '*', '/']
    # Try random attempts first
    for _ in range(200):
        op = random.choice(ops)
        if op == '+':
            a = random.randint(0, 50)
            b = random.randint(0, 50)
        elif op == '-':
            a = random.randint(0, 50)
            b = random.randint(0, a)  # ensure non-negative result
        elif op == '*':
            a = random.randint(0, 12)
            b = random.randint(0, 12)
        else:  # division, ensure integer result and non-zero divisor
            b = random.randint(1, 12)
            q = random.randint(0, 12)
            a = b * q

        problem = f"{a} {op} {b}"
        if problem not in seen_math_problems:
            return problem, op, a, b

    # Fallback: deterministic enumeration
    for op in ops:
        if op == '+':
            for a in range(0, 51):
                for b in range(0, 51):
                    problem = f"{a} + {b}"
                    if problem not in seen_math_problems:
                        return problem, '+', a, b
        if op == '-':
            for a in range(0, 51):
                for b in range(0, a+1):
                    problem = f"{a} - {b}"
                    if problem not in seen_math_problems:
                        return problem, '-', a, b
        if op == '*':
            for a in range(0, 13):
                for b in range(0, 13):
                    problem = f"{a} * {b}"
                    if problem not in seen_math_problems:
                        return problem, '*', a, b
        if op == '/':
            for b in range(1, 13):
                for q in range(0, 13):
                    a = b * q
                    problem = f"{a} / {b}"
                    if problem not in seen_math_problems:
                        return problem, '/', a, b

    return None, None, None, None

# ============================================================================
# MAIN PROGRAM LOOP
# ============================================================================

def main():
    """
    Main program loop that handles user interaction and function selection.
    Provides access to all entertainment functions and manages program flow.
    """
    while True:
        print("\nWhat would you like to do?")
        print("1. Generate a fake news headline")
        print("2. Get a daily horoscope")
        print("3. Solve a math problem")
        print("4. Play Blackjack")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ").strip()
        
        if choice == '1':
            if len(seen_headlines) >= total_headlines:
                print("\nNo more unique headlines available. You've seen them all!")
                continue
            
            result = generate_unique_headline()
            if result[0] is None:
                print("\nNo more unique headlines available. You've seen them all!")
                continue
            
            headline, outlet, datetime_str = result
            seen_headlines.add(headline)
            print(f'\n{"-" * 60}')
            print(f'{outlet}')
            print(f'{datetime_str}')
            print(f'{headline}')
            print(f'{"-" * 60}')
            
        elif choice == '2':
            print("\nChoose your zodiac sign:")
            for idx, sign in enumerate(signs, 1):
                print(f"{idx}. {sign}")
            sign_choice = input("\nEnter the number for your sign: ").strip()
            
            try:
                sign_idx = int(sign_choice) - 1
                if 0 <= sign_idx < len(signs):
                    user_sign = signs[sign_idx]
                else:
                    print("Invalid sign selection.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            user_seen = [h for h in seen_horoscopes if h.startswith(f"{user_sign}:")]
            if len(user_seen) >= len(predictions):
                print(f"\nNo more unique horoscopes available for {user_sign}. You've seen them all!")
                continue
            
            result = generate_unique_horoscope_for_sign(user_sign)
            if result[0] is None:
                print(f"\nNo more unique horoscopes available for {user_sign}. You've seen them all!")
                continue
            
            horoscope, sign, prediction = result
            seen_horoscopes.add(horoscope)
            print(f'\n{"-" * 60}')
            print(f'Your Daily Horoscope for {sign}:')
            print(f'{prediction}')
            print(f'{"-" * 60}')
            
        elif choice == '3':
            result = generate_unique_math_problem()
            if result[0] is None:
                print("\nNo more unique math problems available. You've seen them all!")
                continue
            
            problem, op, a, b = result
            seen_math_problems.add(problem)
            print(f'\n{"-" * 60}')
            print(f'Solve: {problem}')
            print("Type 'skip' to skip this problem.")
            
            while True:
                answer = input("Your answer: ").strip()
                if answer.lower() == 'skip':
                    print("Problem skipped.")
                    break
                
                try:
                    if op == '+':
                        correct = a + b
                    elif op == '-':
                        correct = a - b
                    elif op == '*':
                        correct = a * b
                    else:  # '/'
                        correct = a / b
                    
                    user_val = float(answer) if ('.' in answer or op == '/') else int(answer)
                except ValueError:
                    print("Invalid input. Enter a number or 'skip'.")
                    continue
                
                if op == '/':
                    if abs(user_val - correct) < 1e-6:
                        print("Correct!")
                    else:
                        print(f"Incorrect. The correct answer is {correct}.")
                    break
                else:
                    if user_val == correct:
                        print("Correct!")
                    else:
                        print(f"Incorrect. The correct answer is {correct}.")
                    break
            print(f'{"-" * 60}')
            
        elif choice == '4':
            play_blackjack()
            
        elif choice == '5':
            print("Goodbye!")
            return
            
        else:
            print("Error: Please enter 1, 2, 3, 4, or 5.")

# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()