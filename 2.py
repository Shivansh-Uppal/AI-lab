#1.	To create a set
#2.	Add members to the set
#3.	Remove element from set if element is present

#set function

a=set() #empty set

b=set([1,2,3,4,5,6,7,8,9,10]) #set with elements

c={1,2,3,4,5,6,7,8,9} #set with elements

#add function

a.add(1)
a.add(2)
a.add(3)
print("after adding elements in set a:\n", a)

b.add(11)
print("after adding elements in set b:\n", b)

c.add(10)
print("after adding elements in set c:\n", c)

#remove function

a.remove(1)
print("after removing elements in set a:\n", a)

b.discard(11)
print("after removing elements in set b:\n", b)

c.remove(10)
print("after removing elements in set c:\n", c)

#update

a.update([4,5,6])
print("after updating elements in set a:\n", a)

b.update([12,13,14])
print("after updating elements in set b:\n", b)

c.update([11,12,13])
print("after updating elements in set c:\n", c)

#theory
#1. A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
#2. To add one item to a set use the add() method.
#3. To add more than one item to a set use the update() method.
#4. To remove an item in a set, use the remove(), or the discard() method.
