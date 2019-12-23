# 1a. Write Python code to do the following:
# i. Create list with inputs from user
#ii. Determine minimum and maximum elements in the list
#iii. Insert new element into the list
#iv. Delete an element from the list
#v. Determine if an element is present in the list.

a=list(map(int,input("Enter the list ").split(" ")))
print(a);
print(max(a))
print(min(a))
a.append(int(input("Enter the element to insert ")));
print(a);
a.remove(int(input("Enter the element to remove ")));
print(a);


b = int(input("Enter element to search"));

if b in a:
    print("Element found");
else:
    print("Element not found");


