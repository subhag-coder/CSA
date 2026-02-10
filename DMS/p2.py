class RELATION:
    def __init__(self, set_elements, matrix):
        """
        set_elements: list of elements in the set
        matrix: 2D list (adjacency matrix) representing relation
        """
        self.set_elements = set_elements
        self.matrix = matrix
        self.n = len(set_elements)

    def is_reflexive(self):
        for i in range(self.n):
            if self.matrix[i][i] != 1:
                return False
        return True

    def is_symmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def is_antisymmetric(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True

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


# Example usage
if __name__ == "__main__":
    elements = ['a', 'b', 'c']
    # Example relation matrix
    # Relation: {(a,a), (b,b), (c,c), (a,b), (b,a)}
    matrix = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]

    R = RELATION(elements, matrix)
    print("Relation type:", R.relation_type())
