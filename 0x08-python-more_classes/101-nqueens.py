#!/usr/bin/python3
"""
This module for task "10. N queens".
"""
import sys


def areAttacking(q1, q2):
    if q1[0] == q2[0]:
        return 1
    if q1[1] == q2[1]:
        return 1
    return abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def isOk(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if areAttacking(queens[i], queens[j]):
                return 0
    return 1


def backtrack(sol, n):
    if len(sol) == n:
        print(sol)
        return
    for i in range(n):
        for j in range(n):
            if len(sol) == 0 or sol[-1][0] < i:
                sol.append([i, j])
                if isOk(sol):
                    backtrack(sol, n)
                sol.pop()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    arg = sys.argv[1]
    if not arg.isnumeric():
        print("N must be a number")
        sys.exit(1)
    n = int(arg)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    backtrack([], n)


if __name__ == "__main__":
    main()
