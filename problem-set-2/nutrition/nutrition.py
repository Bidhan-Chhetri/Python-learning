fruit_calories = {
    "apple": 52,
    "banana": 105,
    "grapes": 62,
    "strawberries": 49,
    "orange": 62,
    "watermelon": 85,
    "pineapple": 82,
    "blueberries": 84,
    "peach": 59,
    "pear": 96,
    "cherries": 77,
    "mango": 99,
    "kiwifruit": 42,
    "plums": 76,
    "nectarines": 67,
    "cantaloupe": 53,
    "papaya": 59,
    "raspberries": 64,
    "blackberries": 43,
    "honeydew melon": 61
}

def main(): 
    fruits = input("Items: ").lower()
    if fruits in fruit_calories:
            print(f"Calories: {fruit_calories[fruits]}")

main()