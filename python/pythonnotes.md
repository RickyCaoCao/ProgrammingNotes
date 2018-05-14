# Python Notes

## Python vs Java

### Features in Python

[Stack Overflow Reference](https://stackoverflow.com/questions/49824/java-python/49953#49953)

1. **Everything is an object**

2. **[Line Comprehensions](http://www.pythonforbeginners.com/basics/list-comprehensions-in-python)**: ` some_list = [expression(i) for i in some_list if filter(i)]`

   - Ex:

     ```python
     a_list = [num^3 for num in old_list if item < 5]
     ```

3. **Function Objects**

   - can be passed as parameters
   - lexical scope
   - created when we use `def` or `lambda` expression

4. **[Lambda](https://www.python-course.eu/lambda.php)**

   - anonymous function (used and discarded)

     ``` python
     f = lambda x, y : x + y
     >>> f(1,2) # returns 3
     ```

   - useful for `map(func, seq)`, `list.sort([func])`, `filter(func, list)`, `reduce(func, seq)`

5. **[\__call__](https://stackoverflow.com/questions/25292239/are-functions-objects-in-python)**

   - the default operation to call a function

   - can define `def __call__(self, ...)` within Class to customize a class

     ```python
     def foo(name): print("Hello {}".format(name))
     ...
     >>> foo("Rick") # foo.__call__("Rick") is what it becomes after compiler
     "Hello Rick"
     ```

   - can define `def __call__(self, ...)` within Class to customize a class

    ```python
   class Callable(object):
    	def __init__(self, name):
    		self.name = name
   
   	def __call__(self, greeting):
   		return '{}, {}!'.format(greeting, self.name)
   
   >>> Callable('World')('Hello') 
       # instantiates object with self.name as "World"
       # then subsequently calls the function with "Hello" as greeting
    ```

6. **\__dict__**

   - a dictionary that stores all the properties of an object

7. **[Built in getter/setter/etc.](https://www.programiz.com/python-programming/property)**

   - Use `property(getter=None, setter=None, del=None, docstring=None)`
   - Alternatively, use attributes (@property, @\<property_name>__.setter)

8. **Default and Keyword Arguments**

   - default arguments: `def foo(num=5)`
   - keyword arguments (for invoking)>: `foo(num=10)`

9. **Tuple Variable Assignment**

   - if `foo()` returns 2 numbers, then we can `a,b = foo()` to set vvars

### Common Mistakes When Going Java -> Python

- static method is better as a Python module-level method (rather than classmethod)
  - class attributes are looked up during runtime in Python, which is a lot slower than Java, as that is done during compilation
- use Python dictionary as a switch statement (as we can pass in function objects as the values)
- don't use XML
- don't write getters and setters
  - only use @property when needed to have a modified get/set
- use "closures" rather than function overloading
  - that means using an outer function to return an inner function
  - the inner function takes in all variables that are needed for function overloading

## Closures

### Basics: Nested Function

- inner function can access variables of enclosing scope
  - these variables are called "non-local" and are read-only
  - to modify these variables, we must explicitly declare them using "nonlocal" keyword

``` python
def outerFunction(text):
    text = text
    
    def innerFunction():
        print(text)
    
    innerFunction()

outerFunction("Hello World")
>>> "Hello World"
```

### Closures

- creating a meta-function (that can generate another function)

  ``` python
  def make_multiplier_func(n):
      def multiply(x):
          return x*n
      return multiply
  
  times3 = make_mulitplier_func(3)
  times5 = make_mulitplier_func(5)
  
  print(times3(2)) 	#6
  print(times5(5)) 	#25 
  print(times3(4)) 	#12
  ```

- use `times3.__closure__`  returns a tuple of cell objects

  - to access the argument that was passed in:

    `times3.__closure__[0].cell_contents`

- closures are for avoiding global values, data hiding, and function overloading

- Example:

  ``` python
  def logger(func):
      def log_func(*args):
          logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
          print(func(*args))
      
      return log_func
  
  add_logger = logger(lambda x, y : x + y)
  add_logger(3, 4)	# gives 7
  ```

  

## Data Structures

**Lists**

- `colours = ["red", orange", "yellow", "green", "blue", "indigo", "violet"]`

- mutable

- negative indexing

- Length: `len(colours)`

- Adding Element: `colours.append("gray")`

- Removing elements:

  - ```python
     del a_list[1] # would remove "orange"
    ```

  - ``` python
    colours.remove("indigo") # would remove "indigo"
    ```

  - ``` python
    colours.pop(3) # would remove "green"
    ```

- Concatenate lists: 

  - ```python
    colours + ["turquoise"] # appends and changes 'colours'
    ```

- Slicing: `colours[2:4]`

- 

**Arrays**

- [See numpy](http://cs231n.github.io/python-numpy-tutorial/#numpy)
- uses a lot less space than lists
- good for doing math

## Classes

### Properties

**Private:** Use `_` before a variable to denote that it is private

- `self._secret`
- this is a convention -- python does not apply any restrictions 

## Other Notes

**Lexicon/Static Scoping:** variables can only be used within initiation block (e.g. private vars)

**Dynamic Scoping:** variables that can be used anywhere
```

```