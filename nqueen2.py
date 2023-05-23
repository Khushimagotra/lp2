class NQueens:
    def __init__(self, n):
        self.n = n
        self.columns = [-1] * n
        self.diagonal1 = [-1] * (2 * n - 1)
        self.diagonal2 = [-1] * (2 * n - 1)
        self.solutions = []

    def is_safe(self, row, col):
        for i in range(row):
            if (
                self.columns[i] == col
                or self.diagonal1[row + col] == 1
                or self.diagonal2[row - col + self.n - 1] == 1
            ):
                return False
        return True

    def solve(self, row=0):
        if row == self.n:
            solution = []
            for i in range(self.n):
                col = self.columns[i]
                solution.append([i, col])
            self.solutions.append(solution)
            return True

        found_solution = False
        for col in range(self.n):
            if self.is_safe(row, col):
                self.columns[row] = col
                self.diagonal1[row + col] = 1
                self.diagonal2[row - col + self.n - 1] = 1

                if self.solve(row + 1):
                    found_solution = True

                self.columns[row] = -1
                self.diagonal1[row + col] = -1
                self.diagonal2[row - col + self.n - 1] = -1

        return found_solution

    def find_solutions(self):
        self.solve()
        return self.solutions


# Example usage for N-Queens problem
n = int(input("Enter the number of queens: "))
queens = NQueens(n)
solutions = queens.find_solutions()

print(f"Number of solutions: {len(solutions)}")
for solution in solutions:
    print(solution)
