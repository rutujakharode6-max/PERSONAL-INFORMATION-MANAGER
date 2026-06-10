import sys
# Ensure terminal output can handle beautiful emojis and box drawing characters
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
✨ Personal Information Manager ✨
Author: Your Name
Description: Beautiful info display with modern styling
"""

# === PERSONAL DATA STORAGE ===
name = "Maya Patel"
age = 22
city = "San Francisco"
hobby = "Coding"

# === WELCOME MESSAGE ===
print("\n")
print("  ╭─────────────────────────────────╮")
print("  │  ✨ WELCOME TO YOUR PROFILE ✨  │")
print("  ╰─────────────────────────────────╯")
print("\n")

# === INTERACTIVE INPUT ===
print("  Let's personalize your experience!\n")

favorite_food = input("  💚 What's your favorite food? › ").strip()
while len(favorite_food) == 0:
    print("  ⚠️  Oops! Please enter something.")
    favorite_food = input("  💚 What's your favorite food? › ").strip()

favorite_color = input("  💜 What's your favorite color? › ").strip()
while len(favorite_color) == 0:
    print("  ⚠️  Oops! Please enter something.")
    favorite_color = input("  💜 What's your favorite color? › ").strip()

# === DATA TRANSFORMATION ===
age_in_months = age * 12
formatted_food = favorite_food.title()
formatted_color = favorite_color.capitalize()

# === BEAUTIFUL OUTPUT ===
print("\n  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
print(f"      👤 {name}")
print(f"      🎂 {age} years old ({age_in_months} months)")
print(f"      🏙️  Lives in {city}")
print(f"      🎯 Enjoys {hobby}")
print(f"      🍽️  Loves {formatted_food}")
print(f"      🎨 Favorite color: {formatted_color}")
print("\n  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
print("  ✓ Profile updated successfully!")
print("  ✓ Have a wonderful day! 🌟\n")
