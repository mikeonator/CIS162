# Michael Audi - CIS162 Quiz Week 6 Hash Function

def hash_slinging_slasher(list_in: list):
    """
    definitely not a spongebob reference
    """
    name_list = []
    # make lists of hashes and names
    for name in list_in:
        name_list.append([hash(name), name])
    return name_list


def main():
    list_in = ["Bob", "Suzie", "Mary", "Trieste", "Bill",
               "James", "Dylan", "Michael", "Alice", "Deanna"]
    print(hash_slinging_slasher(list_in))


if __name__ == "__main__":
    main()
