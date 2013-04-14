def RadixSort(A):
	m = max(A)
	d = len(str(m))
	D = [None] * len(A)
	B = [None] * len(A)
	for i in range(0, len(A)):
		D[i] = []
		s = list(str(A[i]))
		for j in reversed(range(0, len(s))):
			D[i].append(s[j])
		for j in range(len(s), d):
			D[i].append('0')
	for j in range(0, d):
		C = [0] * 10
		E = [None] * len(D)
		for i in range(0, len(D)):
			C[int(D[i][j])] += 1
		C[0] -= 1
		for i in range(1, len(C)):
			C[i] += C[i-1]
		for i in reversed(range(0, len(D))):
			E[C[int(D[i][j])]] = D[i]
			C[int(D[i][j])] -= 1
		D = E
	for i in range(0, len(D)):
		B[i] = int(''.join(reversed(D[i])))
	return B


if __name__=="__main__":
	a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
	print(a)
	a = RadixSort(a)
	print(a)