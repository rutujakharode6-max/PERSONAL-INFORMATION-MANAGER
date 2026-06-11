import sys

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

print("\n")
print("  ╭─────────────────────────────────╮")
print("  │  ✨ WELCOME TO YOUR PROFILE ✨  │")
print("  ╰─────────────────────────────────╯")
print("\n")

print("  Let's build your profile!\n")

name = input("  👤 What is your name? › ").strip().title()
while len(name) == 0:
    print("  ⚠️  Oops! Please enter your name.")
    name = input("  👤 What is your name? › ").strip().title()

while True:
    age_input = input("  🎂 How old are you? › ").strip()
    try:
        age = int(age_input)
        if age < 0:
            print("  ⚠️  Age cannot be negative.")
            continue
        break
    except ValueError:
        print("  ⚠️  Oops! Please enter a valid number.")

city = input("  🏙️  What city do you live in? › ").strip().title()
while len(city) == 0:
    print("  ⚠️  Oops! Please enter a city.")
    city = input("  🏙️  What city do you live in? › ").strip().title()

hobby = input("  🎯 What is your hobby? › ").strip().capitalize()
while len(hobby) == 0:
    print("  ⚠️  Oops! Please enter a hobby.")
    hobby = input("  🎯 What is your hobby? › ").strip().capitalize()

favorite_food = input("  💚 What's your favorite food? › ").strip().title()
while len(favorite_food) == 0:
    print("  ⚠️  Oops! Please enter something.")
    favorite_food = input("  💚 What's your favorite food? › ").strip().title()

favorite_color = input("  💜 What's your favorite color? › ").strip().capitalize()
while len(favorite_color) == 0:
    print("  ⚠️  Oops! Please enter something.")
    favorite_color = input("  💜 What's your favorite color? › ").strip().capitalize()

age_in_months = age * 12

print("\n  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
print(f"      👤 {name}")
print(f"      🎂 {age} years old ({age_in_months} months)")
print(f"      🏙️  Lives in {city}")
print(f"      🎯 Enjoys {hobby}")
print(f"      🍽️  Loves {favorite_food}")
print(f"      🎨 Favorite color: {favorite_color}")
print("\n  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
print("  ✓ Profile updated successfully!")
print("  ✓ Have a wonderful day! 🌟\n")
