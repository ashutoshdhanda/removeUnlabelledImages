# scan the files in the folder

# make a list of all files

# split the names from the extension

# if the name does not have a copy, viz. if the name exists only once in the list, then put this name in another list

# add the extension jpg or png to each element of the list to get a 'to-delete-list'

# delete every file in the folder that falls in the 'to-delete-list'
import os
from os import listdir
from os.path import isfile, join
mypath = os.path.dirname(os.path.abspath(__file__))
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
filenames = []
for file in onlyfiles:
	a, b = os.path.splitext(file)
	print("file="+a)
	print("extension="+b)
	filenames.append(a)
# print("The list of filenames is as under:")
# print(filenames)
for filename in filenames:
	if filenames[0]==filenames[1]:
		filenames.pop(0)
		filenames.pop(1)
		#filenames.pop(2)
print("RESULT")
print(filenames)




# put all filenames in a list, for all elements of the list, if the element comes twice, delete the element from the list.
# this filtered list has to be appended with the extension 'jpg' and then the delete fiel has to act on this list

#print(onlyfiles)
