import random

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
    'celebrates their Emmmy award'
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

# Precompute the total possible unique combinations
total_headlines = len(subjects) * len(actions) * len(places)

seen_headlines = set()

def generate_unique_headline():
    # Generate a headline not seen before; return None if exhausted."""
    # If we’re close to exhaustion, sampling might take longer; we can fall back to enumeration.
    # For simplicity, try a fixed number of random attempts first.
    for _ in range(50):
        subject = random.choice(subjects)
        action = random.choice(actions)
        place_or_thing = random.choice(places)
        headline = f'BREAKING NEWS : {subject} {action} {place_or_thing}'
        if headline not in seen_headlines:
            return headline

    # Fallback: enumerate deterministically to find the next unseen combo
    for s in subjects:
        for a in actions:
            for p in places:
                headline = f'BREAKING NEWS : {s} {a} {p}'
                if headline not in seen_headlines:
                    return headline

    return None

# Headline generation loop
while True:
    if len(seen_headlines) >= total_headlines:
        print("\nNo more unique headlines available. You've seen them all!")
        break

    headline = generate_unique_headline()
    if headline is None:
        print("\nNo more unique headlines available. You've seen them all!")
        break

    seen_headlines.add(headline)
    print('\n' + headline)

    user_input = input('\nDo you want another headline (yes/no)? ').strip().lower()
    if user_input == 'no':
        break

print("\nThank you and goodbye!")