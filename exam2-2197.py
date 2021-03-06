# -*- coding: utf-8 -*-
##### 0 #####

def count_elements(xss):
	counter = 0
	for x in xss:
		if isinstance(x,list):
			counter += count_elements(x)
		else:
			counter += 1
	return counter

# TEST CASES
# print(count_elements([]))
# print(count_elements([1,2,2]))
# print(count_elements([1,[2],2]))
# print(count_elements([1,[1,2,[1,4]]]))
# print(count_elements([[[[[[[],[[3,2,3]],3]]]]]]))
# print(count_elements([[[[3]],[3]],5,3,[7]]))
# print(count_elements([1,[5,2],[[3],[5,4]],[[[5,5,5,5]]],6,[5,[[5],[[9]]]]]))

# RESULTS
# 0
# 3
# 3
# 5
# 4
# 5
# 14

##### 1 #####

def flatten(xss):
	flat = []
	size = len(xss)
	if isinstance(xss, list):
		for x in xss:
			if isinstance(x, list):
					flat.append(x)
	return flat

# TEST CASES
#print(flatten([])) 
#print(flatten([1,2,3])) 
#print(flatten([1,[],3])) 
#print(flatten([1,[1,2,[3,4]]])) 
#print(flatten([[[[[[[[1,2,3]]]]]]]])) 
#print(flatten([[[[3]],[4]],5,6,[7]])) 
#print(flatten([1,[2,2],[[3],[4,4]],[[[5,5,5,5]]],6,[7,[[8],[[9]]]]]))

# RESULTS
# []
# [1, 2, 3]
# [1, 3]
# [1, 1, 2, 3, 4]
# [1, 2, 3]
# [3, 4, 5, 6, 7]
# [1, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9]

#### 2 ####

def identity(mat):
	size = len(mat)
	for i in range(size):
		for j in range(size):
			if not (mat[0][0]==1 and mat[1][1]==1 and mat[2][2]==1 and mat[3][3] ==1):
				return False
	return True

xs0 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
xs1 = [[1,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,1]]
xs2 = [[0,-3,6,4],[3,0,-9,8],[-6,9,0,2],[-4,-8,-2,0]]
xs3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# TEST CASES
#print(identity(xs0))
#print(identity(xs1))
#print(identity(xs2))
#print(identity(xs3))

# RESULTS
# True
# False
# False
# False

##### 3 #####

def ascii_art(n):
	for i in range(n):
		for j in range(n):
			print('#', end=' ')
		print()

# TEST CASE
#ascii_art(5)

## (1) ## +
def ascii_art_cross(n):
	for i in range(n):
		for j in range(n):
			if i==2 or j==2:
				print('#', end=' ')
			else:
				print(' ', end=' ')
		print()

# TEST CASE
#ascii_art_cross(5)

## (2) ## X
def ascii_art_X(n):
	for i in range(n):
		for j in range(n):
			if i<=n-j-1 and i>=n-j-1 or i<=j and i>=j: # fill your logical expression code here
				print('#', end=' ')
			else:
				print(' ', end=' ')
		print()

# TEST CASE
#ascii_art_X(5)

## (3) ## ☐
def ascii_art_square(n):
	for i in range(n):
		for j in range(n):
			if (i<=n-j-1 and i<=j and i==0) or \
			(i==1 and j==0) or\
			(i==2 and j==0) or\
			(i==3 and j==0) or\
			(i==4 and j==0) or\
			(i==1 and j==4) or\
			(i==2 and j==4) or\
			(i==3 and j==4) or\
			(i==4 and j==4) or\
			(i>=n-j-1 and i>=j and i==4): # fill your logical expression code here
				print('#', end=' ')
			else:
				print(' ', end=' ')
		print()

# TEST CASE
#ascii_art_square(5)

## (4) ## 
def ascii_art_diamond(n):
	mid = n // 2
	for i in range(n):
		for j in range(n):
			if (i==0 and j==2)or\
			(i==1 and (j==1 or j==3))or\
			(i==2 and (j==0 or j==4))or\
			(i==3 and (j==1 or j==3))or\
			(i==4 and j==2): # fill your logical expression code here
				print('#', end=' ')
			else:
				print(' ', end=' ')
		print()

# TEST CASE
#ascii_art_diamond(5)


##### 4 #####
## (1) ##
def substrings_of_length(k,s):
	if k == 0:
		return ['']
	elif 0 < k <= len(s):
		subs = []
		for k in s:
			a=k[:]
			if len(s)==k:
				subs.append(k)
		return subs
	else:
		return None

# TEST CASES
#print(substrings_of_length(0,"ERICA"))
#print(substrings_of_length(1,"ERICA"))
#print(substrings_of_length(2,"ERICA"))
#print(substrings_of_length(3,"ERICA"))
#print(substrings_of_length(4,"ERICA"))
#print(substrings_of_length(5,"ERICA"))
#print(substrings_of_length(6,"ERICA"))

# RESULTS
# ['']
# ['E', 'R', 'I', 'C', 'A']
# ['ER', 'RI', 'IC', 'CA']
# ['ERI', 'RIC', 'ICA']
# ['ERIC', 'RICA']
# ['ERICA']
# None

## (2) ##
def substrings(s):
	subs = ['']
	pass  # fill your for-loop code here
	return subs

# TEST CASES
# print(substrings("ERICA"))
# print(substrings(""))

# RESULTS
# ['', 'E', 'R', 'I', 'C', 'A', 'ER', 'RI', 'IC', 'CA', 'ERI', 'RIC', 'ICA', 'ERIC', 'RICA', 'ERICA']
# ['']


##### 5 #####
## (1) ##
def longest_ascending_sublist(ns):
	if ns != []:
		longest = []
		current = [ns[0]]
		if len(ns)<2:
			return len(ns)
		else:
			subs = longest_ascending_sublist(ns)
			for sub in subs:
				lenth = len(sub)
				if length>longest and increasing(sub):
					longest = length
		return longest
	else:
		return []

# TEST CASES
#print(longest_ascending_sublist([1,5,3,4,8,2,3,5]))
#print(longest_ascending_sublist([]))
#sample = [59, 4, 38, 54, 33, 75, 19, 73, 49, 7, 86, 28, 54, 13, 6, 42, 97, 84, 26, 69, 86, 14, 79, 27, 68, 57, 35, 53, 92, 58, 68, 49, 93, 28, 31, 63, 51, 1, 44, 62, 14, 40, 53, 40, 5, 69, 81, 95, 58, 55, 90, 56, 91, 40, 55, 14, 65, 28, 37, 61, 66, 89, 26, 63, 98, 59, 7, 23, 34, 67, 77, 30, 49, 55, 31, 58, 10, 27, 15, 45, 42, 77, 11, 14, 9, 55, 88, 44, 53, 12, 54, 95, 25, 91, 29, 8, 25, 90, 34, 55]
#print(longest_ascending_sublist(sample))

# RESULTS
# [3, 4, 8]
# []
# [28, 37, 61, 66, 89]

## (2) ##
def longest_steepest_ascending_sublist(ns):
	def slope(ns):
		return (ns[-1] - ns[0]) / len(ns)
	if ns != []:
		longest = []
		steepest = 0
		current = [ns[0]]
		pass  # fill your for-loop code here
		return longest
	else:
		return []

# TEST CASES
# print(longest_steepest_ascending_sublist([1,5,3,4,8,2,3,5]))
# print(longest_steepest_ascending_sublist([]))
# sample = [59, 4, 38, 54, 33, 75, 19, 73, 49, 7, 86, 28, 54, 13, 6, 42, 97, 84, 26, 69, 86, 14, 79, 27, 68, 57, 35, 53, 92, 58, 68, 49, 93, 28, 31, 63, 51, 1, 44, 62, 14, 40, 53, 40, 5, 69, 81, 95, 58, 55, 90, 56, 91, 40, 55, 14, 65, 28, 37, 61, 66, 89, 26, 63, 98, 59, 7, 23, 34, 67, 77, 30, 49, 55, 31, 58, 10, 27, 15, 45, 42, 77, 11, 14, 9, 55, 88, 44, 53, 12, 54, 95, 25, 91, 29, 8, 25, 90, 34, 55]
# print(longest_steepest_ascending_sublist(sample))

# RESULTS
# [3, 4, 8]
# []
# [7, 23, 34, 67, 77]

