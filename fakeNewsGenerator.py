
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


# Precompute the total possible unique combinations
total_headlines = len(subjects) * len(actions) * len(places)
total_horoscopes = len(signs) * len(predictions)


seen_horoscopes = set()
seen_headlines = set()
seen_math_problems = set()

def generate_unique_horoscope_for_sign(user_sign):
    # Only generate horoscopes for the user's sign
    for _ in range(50):
        prediction = random.choice(predictions)
        horoscope = f"{user_sign}: {prediction}"
        if horoscope not in seen_horoscopes:
            return horoscope, user_sign, prediction

    # Fallback: enumerate deterministically to find the next unseen combo for this sign
    for p in predictions:
        horoscope = f"{user_sign}: {p}"
        if horoscope not in seen_horoscopes:
            return horoscope, user_sign, p

    return None, None, None

def generate_unique_math_problem():
    '''
    Generate a simple arithmetic problem not seen before.

    Supports +, -, *, / (with integer result). Returns (problem_str, op, a, b)
    or (None, None, None, None) when exhausted.
    '''
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

def generate_unique_headline():
    '''Generate a headline not seen before; return None if exhausted.
       For simplicity, try a fixed number of random attempts first.
    '''
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

# Main interactive loop
while True:
    print("\nWhat would you like to do?")
    print("1. Generate a fake news headline")
    print("2. Get a daily horoscope")
    print("3. Solve a math problem")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ").strip()

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
        # Only count horoscopes for this sign
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
        # Math problem flow
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
                # Compute correct answer
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

            # Compare answers
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
        print("Goodbye!")
        break
    else:
        print("Error: Please enter 1, 2, 3, or 4.")

