from random import randrange

def QuickSort(A,p,r):
	if p < r:
		x = A[randrange(p, r)]
		i = p
		j = r-1
		while i < j:
			A[i], A[j] = A[j], A[i]
			while A[j] > x:
				j -= 1
			while A[i] < x:
				i += 1
		QuickSort(A,p,j)
		QuickSort(A,j+1,r)
	
if __name__=="__main__":
	a = [17, 12, 6, 19, 23, 8, 5, 10]
	print(a)
	QuickSort(a,0,len(a))
	print(a)
	