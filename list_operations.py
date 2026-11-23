"""Explore Python lists and nested lists with small food examples."""


def main():
    """Run the original list exercises in order."""
    fruits = ["apple", "banana", "orange", "mango"]
    print("Second and third fruits:", fruits[1], fruits[2])
    print("Last fruit:", fruits[-1])
    print("Number of fruits:", len(fruits))
    fruits.remove("orange")
    fruits[1] = "grapes"
    print("After removal and replacement:", fruits)
    fruits.append("pear")
    fruits.insert(2, "cherry")
    fruits.insert(3, "peach")
    print("After adding fruits:", fruits)
    print("Index of apple:", fruits.index("apple"))
    fruits.sort()
    print("Sorted fruits:", fruits)

    more_fruits = ["apple", "banana", "orange", "mango"]
    more_fruits.append("blackberry")
    print("Another list with an appended fruit:", more_fruits)

    food = ["rice", "beans"]
    food.append("broccoli")
    print("After append:", food)
    food.extend(["bread"])
    food.extend(["pizza"])
    print("After extend:", food)
    print("First two foods:", food[0:2])
    print("Index of rice:", food.index("rice"))

    matrix = [
        ["apple", "banana", "cherry"],
        ["date", "fig", "grape"],
        ["kiwi", "lemon", "mango"],
    ]
    print("Second row:", matrix[1])
    print("Third row, second item:", matrix[2][1])
    print("Third row, third item:", matrix[2][2])
    matrix[1][0] = "orange"
    print("Updated nested list:", matrix)


if __name__ == "__main__":
    main()
