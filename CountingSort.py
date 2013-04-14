def CountingSort(A):
	C = [0] * (max(A)+1)
	B = [None] * len(A)
	for i in range(0, len(A)):
		C[A[i]] += 1
	C[0] -= 1
	for i in range(1, len(C)):
		C[i] += C[i-1]
	for i in reversed(range(0, len(A))):
		B[C[A[i]]] = A[i]
		C[A[i]] -= 1
	return B
	
if __name__=="__main__":
	a = [4, 1, 3, 4, 3]
	print(a)
	a = CountingSort(a)
	print(a)
	b = [4, 1, 3, 2, 0, 16, 9, 10, 14, 8, 7]
	print(b)
	b = CountingSort(b)
	print(b)