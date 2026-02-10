class RELATION:
    def __init__(self, set_elements, matrix):
        self.set_elements = set_elements
        self.matrix = matrix
        self.n = len(set_elements)

    def is_reflexive(self):
        return all(self.matrix[i][i] == 1 for i in range(self.n))

    def is_symmetric(self):
        return all(self.matrix[i][j] == self.matrix[j][i] for i in range(self.n) for j in range(self.n))

    def is_antisymmetric(self):
        return all(not (i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1) 
                   for i in range(self.n) for j in range(self.n))

    def is_transitive(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == 1:
                    for k in range(self.n):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            return False
        return True

    def relation_type(self):
        reflexive = self.is_reflexive()
        symmetric = self.is_symmetric()
        antisymmetric = self.is_antisymmetric()
        transitive = self.is_transitive()

        print(f"\nProperties:")
        print(f"Reflexive: {reflexive}")
        print(f"Symmetric: {symmetric}")
        print(f"Antisymmetric: {antisymmetric}")
        print(f"Transitive: {transitive}")

        if reflexive and symmetric and transitive:
            return "Equivalence Relation"
        elif reflexive and antisymmetric and transitive:
            return "Partial Order Relation"
        else:
            return "None"


def main():
    # Input set
    elements = input("Enter elements of the set (space separated): ").split()
    n = len(elements)

    print("\nEnter the relation matrix row by row (use 0 or 1):")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != n:
            print("Error: Each row must have", n, "entries.")
            return
        matrix.append(row)

    R = RELATION(elements, matrix)

    while True:
        print("\n--- Relation Menu ---")
        print("1. Check Reflexive")
        print("2. Check Symmetric")
        print("3. Check Antisymmetric")
        print("4. Check Transitive")
        print("5. Check Relation Type (Equivalence / Partial Order / None)")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Reflexive:", R.is_reflexive())
        elif choice == "2":
            print("Symmetric:", R.is_symmetric())
        elif choice == "3":
            print("Antisymmetric:", R.is_antisymmetric())
        elif choice == "4":
            print("Transitive:", R.is_transitive())
        elif choice == "5":
            print("Relation type:", R.relation_type())
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
