my_set={1,2,3,4,5}
print(my_set)
my_set.add(6)# Add an element to the set
print(my_set)
my_set.update([7, 8, 9])# Add multiple elements to the set
print(my_set)   
#remove an element from the set. If the element is not found, it raises a KeyError.
my_set.remove(3)
print(my_set)   
my_set.discard(5) # Remove an element from the set. 
#If the element is not found, it does nothing.
print(my_set)

