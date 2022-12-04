calories = {
    "pizza": 800,
    "oatmeal": 80,
    "bread": 100,
    "apple pie": 370,
    "veggie soup": 90,
    "sandwich": 150
}

total = 0
meal = ["oatmeal",  "bread"]

for item in meal:
    total += calories[item]

print(f"Total number of calories: {total}")