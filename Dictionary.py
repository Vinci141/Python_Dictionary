################### Python Built in datastructures - Dictionary ###################

from termcolor import colored
print(colored("Python Built in datastructures - Dictionary",'red','on_yellow'))
my_dictionary = {'name':'vinil','age':'33'}
family = [{'name':'vinil','age':'33'},{'name':'anil','age':'312'}]
print("Accessing dictionary using key:",my_dictionary['age']) # Accessing dictionary using key
print("Accessing dictionary using get method:",my_dictionary.get('age')) # Accessing dictionary using get method

my_dictionary2 = {x :x**2 for x in range(0,5)}
print("Creating Dictionary using Dictionary comprehension:\n",my_dictionary2)

sorted_dict = sorted(family, key=lambda d: d['name'])
print("Sorting a dictionary :\n",sorted_dict)
#
myDict= {}
myDict.update(dict.fromkeys(['a','b','c'],10))
print("Multiple KEY are mapped to same VALUES in a dictionary using dict.fromkeys() method: \n",myDict)
#
myDict2 = {}
myDict2.update(dict.fromkeys(('f','d','e'),20))
print("Multiple KEY(TUPLE) are mapped to same VALUES in a dictionary using dict.fromkeys() method: \n",myDict2)

# merge 2 dictionaries
z = {**myDict,**myDict2}
print("Merge 2 dictionaries \n",z)

myDict['x'] = 30
print("Adding new KEY to an existing Dictionary:\n",myDict)
