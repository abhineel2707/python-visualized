shopping_list = ["milk", "sugar", "egg"]
numbers = [1, "Two", "Three", 4, 5.00]

print(shopping_list)
print(numbers)
print(shopping_list[0], shopping_list[1], shopping_list[2])

daily_txn = ("08-06-2026", "Swiggy", 120.00)
print(daily_txn)
print(daily_txn[0], daily_txn[1], daily_txn[2])

unique_vals = {10, 11, 19, 21, 45, 65, 78, 78, 78, 91, 11, 11, 19, 10, 10}
print(unique_vals)
match_scores = [10, 11, 19, 21, 45, 65, 78, 78, 78, 91, 11, 11, 19, 10, 10]
unique_match_scores = set(match_scores)
print(unique_match_scores)

my_details = {
    "name": "Abhineel Rai",
    "hometown": "Allahabad",
    "residing_in": "Bangalore",
}

print(my_details)

daily_learning = ("Day 1", ["One", 2, "Three", 4.0])
daily_learning[1][0] = "Updated One"
print(daily_learning)
