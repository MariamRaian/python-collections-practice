"""Practice dictionary updates and list operations with example data."""


def main():
    """Run the contact, accessory, and number exercises."""
    # Deliberately non-dialable placeholders, not real phone numbers.
    contacts = {
        "ahmed": "PHONE_001",
        "nour": "PHONE_002",
        "omar": "PHONE_003",
        "mohamed": "PHONE_004",
    }
    print("Contacts:", contacts)
    print("Look up nour:", contacts["nour"])
    contacts["ahmed"] = "PHONE_005"
    contacts["rana"] = "PHONE_006"
    contacts.pop("omar")
    print("Contact items:", list(contacts.items()))
    print("Contact names:", list(contacts.keys()))
    print("Contact placeholders:", list(contacts.values()))
    print("Sorted contacts:", sorted(contacts.items()))
    contacts.clear()
    print("Cleared contacts:", contacts)

    accessories = {
        "mouse": 100,
        "keyboard": 200,
        "webcam": 300,
        "speaker": 400,
        "headphone": 500,
    }
    print("Accessories:", accessories)
    print("Webcam price:", accessories["webcam"])
    accessories["mouse"] = 250
    accessories["pad"] = 100
    accessories.pop("speaker")
    accessories["chair"], accessories["bag"] = 500, 400
    print("Accessory items:", list(accessories.items()))
    print("Accessory names:", list(accessories.keys()))
    print("Accessory prices:", list(accessories.values()))
    print("Sorted accessories:", sorted(accessories.items()))
    accessories.clear()
    print("Cleared accessories:", accessories)

    numbers = [1, 2, 3, 4, 5, 6, 7]
    print("Numbers:", numbers)
    print("Fourth number:", numbers[3])
    print("Last number:", numbers[-1])
    print("Slice from index four:", numbers[4:])
    extended_numbers = numbers + [8, 9, 10]
    print("Concatenated numbers:", extended_numbers)
    print("Count of seven:", extended_numbers.count(7))
    print("Index of five:", extended_numbers.index(5))
    extended_numbers[3] = "three"
    extended_numbers.append(11)
    extended_numbers.remove(6)
    print("After replacement, append, and removal:", extended_numbers)


if __name__ == "__main__":
    main()
