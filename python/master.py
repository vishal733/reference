#!/usr/bin/python


"""
# Python syntax highlights:
- ":" is put at end of every for/while/etc... loop
- For accessing an element, always use square([]) brackets
"""


##########################################################
# Online resources
##########################################################
http://projecteuler.net/ # both Python and Mathematics
http://greenteapress.com/thinkpython/ # How to Think Like a Computer Scientist.
PyGame (http://pygame.org) # Learn to write simple python games.
PyOpenGL # Google for "NeHe's OpenGL" to get started
http://www.pythonchallenge.com/ # 
http://rhettinger.wordpress.com/2011/05/26/super-considered-super/ # Usage of super() in detail


##########################################################
# Interesting modules
##########################################################
- argparse
- serial
- threading



#########################################################
# MODULES - loading/ deleting/ reloading
#########################################################
#import sys # makes sys module functions available as sys.argv, etc.
#from sys import * # you can import only certain functions. Functions/lists are directly accessible with module name suffix
# import sys as s # use like s.argv, etc.
# help (sys) # gives info on sys
# dir(sys) # concise help, gives the name of all functions/variables defined in a package
# help (sys.argv) # help can be called for specific functions/variables



#########################################################
# USER INPUT
# - raw_input()
# - input()
#########################################################
person= raw_input('Enter your name') # Kumar Vishal
pring 'Hello', person, '!' # Hello Kumar Vishal!
#NOTE: raw_input always treats input as a string.
#In order to use as int, use the int(string) function


x, y = input("Enter two comma separated numbers: ")
print ’The sum of %s and %s is %s.’ % (x, y, x+y) # works for integers!!



#########################################################
# PRINT
# - Simple print
# - Print without newline
# - print without any space
#########################################################
print "Hello" #prints with a new-line at the end
print "World", #prints with a space at the end
import sys
sys.stdout.write('!') #prints without new-line or space
sys.stdout.write('\n')


print >>sys.stderr, "This is an error message"
print "This is stdout"
print >>sys.stdout, "This is also stdout"
print '-' * 10


#########################################################
# COMMAND LINE Arguement passing
#########################################################


# Gather our code in a main() function
def main():
"""Command line args are in sys.argv[1], sys.argv[2] ...
sys.argv[0] is the script name itself and can be ignored
"""
print 'Printing command line parameter = ', sys.argv[0]
print 'Number of arguements passed = ', len(sys.argv)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__': # by default __name__ holds __main__
main()


print __name__



##########################################################
# General 
##########################################################
s='hi'
print s[1] ## i
print len(s) ## 2
pi=3.14
print 'The value of pi is' + str(pi)
3+4
3-4
3*4
6/5
6//5 ## 1 , use // to explictly indicate an integer division


a,b = 0,1 # assigns 0 to a, 1 to b in a single statement]
a,b = b,a # swapping in python can be as simple as this. No need to explicitally take a backup
(a,b) = (b,a) # swapping is actually a tuple operation


raw = r'This is\t\n example for raw string' # Raw strings get passed without special treatment of backslashes
print raw


int("3") # convert string to int
str(3) # convert number to string


x=true;
if x: # We need to put colon. And are not supposed to put any brackets for iteration loops/ conditional statements
  print "This is the true part"
else: print "This is the false part" #May be contained on the same line as colon


##########################################################
# Data types
# - Lists
# - Set
# - Sorting
# - Tuples
# - Arrays
# - Dict
# - Strings
##########################################################


#############################################
#LISTS
#############################################
colors = [red, green, blue]
print colors[2]
len(colors) # 3


b= colors #does not copy the list. Both b and colors will point to same list


for col in colors:
  print col, # red green blue


if 'green' in colors:
  print "Green is present" # NOTE: No need for a 'for' loop


for i in range(100) #range(x) produces a list 0 1 .... x
  print i, # 0 1 2 3 ...... 99
#xrange(x) -- similar to range, but avoids building the whole list for performance reasons


while i < len(colors):
print i, # 0 1 2
i += 1


#----------- LIST METHODS ----------------#
colors.append('yellow') # appends yellow at end of list
colors.insert(1, 'orange') # inserts orange at index 1
colors.extend(['yyy', 'zzz']) # adds list of elements at the end
print colors ## ['red', 'orange', 'green', 'blue', 'yyy', 'zzz']
print colors.index('yyy') # 4
colors.remove('yyy') # search and remove that element
print colors.pop(2) # 'green'. Removes element at index 2. Also returns it's value
print colors # ['red', 'orange', 'blue', 'yyy']


####NOTE: Most of the above methods do not return anything
#### Ex: List2 = colors.append('xxx') will return an empty List2


#------------ LIST BUILDUP ----------------#
list = [] # Common method is to start with an empty list.
list.append('a')
list.append('b')



#------------ LIST SLICES ----------------#
list = ['a', 'b', 'c', 'd']
print list[1:-1] ## ['b', 'c']
list[0:2] = 'z' ## replace ['a', 'b'] with ['z']
print list ## ['z', 'c', 'd']



############################################
# SORTING- Two functions: sorted, sort
############################################


a = [5, 1, 4, 3]
print sorted(a) ## [1, 3, 4, 5], sorted returns another list which is sorted
print sorted(a, reverse=True) ## [5, 4, 3, 1] Reverse list
print a ## [5, 1, 4, 3], original list is not sorted on calling sorted(list)
b= a.sort() # sort doesn't return anything. Sort can be called on a list, does not work on any enumerable collection like sorted()
print a ## [ 1, 3, 4, 5]
print b ## ''


strs = ['aa', 'BB', 'zz', 'CC']
print sorted(strs) ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print sorted(strs, reverse=True) ## ['zz', 'aa', 'CC', 'BB']


#---------------- Custom sorting -----------#
strs = ['ccc', 'aaaa', 'd', 'bb']
print sorted(strs, key=len) ## ['d', 'bb', 'ccc', 'aaaa'], sort by length
# key forces proxy values for sorting. Proxy values generated by using the function passed
print sorted(strs, key=str.lower) ## ['aa', 'BB', 'CC', 'zz'], force case-insensitive sorting


#custom sort function
def MyFn(s):
return s[-1]


## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']


## Now pass key=MyFn to sorted() to sort by the last letter:
print sorted(strs, key=MyFn) ## ['wa', 'zb', 'xc', 'yd']


## sorted(strs, cmp=cmpFn), specifies traditional two-arguement comparison function
## that takes two values from the list and returns negative/0/positive to indicate
## their ordering


#############################################
#SET
#############################################
# Lists may have duplicates. Whereas a Set would not
numberList = [2, 1, 3, 2, 5, 5, 2]
aSet = set(numberList)
aSet # set([1, 2, 3, 5])
# typically item is unordered in a set


set(['animal', 'food', 'animal', 'food', 'food', 'city']) # set(['food', 'city', 'animal'])



#########################################################
# TUPLES
#########################################################
# Tuple - fixed size grouping of elements, such as (x,y)
# Tuples are like lists, except they are immutable, and do not change size
# Tuples play a sort of "struct" role in Python
# Function that needs to return multiple values can just return a tuple of values


tup = (1, 2, 'hi') 
print len(tup) ## 3
print tup[2] ## hi
tup[2] = 'bye' ## NO, tuples cannot be changed
tup = (1, 2, 'bye') ## THIS WORKS


tup = ('hi',) ## size-1 tuple. Still have to add the comma. Necessary to separate from putting an expression in parantheses.


(x, y, z) = (42, 13, "hike")
print z ## hike


(err_string, err_code) = Foo() ## if Foo() returns a length-2 tuple





#########################################################
#DICTS
#########################################################
# Python's efficient key/value hash table structure is called a "dict". 
# Ex: dict = {key1:value1, key2:value2, key3:value3, ...}
# Ex: dict = {} # Empty dict
dict2 = {}
dict2['a'] = 'alpha'
dict2['b'] = 'beta'
dict2['g'] = 'gamma'
dict2['o'] = 'omega'
print dict2 ## {'a': 'alpha','b': 'beta', 'o': 'omega', 'g': 'gamma'}


print dict2['a'] ## simple lookup, returns 'alpha'
dict2['a'] = 6 ## Put new key/value into dict
'a' in dict2 ## True
## print dict['z'] ## Throws KeyError
if 'z' in dict2: print dict2['z'] ## Avoid KeyError
print dict2.get('z') ## None (instead of KeyError)


for key in dict2: print key #prints a b o g


print dict2.keys() ## ['a', 'b', 'o', 'g']
print dict2.values() ## ['alpha', 'beta', 'omega', 'gamma']
print dict2.items() ## [('a', 'alpha'), ('b', 'beta'), ('o', 'omega'), ('g', 'gamma')]


for key in sorted(dict2.keys()):
print key, dict2[key]
#a alpha
#b beta
#g gamma
#o omega


for k, v in dict2.items(): print k, '---', v
#a --- alpha
#b --- beta
#o --- omega
#g --- gamma


#------------ DICT FORMATTING --------------------------#
#----------Lookup while printing -----------------------#
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % hash # %d for int, %s for string
# 'I want 42 copies of garfield'


##########################################################
#DEL
##########################################################
var = 6
del var # var no more!

list2 = ['a', 'b', 'c', 'd']
del list2[0] ## Delete first element
del list2[-2:] ## Delete last two elements
print list2 ## ['b']


dict1 = {'a':1, 'b':2, 'c':3}
del dict1['b'] ## Delete 'b' entry
print dict1 ## {'a':1, 'c':3}


##########################################################
# STRINGS/CHARACTERS
# - Convert between ascii and actual character
# - Character mapping
# - Changing individual characters in a string - by converting string to list/array
# - Joining the elements of a list to make a string
# - Counting occurance of characters in a string
##########################################################


#----------------------------------
#Common String operations
#----------------------------------
s0 = 'string0'
s1= '-' + s0
print s1


s2= '*' * 10 # Convenient way to repeat strings
print s2


sString = " This is a sample string "
print sString.lower()
print sString.upper()
print sString.strip() #Removes white-space from start and end
print sString.rstrip("\n") #Removes new-line characters from end 
print sString.isalpha() #Whether all characters of string are alphabets
print sString.isdigit() #Whether all characters of string are digits
print sString.isspace() #Whether all characters of string are space
print sString.startswith(' This') # whether start of string matches 
print sString.endswith(' This') # whether end of string matches 
print sString.find('This') # searches and returns the location of string (not a regex). Returns -1 if not found
print sString.replace('This', 'That') # Does string replacement in sString, and returns a new string
print sString.split(' ') # Retruns a list of substrings separated by the given delimiter. When nothing is passed as arguement,
print sString.split() # Split on any white-space character. Also removes multiple-spaces
print sString.join(["123","456","789"]) # returns a string after joining the contents of list passed. After joining every element, sString is concatenated



#-------------------------------------
# String numbering
# H e l l o
# 0 1 2 3 4
# -5 -4 -3 -2 -1
#-------------------------------------
sString="Hello"
print sString[1:3] # el, from a to b, not including b
print sString[3:10] # lo
print sString[-1] # 'o'
print sString[:-2] # 'Hel'
print sString[5:] # ''
print sString[5] # throws an error
print sString[-2:] # 'lo'
print sString[-2:0] # ''
print sString[2:2] # ''


# s[:n] + s[n:] = s is always valid


#-------------------------------
# String %
#-------------------------------
text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down') # This is spanning a single line.
text = ("%d little pigs come out or I'll %s and %s and %s" %
(3, 'huff', 'puff', 'blow down')) # add paranthesis to span the statement across multiple lines



z_ascii= ord('z')
print "Ascii value of 'z':", z_ascii


a_alpha = chr(ord('a'))
print "Char for ascii",ord('a'),":",a_alpha


#Character mapping
print "Character mapping:",


inp_tab='abcdefghijklmnopqrstuvwxyz'
out_tab='cdefghijklmnopqrstuvwxyz--' #size of inp_tab, out_tab must be same


out_list=list(out_tab) # Convert to array, to change individual entries in a string
out_list[24]='a'
out_tab= "".join(out_list)


from array import array
out_array=array("c",out_tab) #Convert to char array, to change individual entries
out_array[25]='b'
out_tab= out_array.tostring()


from string import maketrans
data="g fmnc wms bgblr rpylqjyrc gr zw fylb."
transtab= maketrans(inp_tab, out_tab)
print data.translate(transtab)


from collections import Counter
c= Counter()
for i in data:
c[i] +=1


print c



##########################################################
# FILE i/o - read line by line, whole file at once
##########################################################
#f = open('foo.txt', 'r') ## read
#f = open('foo.txt', 'w') ## write
#f = open('foo.txt', 'a') ## append
#f = open('foo.txt', 'rU') ## read Universal. Smart about converting diff line-endings, can be read as '\n'


f= open('foo.txt', 'rU')
for line in f: ## iterates over the lines of the file
print line, ## trailing, so print does not add extra end-of-line char since 'line' already includes the end-of-line.
f.close()


#f.read() ## reads whole file at once
#f.readline() ## reads one line. Reads the next line when called progressively
#f.readlines() ## reads whole file at once, returns its contents as a list of its lines



#--------- WRITE TO FILE --------------------#
#f.write(string) ## standard way of writing into files
#print >> f, string ## another syntax for writing into files



#---------- DEALING WITH UNICODE FILES -------------#
import codecs # codec module provides support for reading a unicode file


f=codecs.open('foo.txt', 'rU', 'utf-8')
for line in f:
# here line is a *unicode* string

#For writing, use f.write() since print does not fully support Unicode.



##########################################################
# REGEX - re.search, re.findall, re.sub
##########################################################
# search returns the first match
# findall returns all the matches in a list
# sub is to substitute all instances of matches


import re


f=open('input3.txt','r')
data= f.read()



#re.findall
print "".join(x[1] for x in re.findall('(^|[^A-Z])[A-Z]{3,3}([a-z])[A-Z]{3,3}([^A-Z]|$)',data))


data="skjd1.23k2cow3r98au1*238vkncowsl1-23cssP1 23]O][;'.,[PSADJPSADMKLSDLF;,.SADMFKDSF],DSF'D"
print "Original data:", data


out= re.findall('s',data);
print out


# Metacharacters: \ . * +
# "." matches any character
# "*" matches zero or more occurrences
# "+" matches one or more occurences
# "?" matches a character zero or one times
# {n,m} - minimum and maximum number of matches
# "^" - beginning of line
out= re.findall('1.23',data) # "." matches any character
print out
out= re.findall('1\.23',data) # "\." to remove special meaning of "."
print out


out= re.findall('ss*',data)
print out
out= re.findall('ss+',data)
print out


out=re.findall('cows?',data)
print out


out=re.findall('[0-9][a-zA-Z]{2,3}[0-9]',data)
print out


out=re.findall('[0-9][a-zA-Z]{2,}[0-9]',data) #upto infinite matches
print out


out=re.findall('[0-9][a-zA-Z]{3}[0-9]',data) # matches exactly n occurances
print out


# *? - makes * nongreedy
# *? - makes * nongreedy


##############################
# Groups and Alternation
##############################
# Even metacharactrs can be quantified using [* ? +]
# () - create a group of pattern to be matched
# | matches any of many words



##############################
# Sequences
##############################
# []
out=re.findall('s[kl]',data)
print out


out=re.findall('[a-zA-Z]+',data)
print out


out=re.findall('[^a-zA-Z]+',data)
print out



##############################
# Shorthands
##############################
# Some implementations of regex allows for shorthands for commonly used sequences
# \d - a digit ([0-9])
# \D - a non-digit ([^0-9])
# \w - a alphanumeric world ([a-zA-Z0-9])
# \W - a non-word ([^a-zA-Z0-9])
# \s - a single whitespace ([ \t\n\r\f]) - space, newline, return, tab, form [ \n\r\t\f]
# \S - a single non-whitespace ([^ \t\n\r\f])
# \b - boundary between word and non-word
# \t - tab
# \n - newline
# \r - return


###############################
# Wildcards
###############################



###############################
# Options
###############################
# Ex: re.search(pat, str, re.IGNORECASE).


#IGNORECASE -- ignore upper/lowercase differences for matching, so 'a' matches both 'a' and 'A'.
#DOTALL -- allow dot (.) to match newline -- normally it matches anything but newline. This can trip you up -- you think .* matches everything, but by default it does not go past the end of a line. Note that \s (whitespace) includes newlines, so if you want to match a run of whitespace that may include a newline, you can just use \s*
#MULTILINE -- Within a string made of many lines, allow ^ and $ to match the start and end of each line. Normally ^/$ would just match the start and end of the whole string.



##########################################################
# FILE SYSTEM -- os, os.path, shutil
##########################################################
import os
# import os.path , is this required??
# import shutil, is this required??
path= "/home/vishal/foo/bar.html"
dir = "/home/vishal/foo/"
os.listdir(dir) # gives a list of files directory 'dir'
os.path.abspath(path) # gives the full system path for mentioned path . Ex: "." will expand to current directory. can also include filename
os.path.dirname(path) # returns "/home/vishal/foo"
os.path.basename(path) # returns "bar.html"
os.path.join(dir, filename) # Joins the dir and filename to arrive at complete path for a file
os.path.exists(path) # true if it exists
os.mkdir(dir_path) # makes one dir
os.makedirs(dir_path) # makes all the directories in this path
shutil.copy(source-path, dest-path) -- copy a file (dest path directories should exist)



##########################################################
# Running external processes -- commands. 
# os, commands module
##########################################################
os.system(cmd) # runs the cmd. Returns command exit status. Puts output to standard output. Is useful when we don't intend to process command output


import commands
(status, output) = commands.getstatusoutput(cmd) # runs the command, waits for it to exit, returns status int and output text as a tuple. Standard output and standard error get combined into one output text
output = commands.getoutput(cmd) #same as getstatusoutput, but without the status int




##########################################################
# Exceptions
##########################################################
try:
## 
except IOError:
## ..


##########################################################
# Handling URLs
# - read from webpage
##########################################################
import urllib


f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
data2= f.read()



##########################################################
# Pickle
# - pickle
# - unpickle
##########################################################


##########################################################
# COMMON MODULES
# - math
##########################################################


import math


ratio = signal_power/ noise_power
decibels = 10 * math.log10(ratio)


height = math.sin(0.7) # sin (0.7 radians)


degrees = 45
radians = degrees / (360.0 * 2 * math.pi) # math.pi contains value of pi accurate to about 15 digits
math.sin(radians) # 0.707106781187


math.sqrt(2)
math.exp(math.log(x+1))




##########################################################
# OOPS
# - general
# - __init__ method
# - __str__ method
# Operator overloading using __add__, etc.
# Type-based dispatch
# right-side operator -- Ex: __radd__
# Polymorphism
# Polymorphism vs inheritance
##########################################################


class Point(object):
"""Represents a point in 2-D space."""


print Point # <class '__main__.Point'> 
# Because Point is defined at the top level, its “full name” is __main__.Point


blank = Point()
print blank # <__main__.Point instance at 0xb7e9d3ac>


blank.x = 3.0 # !!!! Works even though x was not originally part of Point
blank.y = 4.0 # !!!!


class Time(object):
# __init__ is a special function which gets invoked when an object is instantiated.
def __init__(self, hour=0, minute=0, second=0): 
self.hour = hour
self.minute = minute
self.second = second


# __str__ is special method, supposed to return a string representation of an object. When we print an object, Python invokes the str method
def __str__(self):
return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)


# __add__ if defined is a special function for operator overloading '+' operator. For every operator in Python there is a corresponding special method, like __add__
def __add__(self, other):
seconds = self.time_to_int() + other.time_to_int()
return int_to_time(seconds)


# We could also have wanted to add an interger to time. Another implementation which first checks the type of other.
def __add__(self, other): # example of type-based dispatch
if isinstance(other,Time): #built-in function isinstance takes a value and a class object, returned True if the value is an instance of the class.
return self.add_time(other)
else:
return self.increment(other)
def add_time(self, other):
seconds = self.time_to_int()+other.time_to_int()
return int_to_time(seconds)
def increment(self, seconds) :
seconds += self.time_to_int()
return int_to_time(seconds)


#Now implementation of addition is not communicative. If integer is the first operand, we get
print 1337 + start # TypeError


# Solution is the use of special method called '__radd__' which is "right-side add". This is invoked whenever a Time object appears on the right side of the + operator.


def __radd__(self, other):
return self.__add__(other)



########################################
# POLYMORPHISM
########################################
# Functions that can work with several types are called polymorphic.
#Polymorphism can facilitate code reuse.
#For example, the built-in function sum, which adds the elements of a sequence, works as long as the elements of the sequence support addition.


# Ex: Since Time objects provide an add method, they work with sum
#>>> t1 = Time(7, 43)
#>>> t2 = Time(7, 41)
#>>> t3 = Time(7, 37)
#>>> total = sum([t1, t2, t3])
#>>> print total
#23:01:00


##########################################################
# Tkinter - for GUI applications using Python
##########################################################
# http://www.pythonware.com/library/tkinter/introduction/x59-details.htm
import Tkinter
# from Tkinter import *


# Tkinter support the following widgets
# - Button: A widget, containing text or an image, that performs an action when pressed.
# - Canvas: A region that can display lines, rectangles, circles and other shapes.
# - Entry: A region where users can type text.
# - Scrollbar: A widget that controls the visible part of another widget.
# - Frame: A container, often invisible, that contains other widgets
