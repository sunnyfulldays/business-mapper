#Written by David Kraus 
#Descriptions:
# -------------------------
# This code does the following:
#1. Takes a combined string consisting of a name and address 
# and splits it into seperate strings
#2. Takes these, and feeds the name string into the probablepeople library
# and returns a dictionary of the components of the name
#3. Does the same with the address string
#4. Formats the dictionary as XML and returned an XML file

import codecs

#needed because default file opening library does not support text files
#encoded in UTF-8

import usaddress
import probablepeople
import re

#parameters for opening file

filename = "test"
mode = "r"  #if file should be read-only have things written to it
encoding = "UTF-8" #encoding of text file

def openPeopleAddress(filename,mode,encoding):
	file = codecs.open(filename,mode,encoding)
	myList = []
	for line in file:
		myList.append(line)
	return myList

def returnAddress(testList):
	address = re.search('[0-9].*',testList) 
	if address:
		address = address.group()
	return address

def returnName(testList):
	name = re.search('.+?(?=[0-9])',testList)
	if name:
		name = name.group()
	return name

def lookupPeople(name):
	parsedName = probablepeople.parse(name)
	return parsedName

def lookupAddress(address):
	parsedAddress = usaddress.parse(address)
	return parsedAddress

def addressToJSON(address):
		tupleswitch = dict([(element[1], element[0]) for element in address])
		return tupleswitch



#opening text file

testList = openPeopleAddress(filename,mode,encoding)

#empty lists for addresses and names 

name = []
address = []
filteredName = []
filteredAddress = []



#add addresses to address list and names to name list 

for i in testList:
	appendAddress = returnAddress(i)
	appendName = returnName(i)
	address.append(appendAddress)
	name.append(appendName)


#remove empty elements from name and address lists 

name = filter(None, name)
address = filter(None, address)


for i in name:
	nameElement = lookupPeople(i)
	filteredName.append(nameElement)
	#print(nameElement)

for i in address:
	addressElement = lookupAddress(i)
	filteredAddress.append(addressElement)
	#print (addressElement)

	
##print(returnName(testList[2]))



#print (returnName('Joe Jr. 134 Test St.'))

#print re.match(".+?(?=/d)","Joe Jr, 134 Test St.")





# def PeopletoXML():

# def AddresstoXML():




# file = codecs.open("test","r","UTF-8")

# myList = []

# for line in file:
#     myList.append(line)



# print(myList[1])
# print(myList[10])



# print address
# print name
        


