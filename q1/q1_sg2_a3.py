"""
Section: 9-Arayat Score:____________
C# / Name: #19 / Canto, Louise Audreana B. Date: 08/13/26
"""
import time
birth_year = int(input("Enter your birth year: "))
"""
Variable for you to be allowed to enter your birth year. It's in int form
because otherwise, it will not work for the equation in the next variable.
"""
year_calculation = (birth_year - 1900) % 12  # Determines the zodiac through math
# Since a zodiac recurs every 12 years, you can just divide it by 12.

# If statement to determine zodiac.
if birth_year < 1900:
    print("Invalid Year, it should be earlier than 1900.")
else:
    zodiacs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)",
    ]
    print(f"Your Chinese Zodiac sign is : {zodiacs[year_calculation]}")
    # The result will be printed here.
    time.sleep(1)
