################### Python Built in datastructures - Dictionary ###################

'''
Time and space complexity of creating a dictionary
The time complexity to create a dictionary is O(len(dict)), because when we create a dictionary,
the hash function has to calculate hash values for each element in the dictionary. The space complexity to create a dictionary is O(N).

Time and space complexity of accessing an element in a dictionary
The time complexity to access an element in a dictionary is O(1) and the space complexity is also O(1), as we are not using any additional memory to access the element.

Time and space complexity of modifying the value in a dictionary
The time complexity to change the value of the existing key is O(1), because we are just assigning the new value to a key. 
The space complexity is also O(1), as we are not using any extra space to modify the value of a key.

Time and space complexity of inserting a key-value pair in a dictionary
The time complexity to insert an element in a dictionary is O(1), but sometimes based on the hash function it takes amortized or O(N) time complexity. 
The space complexity for adding a key-value pair is O(1)

Time and space complexity of traversing a dictionary
The time complexity to traverse a dictionary is O(N), as we are iterating through each element one by one.
The space complexity is O(1) because we are not using any additional space.


Time and space complexity to search for a value in a Dictionary
The time complexity to search for a value in dict_1 is O(N), as the for loop iterates through all pairs of dictionaries one by one. 
The space complexity is O(1) because we are not using any additional space to search for a value.

Time and space complexity to remove an element from a dictionary
The time complexity to remove a key-value pair is O(1) in the average case, but it is O(N) in the amortized worst case. 
The space complexity is O(1) because we are not using any additional memory space.
'''
import datetime
print("Today's Date is :",datetime.datetime.now().date())

from termcolor import colored
print(colored("Python Built in datastructures - Dictionary",'red','on_yellow'))
my_dictionary = {'name':'vinil','age':'33'}
family = [{'name':'vinil','age':'33'},{'name':'anil','age':'312'}]
print("Accessing dictionary using key:\nSYNTAX : my_dictionary['age']\n",my_dictionary['age']) # Accessing dictionary using key
print("\n\n")
print("Accessing dictionary using get method: \nSYNTAX : my_dictionary.get('age')\n",my_dictionary.get('age')) # Accessing dictionary using get method
print("\n\n")
my_dictionary2 = {x :x**2 for x in range(0,5)}
print("Creating Dictionary using Dictionary comprehension:\nSYNTAX : {x :x**2 for x in range(0,5)} \n",my_dictionary2)
print("\n\n")
sorted_dict = sorted(family, key=lambda d: d['name'])
print("Sorting a dictionary :\nSYNTAX : sorted(family, key=lambda d: d['name']) \n",sorted_dict)
print("\n\n")
#
myDict= {}
myDict.update(dict.fromkeys(['a','b','c'],10))
print("Multiple KEY are mapped to same VALUES in a dictionary \nSYNTAX :  dict.fromkeys() method: \n",myDict)
print("\n\n")
#
myDict2 = {}
myDict2.update(dict.fromkeys(('f','d','e'),20))
print("Multiple KEY(TUPLE) are mapped to same VALUES in a dictionary \nSYNTAX :  dict.fromkeys() method: \n",myDict2)
print("\n\n")
# merge 2 dictionaries
z = {**myDict,**myDict2}
print("Merge 2 dictionaries \nSYNTAX - {**myDict,**myDict2}\n\n",z)
print("\n\n")
myDict['x'] = 30
print("Adding new KEY to an existing Dictionary:\n\n",myDict)
print("\n\n")
list1 = ['a','b','c']
list2 = [1,2,3]
new_dict2 = {k:v for k,v in zip(list2,list1)}
print("New dictionary from 2 lists using comprehension:\nSYNTAX - {k:v for k,v in zip(list2,list1)}\n",new_dict2)
print("\n\n")
new_dict = dict(zip(list1,list2))
print("New dictionary from 2 lists:\nSYNTAX - dict(zip(list1,list2))",new_dict)
print("\n\n")
min_dict = min(new_dict, key=new_dict.get)
print("Finding KEY which is having MINIMUM value in given dictionary:\nSYNTAX - min(new_dict, key=new_dict.get)\n",min_dict)
print("\n\n")
#delete a key in dictionary
'''
del d[k]
It is highly recommended to make a shallow copy of original dictionary as deleting in original dictionary will update it. 

def removekey(d,key):
    r = dict(d)
    del r[k]
    return r
'''
def removekey(d,key):
    _copyDict = d.copy()
    _copyDict.pop(key)
    return _copyDict

key_to_remove=2
remaining_dict = removekey(new_dict2,key_to_remove)
print("Remaining Elements:\n",remaining_dict)
print("\n\n")
print("Check if given KEY exist in dictionary \nSYNTAX - remaining_dict.__contains__(1): \n",remaining_dict.__contains__(1)) # check if given KEY exist in dictionary
print("\n\n")
tuple_from_dict = sum(remaining_dict.items(),())
print("Tuple made from Dictionary : \nSYNTAX - sum(remaining_dict.items(),()) :\n",tuple_from_dict)
# print("CLASS of tuple_from_dict:\n",type(tuple_from_dict))
print("\n\n")
print("List from a Dictionary : \nSYNTAX : list(myDict.items()) \n",list(myDict.items()))
print("\n\n")


print("Printing dictionary into CSV File using Pandas library")
import pandas as pd
pd.DataFrame(family).to_csv("family.csv", index=False)
print("\n\n")

#Python program to filter dict based on some criteria
ini_dict = {'a': 1, 'b': -3, 'c': 2, 'd': -6}
print("Initial Dictionary:", ini_dict)
result1 = dict((k, v) for k, v in ini_dict.items() if v >= 0)
print("Updated Dictionary using filter criteria if value > 0: -->", result1)
# Python program to filter dict based on some criteria c
result2 = dict(filter(lambda x: x[1] > 0, ini_dict.items()))
print("Updated Dictionary using Lambda Function: -->", result2)

