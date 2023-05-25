# Loops
# O(n)
for i in range(100): # better to use xrange
	print i

# O(n^2)
for i in xrange(100):
	for j in xrange(100):
		print(i, j)
# input size required time complexity
# n ≤ 10 O(n!)
# n ≤ 20 O(2n)
# n ≤ 500 O(n3)
# n ≤ 5000 O(n2)
# n ≤ 106 O(nlogn) or O(n)
# n is large O(1) or O(logn)

# Maximum Subarray Sum
arr = [-1, 2, 4, -3, 5, 2, -5, 2]

# O(n^3) solution
best = 0
for i in arr:
	for j in arr:
		sum = 0
		for k in arr:
			sum += k
		best = max(best, sum)
print best

# O(n^2) solution
best = 0
for i in arr:
	sum = 0
	for j in arr:
		sum += j
		best = max(best, sum)
print best

# O(n) solution
best, sum = 0, 0
for i in arr:
	sum = max(i, sum + i)
	best = max(best, sum)
print best
