# python

## object oriented programming

### encapsulation

a python class defines a set of attributes for the data and the methods used to carry out operations related to the data, it hides (encapsulates) the implementation details of the programmed elements, while restricting direct access to those elements it also provides a public interface for interacting with the class through its objects

- a class acts as a template for creating objects that can potentially access the same set of related methods and attributes
- wrapping / bundling everything up about a particular thing (data attributes and methods to work with that data)
- for example a bank accounts features and behaviours
    - methods for the data (deposit, withdraw, check balance)
    - data fields (name, sortcode, account number, balance)
- once wrapped we can ask the object itself to do what its supposed to do -> deposit money, withdraw money
- nobody outside the object needs to worry about how it does its jobs
- one object stays out of the business of other objects

class = human
objects = name
properties = email, address
methods = verify, send mail

### inheritance

we dont have to define everything about an object over and over if it shares features and behaviours with other objects
we can define a class for accounts and let both a current account and a savings account inherit all the stuff in common

accounts -> parent class
current account -> child class
savings account -> child class
a child is like its parents but much more special -> a current account can write physical cheques, a savings account cannot

### polymorphism

treat the same object as different things depending on how we need it at different times
treat groups of objects that share an ancestor or trait as if they were that ancestor or trait
we could ask a queue of animals to move quickly and not care how different animals would handle the shared behaviour
we could ask a current, savings and isa and ask each to get balance

## basics

() to specify order
print('')

a = 9
a = b = c = 9 -> all equal 9
a, b, c = 1, 2, 3 -> a=1 b=2 c=3
print(var)
var = input('whats your name')

== -> equals
!= -> not equals

and, or and not

list ['one', 'two', 'three']
list [ 1, 2, 3]
append / extend / sort etc
list () is a tuple / restricted / fixed values that cannot be changed by the program
list {} is a set, a list of unique values
a python dictionary is a powershell hash table

def name() is a custom function
variables created outside of functions can be referenced inside functions as they have a global scope
varialbes created inside functions cannot be referenced from outside the function which they have been created, they have a local scope
locals can be accessible elswere if they are decalred with the global keyword - where a global and local have the same name the function will use the local version

def name(argument) - a call to this function must specify a value for argument 

return -> return a valus from a function 

lambda is an anonymous unnamed function, efficient when you want to create a function that is simple, usually a single line

def square(x):
    return x ** 2

as a lambda:

square = lambda x:x ** 2

def function_1(x): return x **2
def function_2(x): return x **3
def function_3(x): return x **4
callbacks = [ function_1, function_2, function_3]
for function in callbacks: print ( function(3))
=9
=27
=81

lambda
callbacks = [ lambda x:x ** 2, lambda x:x ** 3, lambda x:x ** 4 ]
for function in callbacks: print ( function(3))
=9
=27
=81

pass is a placeholder

genrator is a special function, it has a yeild keyword

```python
def fibonacci_generator() :
	a = b = 1
	while True :
		yield a
		a , b = b , a + b

fib = fibonacci_generator()

for i in fib :
	if i > 100 :
		break
	else :
		print( 'Generated:' , i )
```

handling exceptions -> try and except blocks

debugging with assert 
assert test-expression, descriptive-message

```python
assert type(element) is int, 'argument must be a integer'
```

functions can be stored in one or more files to allow them to be used in several programs
imported functions can be called using their dot suffixed name
for example a steps function from a imported module named imported would be references as steps.imported()

where the function includes arguments its useful to assign a default value to the argument in the definition.

sys and keyword, import sys, keyword then interrogate

```python
import sys , keyword

print( 'Python Version:' , sys.version )

print( 'Python Interpreter Location:' , sys.executable )

print( 'Python Module Search Path: ' )
for dir in sys.path :
	print( dir )

print( 'Python Keywords: ' )
for word in keyword.kwlist :
	print( word )
```

math module same as powershell, import math, import random

date time module same as powershel

time module for timers etc - time since epoch

import re - regular expressions - same as powershell, eg to check mail format name@domain.ext

strings same as powershell - str object can capitalise etc
str object to format strings

dir() can be used to examine the names of functions and variables defined by a module
import module
for i in dir(module):
    print(i)

the __builtins__ module can be examined with dir()

pickle - store integer as string then retrieve as integer
import pickle, os

```python
import pickle, os

if not os.path.isfile( 'pickle.dat' ) :

	data = [ 0 , 1 ]
	data[ 0 ] = input( '\nEnter Topic: ' )
	data[ 1 ] = input( 'Enter Series: ' )
	file = open( 'pickle.dat' , 'wb' )
	pickle.dump( data , file )
	file.close()
else :
	file = open( 'pickle.dat' , 'rb' )
	data = pickle.load( file )
	file.close()
	print( '\nWelcome Back To:' , data[ 0 ] , data[ 1 ] )
```

class
set of properties that charactize an object
the properties are its data members, class function members are known as methods and variables decalred within a class structure but outside ant method definitions are known as attributes

class members can be referenced throughout a program using . notation class-name.class-method or class-name.attribure-name

class first letter in uppercase, ClassName:

all variables referenced within method definitions can only be accessed locally within the method they are decalred, called: instance variables

this is encapsulation ! effectively hidden form the rest of the program

all properties of a class are referenced internally by the dot notation prefix self so an attribute named sound is self.sound, all method definitions is a class must have a self their first argument so a method named talk is talk(self)

when a class is created a special __init__(self) method is automatically called, subsequent arguments can be added in its parenthisis if vaules are to be passed to initialize attributes

```python
class Critter:
    '''a base calss for all critter properties'''
    count = 0 # class variable shared amongst all instances of this class, can be referenced as Critter.count inside and outside the class
    def __init__(self, chat): # automaticalled called when a instance of the class is created, in this case initialises the variable sound with a value passed from the chat argument and incements the count class variable whenever an instance of this class is created
        self.sound = chat
        Critter.count += 1
    def talk(self): # this method is decalred like a regular function except the first argument self which is automatically incorporated - no value needs to be passed form the caller, the talk methos in this case simply returns the value encapsulated in the sound instance variable
        return self.sound
```

an instance of a class is a prototype created by calling that class's name constructor and specifying the required number of arguments within its parentheses, the calls arguments must match those specified by the __init__() method defintion, other than the value for the self argument

the class instance returned by the constructor is assigned to a variable using the syntax instance-name = ClassName(args)

dot notation can be used to reference the methods and class variable attributes of an instance object by suffixing their name as instance-name.method-name() or instance-name.attribute-name()

```python
class Bird :

	'''A base class to define bird properties.'''

	count = 0

	def __init__( self , chat ) :

		self.sound = chat
		Bird.count += 1

	def talk( self ) :

		return self.sound

```

```python
from Bird import *

print( '\nClass Instances Of:\n' , Bird.__doc__ )

polly = Bird( 'Squawk, squawk!' )

print( '\nNumber Of Birds:' , polly.count )
print( 'Polly Says
:' , polly.talk() )

harry = Bird( 'Tweet, tweet!' )
print( '\nNumber Of Birds:' , harry.count )
print( 'Harry Says:' , harry.talk() )

```

addressing class attrributes

an attribute of a class instance can be added, modified or removed at any time using dot notation to address the attribute

instance-name.attribute-name = value
del instance-name.attribute-name

**getattr( instance-name, 'attribute-name') -> get attribute value**

hasattr -> true is the value exists

setattr -> set attribute name (instance-name, 'attribute-name, value)

delattr -> delete

**examining built in attributes**
class-name.__doc__

the built in dir() function can be used to display a list of all buitl in attributes in a class

the built in __dict__ is a namespace dictionary of class compoenent keys and their associated vlaues, the dictionary of a base class inclused its default __init__() method and all other class methods and attributes, the dictionary of a class instance includes its instance attributes

```python
from Bird import *

zola = Bird( 'Beep, beep!' )

print( '\nBuilt-in Instance Attributes...' )
for attrib in dir( zola ) :

	if attrib[0] == '_' :

		print( attrib )

print( '\nClass Dictionary...' )
for item in Bird.__dict__ :

		print( item , ':' , Bird.__dict__[ item ] )

print( '\nInstance Dictionary...' )
for item in zola.__dict__ :

		print( item , ':' , zola.__dict__[ item ] )
```

collecting garbage, python automatically performs garbage collection using the class id(), can be destroyed in code using the __del__() method

interiting features, a class can be created as new or can be derived from an existing class. a derived class inherits the members of the parent (base) in addition to its own members

a polygon class may define width and height - common to all polygone
classes of rectangle and traingle could be derived from the polygonw class, inheriting width and height in addition to their own members defining unique features.

polygon, rectangle, triangle, inherit

```python
class Polygon :
	width = 0
	height = 0
	def set_values( self , width , height ) :
		Polygon.width = width
		Polygon.height = height
```

```python
from Polygon import *

class Rectangle( Polygon ) :
	def area( self ) :
		return self.width * self.height
```

```python
from Polygon import *

class Triangle( Polygon ) :
	def area( self ) :
		return ( self.width * self.height ) / 2
```

```python
from Rectangle import *
from Triangle import *

rect = Rectangle()
trey = Triangle()

rect.set_values( 4 , 5 )
trey.set_values( 4 , 5 )

print( 'Rectangle Area:' , rect.area() )
print( 'Triangle Area:' , trey.area() ) 
```

**dont confuse class instances and derived classes, a instance is a copy of a class whereas a derived class is a new class the inherits properties of the base class from which it is derived**

overriding base methods, a method can be declared in a derived class to override a matching methods in the base class, this effecitvely hides the base class method unless its called explicitly using the base class name for identification.

```python
class Person :

	'''A base class to define Person properties.'''

	def __init__( self , name ) : 
		self.name = name

	def speak( self , msg  = '(Calling The Base Class)' ) :
		print( self.name , msg )
```

```python
from Person import *

'''A derived class to define Man properties.'''

class Man( Person ) :

	def speak( self , msg ) :
		print( self.name , ':\n\tHello!' , msg )
```

```python
from Person import *

'''A derived class to define Hombre properties.'''

class Hombre( Person ) :
	def speak( self , msg ) :
		print( self.name , ':\n\tHola!' , msg )
```

```python
from Man import *
from Hombre import *

guy_1 = Man( 'Richard' )
guy_2 = Hombre( 'Ricardo' )

guy_1.speak( 'It\'s a beautiful evening.\n' )
guy_2.speak( 'Es una tarde hermosa.\n' )

Person.speak( guy_1 )
Person.speak( guy_2 )
```

**polymorphism**

to assign a different menaning or purpose to an entity according to its context, in python the + character entity can be described as polymorphic because it represents either the aritimitical addition operator or the string connetation operator in the context of character operands.

python class methods can also be polymorphic because the python language uses duck typing, meaning if it walks like a duck, swims like a duck, and quacks like a duck then that bird is reckoned to be a duck.

in a duck typed language you can create a function to take an object of any type and call that objects methods, if the object does have the called metods and is reckoned to be a duck they are executed, otherwise the function singals a run time error.

duck, mouse, polymorph

```python
class Duck :

	'''A class to define Duck properties.'''

	def talk( self ) :
		print( '\nDuck Says: Quack!' )

	def coat( self ) :
		print( 'Duck Wears: Feathers' )
```

```python
class Mouse :

	'''A class to define Mouse properties.'''

	def talk( self ) :
		print( '\nMouse Says: Squeak!' )

	def coat( self ) :
		print( 'Mouse Wears: Fur' )
```

```python
from Duck import *
from Mouse import *
 
def describe( object ) :
	object.talk()
	object.coat()

donald = Duck()
mickey = Mouse()

describe( donald )
describe( mickey )
```

sending responses, designing gui to do.
