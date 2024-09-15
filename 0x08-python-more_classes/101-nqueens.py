#!/usr/bin/python3
"""
This module for task "10. N queens".
"""
import sys


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
inc = 2
if n % 2 == 0:
	for i in range(1, n - 1):
		sol = [[0, i]]
		while len(sol) != n:
			sol.append([sol[-1][0] + 1, (sol[-1][1] + inc) % (n + 1)])
		print(sol)
		inc += 1
else:
	while inc < n - 1:
		for i in range(n):
			sol = [[0, i]]
			while len(sol) != n:
				sol.append([sol[-1][0] + 1, (sol[-1][1] + inc) % n])
			print(sol)
		inc += 1
