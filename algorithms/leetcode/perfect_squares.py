"""279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for
example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

  Input: n = 12
  Output: 3
  Explanation: 12 = 4 + 4 + 4.

Example 2:

  Input: n = 13
  Output: 2
  Explanation: 13 = 4 + 9.


https://leetcode.com/problems/perfect-squares/
"""
import math


class Solution:
    # Bottom-up iterative
    def numSquares_bottomup(self, n):
        if not n:
            return 1
        # Base case complete via initialization.
        num_squares = list(range(n+1))
        squares = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
        # Base case
        num_squares[0] = 0
        # Bottom-up iterative.
        for n2 in range(1, n + 1):
            for square in squares:
                if square > n2:
                    break
                num_squares[n2] = min(num_squares[n2],
                                      num_squares[n2 - square] + 1)
        return num_squares[-1]

    # Top-down recursive with memoization
    def numSquares_topdown(self, n):
        if not n:
            return 1
        # Base case complete via initialization.
        num_squares = [float('inf')] * (n + 1)
        squares = [i**2 for i in range(1, int(math.sqrt(n) + 1))]
        # Top-down recursive with memoization.
        def numSquaresRec(n):
            # Return memoized solution if available.
            if not n or num_squares[n]:
                return num_squares[n]
            # Otherwise, sollve for the subcases recursively.
            num = n
            for square in squares:
                if square > n:
                    break
                num = min(num, numSquaresRec(n-square) + 1)
            # Memoize the solution for future reuse.
            num_squares[n] = num
            return num
        return numSquaresRec(n)

    # External solution (DP solutions produce "Time Limit Exceeded")
    def numSquares_external(self, n):
        def isSquare(n):
            sq = int(math.sqrt(n))
            return sq*sq == n

        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2      # reducing the 4^k factor from number
        if (n & 7) == 7: # mod 8
            return 4

        if isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        for i in range(1, int(n**(0.5)) + 1):
            if isSquare(n - i*i):
                return 2
        # bottom case from the three-square theorem
        return 3

    def numSquares(self, n):
        return self.numSquares_external(n)


if __name__ == '__main__':
    solution = Solution()

    solution = Solution()
    cases = [12, 13]
    solutions = [3, 2]
    results = [solution.numSquares(n) for n in cases]
    print(results)
    assert(results == solutions)
