# def main():
#     print("Hello from python-visualized!")


# if __name__ == "__main__":
#     main()

import json


def greet(name):
    """Greet a user"""
    return f"Hello, {name}!"


def calculate_average(numbers):
    """Calculate average of list of numbers"""
    sum = 0
    for n in numbers:
        sum += n
    return sum / len(numbers)


def parse_json_file(filename):
    """Parse a json file"""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except:
        return None


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(greet("Abhineel"))
    print(calculate_average(numbers))
