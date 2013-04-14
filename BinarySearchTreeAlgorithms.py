from BinarySearchTree import *

def PreOrderTraversal(x):
	if x != None:
		print(x.key,end=' ')
		PreOrderTraversal(x.left)
		PreOrderTraversal(x.right)

def InOrderTraversal(x):
	if x != None:
		InOrderTraversal(x.left)
		print(x.key,end=' ')
		InOrderTraversal(x.right)

def PostOrderTraversal(x):
	if x != None:
		PostOrderTraversal(x.left)
		PostOrderTraversal(x.right)
		print(x.key,end=' ')
		
def InOrderTreeWalk(x):
	a = []
	if x != None:
		a += InOrderTreeWalk(x.left)
		a += [x.key]
		a += InOrderTreeWalk(x.right)
	return a
	
def TreeSort(A):
	T = BinarySearchTree()
	for i in range(0, len(A)):
		T.insert(A[i])
	return InOrderTreeWalk(T.root)

if __name__=="__main__":
	t = BinarySearchTree()
	print('empty: ' + str(t.isEmpty()))
	print('size: ' + str(t.size()))
	t.insert(11)
	t.insert(6)
	t.insert(19)
	t.insert(4)
	t.insert(8)
	t.insert(17)
	t.insert(43)
	t.insert(5)
	t.insert(10)
	t.insert(31)
	t.insert(49)
	print('')
	
	InOrderTraversal(t.root)
	print('')
	print('empty: ' + str(t.isEmpty()))
	print('size: ' + str(t.size()))
	
	print('sum: ' + str(t.sum()))
	print('min: ' + str(t.min()))
	print('max: ' + str(t.max()))
	print('root: ' + str(t.root))
	print('predecessor: ' + str(t.predecessor()))
	print('successor: ' + str(t.successor()))
	print('node: ' + str(t.search(17)))
	print('predecessor: ' + str(t.search(17).predecessor()))
	print('successor: ' + str(t.search(17).successor()))
	
	print('')
	t.delete(17)
	InOrderTraversal(t.root)
	print('')
	print('sum: ' + str(t.sum()))
	print('min: ' + str(t.min()))
	print('max: ' + str(t.max()))
	print('root: ' + str(t.root))
	print('predecessor: ' + str(t.predecessor()))
	print('successor: ' + str(t.successor()))
	print('search 17: ' + str(t.search(17)))
	print('node: ' + str(t.search(19)))
	print('predecessor: ' + str(t.search(19).predecessor()))
	print('successor: ' + str(t.search(19).successor()))
	
	print('')
	t.delete(4)
	InOrderTraversal(t.root)
	print('')
	print('sum: ' + str(t.sum()))
	print('min: ' + str(t.min()))
	print('max: ' + str(t.max()))
	print('root: ' + str(t.root))
	print('predecessor: ' + str(t.predecessor()))
	print('successor: ' + str(t.successor()))
	print('search 4: ' + str(t.search(4)))
	print('node: ' + str(t.search(6)))
	print('predecessor: ' + str(t.search(6).predecessor()))
	print('successor: ' + str(t.search(6).successor()))
	
	print('')
	t.delete(43)
	InOrderTraversal(t.root)
	print('')
	print('sum: ' + str(t.sum()))
	print('min: ' + str(t.min()))
	print('max: ' + str(t.max()))
	print('root: ' + str(t.root))
	print('predecessor: ' + str(t.predecessor()))
	print('successor: ' + str(t.successor()))
	print('search 43: ' + str(t.search(43)))
	print('node: ' + str(t.search(31)))
	print('predecessor: ' + str(t.search(31).predecessor()))
	print('successor: ' + str(t.search(31).successor()))
	
	print('')
	print('node: ' + str(t.search(49)))
	print('predecessor: ' + str(t.search(49).predecessor()))
	print('successor: ' + str(t.search(49).successor()))
	print('node: ' + str(t.search(5)))
	print('predecessor: ' + str(t.search(5).predecessor()))
	print('successor: ' + str(t.search(5).successor()))
	
	a = [49, 11, 31, 6, 4, 43, 5, 17, 19, 8, 10]
	print('\nTree Sort')
	print(a)
	print(TreeSort(a))
	