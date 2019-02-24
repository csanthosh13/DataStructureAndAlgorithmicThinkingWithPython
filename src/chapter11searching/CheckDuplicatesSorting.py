# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def CheckDuplicatesSorting(A):
	A.sort()
	for i in range(0, len(A) - 1):
		if(A[i] == A[i + 1]):
			print("Duplicates exist:", A[i])
			return
	print("No duplicates in given array.")

A = [33, 2, 10, 20, 22, 32]
CheckDuplicatesSorting(A)
A = [3, 2, 1, 2, 2, 3]
CheckDuplicatesSorting(A)
