def Parent(i):
		return round(i/2-0.6)
	
def Left(i):
		return (i*2+1)
	
def Right(i):
		return (i*2+2)
		
def HeapProperty(A):
	for i in reversed(range(0, len(A))):
		if A[i] > A[Right(i)] or A[i] > A[Left(i)] or i == 0:
			break
	return i
		
def Heapify(A,i,n):
	l = Left(i)
	r = Right(i)
	smallest = l if l < n and A[l] < A[i] else i
	smallest = r if r < n and A[r] < A[smallest] else smallest
	if smallest != i:
		A[smallest], A[i] = A[i], A[smallest]
		Heapify(A,smallest,n)
		
def BuildHeap(A):
	for i in reversed(range(0, int(len(A)/2))):
		Heapify(A,i,len(A))
		
def HeapSort(A):
	BuildHeap(A)
	n = len(A)
	for i in reversed(range(1,n)):
		A[0], A[i] = A[i], A[0]
		n -= 1
		Heapify(A,0,n)
		
if __name__ == "__main__":
	a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
	print(a)
	HeapSort(a)
	print(a)