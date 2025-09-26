
import random
from datetime import datetime

subjects = [
    'Donald Trump',
    'Vladimir Putin',
    'Barrack Obama',
    'Member of the FBI',
    'A group of Los Angelenos',
    'Bill Gates',
    'A dog named Spike'
]

actions = [
    'launches attack on rabies',
    'cancels tour',
    'fights a walrus',
    'eats worms',
    'declares war on spiders',
    'orders a bowl of cereal',
    'celebrates their Emmy award'
]

places = [
    'at Olive Garden',
    'in Grand Central Park',
    'on a Disney Cruise',
    'inside the White House',
    'at Coachella',
    'during a baseball game',
    'at the Grand Canyon'
]

news_outlets = [
    'CNN',
    'Fox News',
    'NBC News',
    'ABC News',
    'CBS News',
    'The New York Times',
    'The Washington Post',
    'USA Today',
    'Associated Press',
    'Reuters',
    'NPR',
    'Bloomberg',
    'The Wall Street Journal',
    'Politico',
    'BBC News America'
]

# Precompute the total possible unique combinations
total_headlines = len(subjects) * len(actions) * len(places)

seen_headlines = set()

def generate_unique_headline():
    # Generate a headline not seen before; return None if exhausted.
    # For simplicity, try a fixed number of random attempts first.
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

# Headline generation loop
while True:
    if len(seen_headlines) >= total_headlines:
        print("\nNo more unique headlines available. You've seen them all!")
        break

    result = generate_unique_headline()
    if result[0] is None:
        print("\nNo more unique headlines available. You've seen them all!")
        break
    
    headline, outlet, datetime_str = result
    seen_headlines.add(headline)
    
    # Display the news report
    print(f'\n{"-" * 60}')
    print(f'{outlet}')
    print(f'{datetime_str}')
    print(f'{headline}')
    print(f'{"-" * 60}')

    while True:  # Inner loop for input validation
        user_input = input('\nDo you want another headline (yes/no)? ').strip()
        
        if user_input in ['YES', 'Yes', 'yes', 'y', 'Y']:
            break  # Exit inner loop to generate another headline
        elif user_input in ['no', 'NO', 'No', 'n', 'N']:
            print("Goodbye!")
            exit()  # Exit the program
        else:
            print("Error: Please answer with yes or no.")
            # Continue the inner loop to ask again