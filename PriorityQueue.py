from MaxBinaryHeap import *
		
def ExtractMax(A):
	A[0], A[len(A)-1] = A[len(A)-1], A[0]
	Heapify(A,0,len(A)-1)
	return A.pop()
	
def HeapInsert(A,key):
	A.append(key)
	i = len(A)-1
	while i > 0 and A[Parent(i)] < A[i]:
		A[Parent(i)], A[i] = A[i], A[Parent(i)]
		i = Parent(i)

if __name__=="__main__":
	a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
	print(a)
	BuildHeap(a)
	print(a)
	HeapInsert(a,17)
	print(a)
	print(ExtractMax(a))
	print(a)