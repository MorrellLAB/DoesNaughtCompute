# Introduction to Python
### Shawn Goggins and Paul Hoffman
Does[0]Compute? February 12, 2016

---

# Assumed Knowledge
- Can start Python interpreter
- Using Python 3
    - `python --version`
        - *nix: `which python3`
        - Windows: `where.exe python3`

# What is Python?

- High-level, interpreted, imperative programming language
- Primarily object oriented
- Dynamically typed

# Programming Paradigms

High-level:
- Human readable
- Abstracted away from the hardware

# Assembly Language

![Assembly Language](https://upload.wikimedia.org/wikipedia/commons/f/f0/Zstr_count_x86_assembly.png)

Code for the NASM Assembler for 32-bit Intel x86 processors

# Programming Paradigms

Interpreted:
- Do not need to compile source code before running program
- Can enter an 'interactive' mode for Python

Imperative:
- Program can change state
- Code describes how to solve a problem rather than what the solution should be like

# Imperative vs Declarative Programming

*Imperative*

```python
>>> numbers = [1, 2, 3, 4, 5] # Create a list of numbers
>>> doubled = [] # Create an empty list for doubled numbers
>>> for i in numbers: # For each number
...     newNumber = i * 2 # Create a new number equal to the current number times two
...     doubled.append(newNumber) # Add this to the list of doubled numbers
...
>>> doubled # Print our list to the screen
[2, 4, 6, 8, 10]
```

*Declarative*

```javascript
> var numbers = [1,2,3,4,5] // Create an array of numbers
> var doubled = numbers.map(function(n) { // Tell the computer to double all numbers
    return n * 2 // But we don't specify how to go about the doubling
})
> console.log(doubled) // Print our array of double numbers to the screen
[2, 4, 6, 8, 10]
```

# Python Quirks I: Whitespace and Indentation

Python is whitespace senstive

```python
>>> def hello_world(): # No indentation for this line, but the colon is required
...     print("Hello World") # We have a single intentation to denote the code block, this is required
...         print("Another line!") # What happens if we add a second indenation without starting a new code block?
  File "<stdin>", line 3
    print("Another line!")
    ^
IndentationError: unexpected indent
```

# Python as an Object Oriented Language

- Computers don't inherently know what that data is or how to use it
- **Types** tell the computer what kind of data we have and what we are allowed to use it for
- We use these data by calling functions and methods for manipulation and analyses

# Primitive Types

| Type | What? |
| ---- | ----- |
| `bool` | Boolean values, used for logical statements: `True` and `False` |
| `str` | String, litterally whatever you put in: "Hello world" |
| `int` | Integers, whole numbers only: 5, 10, -36 |
| `float` | Floating-point numbers, numbers with a fractional part: 5.9, 12.3 |

# Dynamic Typing

Python does not require declaration of variables

*C++*

```cpp
int var; // Declare `var' as an integer type
var = 5; // Tell C++ that `var' equates to 5
```

*Python*

```python
>>> var = 5 # Python understands that 5 is an integer type
>>> type(var) # Make sure that we `int' as our type
<class 'int' >
```

# Collections

| Type | What? |
| ---- | ----- |
| `list` | An unordered, mutable collection of primitive types |
| `tuple` | An unordered, unmutable collection of primitive types |
| `set` | An unordered, mutable, unique **collection** of primitive types |
| `dict` | An unordered, mutable collection of primitive types stored in `key: value` pairs |

# Python Quirks II: Referenced Values

```python
>>> alphabet_list = ['a', 'b', 'c'] # Create a list with square brackets
>>> alphabet_list # What does this look like?
['a', 'b', 'c']
>>> copy_list = alphabet_list # Make a new list that's the same as `alphabet_list'
>>> copy_list # Make sure it's the same
['a', 'b', 'c']
>>> copy_list.append('d') # Add the letter 'd' to our new list
>>> copy_list # Make sure we have the letter 'd'
['a', 'b', 'c', 'd']
>>> alphabet_list # lol
['a', 'b', 'c', 'd']
```

# String Operations

Strings are the literal representation of anything defined in single quotes `''` or double quotes `""`

- `in` and `not in` search strings
- `+` concatenates strings
- `[]` subsets and slices strings

# Strings and Slices

```python
>>> foo = 'Hello ' + 'World' # Concatenate the strings 'Hello ' and 'World' together
>>> foo # What do we get?
Hello World
>>> "ello" in foo # Search for 'ello' in `foo'
True
>>> foo[0] # What's the first letter of `foo'
'H'
```

# Python Quirks III: 0-Based, Partially Inclusive Counting

Python, like many other languages, is a 0-based language

```
 0  1  2  3  4  5
 |  |  |  |  |  |
 A  B  C  D  E  F
 |  |  |  |  |  |
-6 -5 -4 -3 -2 -1
```

Slices create a range that is bounded inclusively on the lower end and exclusively on the upper

```
[0:2] -> [0, 2) -> AB
[-5:-1] -> [-5, -1) -> BCDE
```

# Creating a Slice in Python

```python
>>> foo # What's `foo' again?
'Hello World'
>>> foo[2:] # Take all of `foo' from the 2nd index to the end
'llo World'
>>> foo[:7] # Take all of `foo' from the beginning up to, but not including, the 7th index
'Hello W'
>>> foo[-4:-2] # Take from the 4th to last index up to, but not including, the 2nd to last
'or'
```

# Changing the Step Sizes of a Slice

```python
>>> foo # What's `foo' again?
'Hello World'
>>> foo[2:7:2] # Take from the 2nd index up to, but not including, the 7th index in intervals of 2
'loW'
>>> foo[::-1] # Invert the string
'dlroW olleH'
>>> foo[8:3:-1] # Take from the 8th index up to, but not including, the 3rd index backwards by 1
'roW o'
```

# Pythonic Logic

- Python follows standard Boolean Logic
- `and` operators must have both sides be `True` to equate to `True`
- `or` operators must have one side be `True` to equate to `True`

```Python
>>> True and False # Because there's a `False', we get `False'
False
>>> True or False # Because there's a `True', we get `True'
True
```

# Boolean Conversions

In Python, some values get converted to `False` while others get converted to `True`

```python
>>> bool(0) # Convert 0 to its Boolean value
False
>>> bool(1) # Any numbers that aren't 0 convert to `True'
True
>>> bool('') # Empty strings are converted to `False'
False
bool('a') # Non-empty strings are converted to `True'
True
```

# Conditionals

| Keyword | Function |
| ------- | -------- |
| `while` | Start a while loop |
| `if` | Start and if/else statement: define code to run if and only if statement is `True` |
| `elif` | Create another condition to meet: `else` check `if` condition 2 is met |
| `else` | Define code to be run if and only if all conditions above are not met |
| `and` | All subcondiditions need to be `True` for entire condition to be `True` |
| `or` | Only one subcondtion needs to be `True` for entire condition to be `True` |
| `in` | Search for something in a larger thing |
| `is` | Determine if two objects refer to the same value, useful for dealing with referenced values |
| `not` | Negate the condition: if originally is `True`, become `False` and vice versa |

# If/Else Statements

```python
>>> foo # Paul likes comments
'Hello World'
>>> if 'll' in foo and 'rd' in foo: # Search for `ll' and `rd' in `foo'
...     print("Yes") # If both are present, print `yes'
... elif 'll' in foo or 'rd' in foo: # If only one of the two is present
...     print("Maybe") # Print `maybe'
... else: # If none of the above
...     print("No") # Print `no'
...
Maybe
```

# While Loops

```python
>>> x = -2
>>> y = 2
>>> while x <= y:
...    print ("X is now: ", x)
...    x = x +1
...
X is now: -2
X is now: -1
X is now: 0
X is now: 1
X is now: 2
```

# For Loops

```python
>>> foo
'Hello World'
>>> for i in foo[0:5]:
...     print(i)
...
H
e
l
l
o
```

# Functions and Methods

Both functions and methods do things, but methods are attached to an object

Functions are generic actions that can be used on different **types**
- All functions need at least one argument to act on

Methods are attached to objects, and restricted to specific **types**
- Some methods can be called without an extra argument, because they are attached to an object already

# Functions vs Methods

```python
>>> foo # What's `foo' again?
'Hello World'
>>> foo.find('ll') # The 'find' method of the object 'foo'
2
>>> find(foo, 'll') # There is no 'find' function
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'find' is not defined
>>>
>>> len(foo) # The standard function 'len'
11
>>> foo.len() # 'foo' has no method 'len'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'len'
```

# User Defined Functions

```python
>>> def string_concatenation(str1, str2): # Give the function a name and add arguments
...     con_str = str1 + str2 # Do something in our function
...     return(con_str) # Return an output value
...
>>> string_concatenation('Hello', 'World') # Call our function
'HelloWorld'
```

# Modules

Modules are a collection of code that expand the capabilities of Python

Some modules are included with a Python installation, but are not loaded by default

Load modules using the `import` statement

# Modules

```python
>>> import re # Import the `re' module, enabling regular expressions
>>> help(re) # Get help with the `re' module

>>> dir(re) # List all components to the `re' module
['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_alphanum_bytes', '_alphanum_str', '_cache', '_cache_repl', '_compile', '_compile_repl', '_expand', '_locale', '_pattern_type', '_pickle', '_subx', 'compile', 'copyreg', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'sys', 'template']
>>> regex = re.compile(r'(ll)') # Create a regex search object to look for 'll'
>>> match = re.search(regex, 'Hello World") # Search for 'll' in 'Hello World'
>>> match.groups() # Get the results
('ll',)
```

# Coding Challenge
## Download Example Code

`https://github.com/MorrellLab/DoesNaughtCompute`