class Person:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def search_tree(person: Person, target_name: str):
    if person.name == target_name:
        return person
    for child in person.children:
        result = search_tree(child, target_name)
        if result is not None:
            return result
    return None


def ask_tree(person: Person, target_name: str):
    result = search_tree(person, target_name.capitalize())
    if result is not None:
        print(
            f"Yes, {result.name} was found and has {len(result.children)} children: ", end="")
        for child in result.children:
            print(child.name, end=", ")
    else:
        print(f"No, {target_name} was not found in the Family Tree.")


def main():

    alice = Person("Alice")
    bob = Person("Bob")
    carol = Person("Carol")
    daniel = Person("Daniel")
    emma = Person("Emma")
    frank = Person("Frank")

    alice.add_child(bob)
    alice.add_child(carol)
    bob.add_child(daniel)
    carol.add_child(emma)
    carol.add_child(frank)

    ask_tree(alice, input("Who do you wish to search the Family Tree for? "))


if __name__ == "__main__":
    main()
