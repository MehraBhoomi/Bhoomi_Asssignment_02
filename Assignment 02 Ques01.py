# Assignment No. 02

# Que no. 01]  Write a Python program to get a list, sorted in increasing order by the last element
#              in each tuple from a given list of non-empty tuples

#              Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#              Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# Solution:- 

L1 = [(2,5), (1,2), (4,4), (2,3), (2,1)]

def sort_keys(t):
    return t[1]

print("Sample List: ", L1)
print("Sorted List: ", sorted(L1, key=sort_keys))
