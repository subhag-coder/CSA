class SET:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = set(elements)

    def is_member(self, element):
        return element in self.elements

    def powerset(self):
        from itertools import chain, combinations
        s = list(self.elements)
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

    def is_subset(self, other_set):
        return self.elements.issubset(other_set.elements)

    def union(self, other_set):
        return SET(self.elements.union(other_set.elements))

    def intersection(self, other_set):
        return SET(self.elements.intersection(other_set.elements))

    def complement(self, universal_set):
        return SET(universal_set.elements.difference(self.elements))

    def difference(self, other_set):
        return SET(self.elements.difference(other_set.elements))

    def symmetric_difference(self, other_set):
        return SET(self.elements.symmetric_difference(other_set.elements))

    def cartesian_product(self, other_set):
        return {(a, b) for a in self.elements for b in other_set.elements}

    def __str__(self):
        return "{" + ", ".join(map(str, self.elements)) + "}"


def menu():
    print("\n--- SET Operations Menu ---")
    print("1. Check membership")
    print("2. Power set")
    print("3. Subset check")
    print("4. Union")
    print("5. Intersection")
    print("6. Complement")
    print("7. Difference")
    print("8. Symmetric Difference")
    print("9. Cartesian Product")
    print("0. Exit")


if __name__ == "__main__":
    # Input universal set
    universal = SET(input("Enter elements of universal set (space separated): ").split())
    s1 = SET(input("Enter elements of Set 1 (space separated): ").split())
    s2 = SET(input("Enter elements of Set 2 (space separated): ").split())

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            elem = input("Enter element to check: ")
            print("Member:", s1.is_member(elem))
        elif choice == "2":
            print("Power set of Set 1:", s1.powerset())
        elif choice == "3":
            print("Set1 ⊆ Set2:", s1.is_subset(s2))
        elif choice == "4":
            print("Union:", s1.union(s2))
        elif choice == "5":
            print("Intersection:", s1.intersection(s2))
        elif choice == "6":
            print("Complement of Set1:", s1.complement(universal))
        elif choice == "7":
            print("Set1 - Set2:", s1.difference(s2))
        elif choice == "8":
            print("Symmetric Difference:", s1.symmetric_difference(s2))
        elif choice == "9":
            print("Cartesian Product:", s1.cartesian_product(s2))
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
