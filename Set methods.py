""""""
"""
Features of Set
Syntax - {}
1.Set is an important data types in python
2.While giving elements in a set use a comma(,) as a seprator
4.Set is mutable data types
    Mutable - Values can be updated 
    Immutable - Values cannot be updated
5.Accepts all types of Data 
    Homogenous - Can only store single type of data 
    Hetrogenous - Can store more than one type of data
6.Background Data Structure of Set is - Hash Table
7.Indexing & Slicing not supported
8.Sequence order is not preserved
9.Duplicates are not allowed
10.There are many method in Set like ...
"""
s1 = {10,20,30,40}
s2 = {30,40,50,60,70}
#1. Union = Combines elements of both sets
print(s1.union(s2)) #Output is temporary
print(id(s1))
print(id(s2))
#if we want changes in s1 itself, means we should first do the union and save the result in first set
#2.Update -
s1.update(s2) #Set is mutable
print(s1) #Changes persist in same object
print(id(s1)) #Id is also same
#3.Intersection - Common elements from both set
print(s1)
print(s2)
print(s1.intersection(s2))
print(s2.intersection(s1))
#4.Intersection_update - In order to save the changes in any one set use intersection_update
s1.intersection_update(s2) #First to intersection and then save changes
print(s1)
print(id(s1)) #Id is same
#5.Difference  - Uncommon element from first set
s3 = {1,2,3,4,5,6}
s4 = {5,6,7,8,9,10}
print(s3.difference(s4))
print(s4.difference(s3))
print(id(s3))
#6.Difference_update - If changes needs to store permanently use difference_update
s3.difference_update(s4) #Set is mutable
print(s3)
print(id(s3)) #Id is also same
#7.Symmetric_Difference - Uncommon elements from both sets use symmetric_differnce
print(s3.symmetric_difference(s4))
#8.Symmetric_Difference_Update
s3.symmetric_difference_update(s4) #Set is Mutable
print(s3)
print(id(s3)) #Id is also same
#9.Pop - Remove elements from set
s3.pop()
print(s3)
#takes no arguments (no index, no value) (Output - TypeError)
#its empty pop() because it removes arbitrary elements
#Pop() over empty set (Output - KeyError: pop from an empty set)
#10.Clear - Removes all the elements
s1.clear()
print(s1)
#Clear() on empty set has no effect
#11.Remove - Removes specified elements from set
#Remove() takes only 1 argument
print(s3)
s3.remove(7)
print(s3)
#If we try to remove the element which is not present in set (Output - KeyError)
a = {1,2,3,4,5,6}
b = {4,5,6}
c = {10,20,30}

#Boolean Output Methods
#12.Isdisjoint - No Common elements
print(b.isdisjoint(a))
print(c.isdisjoint(a))
#13.Issubset - Checks whether one set is subset of another set
print(b.issubset(a))
#14.Issuperset - Checks whether one set is superset of another set
print(a.issuperset(b))

#-------------------------------------------------------------------------------------

#Frozen Set - Immutable set
k = [10,20,30,10,20]
print(k)
print(frozenset()) #Empty Frozen Set
print(frozenset(k)) #Supply iterables in it
print(frozenset('amitabh'))
#Difference between Set and Frozenset
#1.Mutability - Set is Mutable,
# Frozen Set is Immutable(once frozenset is created, its elements cannot be changed
#2.Hashability - Set is not hashable because it is mutable and its value changes when its element changes,
# Frozen Set is hashable because it is immutable and can be used as a dictionary key or as an element in another set
#3.Creation - Set is created using curly braces {} or the set(),
#Frozen Set is created by using frozen()
#4.Methods - Set provides methods to add,remove and modify
#Frozen Set only provides methods to access its elements
