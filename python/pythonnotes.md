# Python Notes

## Python vs Java

### Features in Python

[Stack Overflow Reference](https://stackoverflow.com/questions/49824/java-python/49953#49953)

1. **Everything is an object**

2. **[List Comprehensions](http://www.pythonforbeginners.com/basics/list-comprehensions-in-python)**: ` some_list = [expression(i) for i in some_list if filter(i)]`

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

- 

## Data Structures

**Booleans: ** True/False (notice capitals)

**Strings**

- essentially list of chars so list functions work most of the time
- length: `len(a_str)`
- slicing: `a_str[ left : right : skips ]`
- `a_str[::]` means string as is 
- `a_str[::-1] ` means string reversed
- Split phrase on whitespace: `a_str.split()`
- Split phrase on letter 't': `a_str.split('t')`
- Join list of strings with space in between: `' '.join(str_list)`
- Strip whitespaces, trailing characters, newline: `a_str.strip()`
- `\` is escape character

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

- Converting sequence (string, tuples) to list: `list([iterable])`

  - Can also be collection (set, dictionary) or iterator

**Sets**

- A list without duplicates

- Use `&` and `|` for intersection and union of sets, respectively

  - This is faster than list comprehension (see `ex5.py`)

  - ``` python
    set(a) & set(b) # faster
    set([n for n in a if n in b]) # slower
    ```

**Arrays**

- [See numpy](http://cs231n.github.io/python-numpy-tutorial/#numpy)
- uses a lot less space than lists
- good for doing math

**Dictionaries** (aka hashmaps)

- add key: `dict['newkey'] = 3`
- get key: `dict['some_key']`
  - better way: `dict.get('some_key', 'failback_val')`
    - prevents crashing if key doesn't exist
- get all keys: `dict.keys()`
- get all key-value pairs: `for pair in dict.items():`

## Classes

### Properties

**Private:** Use `_` before a variable to denote that it is private

- `self._secret`
- this is a convention -- python does not apply any restrictions

**Type Checking:**

- `num.isDigit()`
- or `type(num) is int`

## Common Functions

`raw_input(...)` takes user input

- don't use `input(...)` as that runs `eval()` on the argument

`for i in range(left_incl, right_excl):`

- better than while loop

try/except == try/catch in Java

`map(func, list)` = returns a list where `func` runs on each element of `list`

### File I/O

- use `with` statement to automatically close the file -- good if program crashes as file will close and not be in memory

``` python
with open(f_name, 'w') as open_file:
    open_file.write("Hello World!")
```

**Modes:**

- `r` = read
- `w` = write
- `r+` = read + write

**Reading Files:**

- best method: `for line in open_file:`
- `open_file.readline()` - reads one line
- `open_file.read()` - reads entire file and returns string
- `open_file.readlines()` - reads entire file and returns list of strings (each line is a string)

**Writing Files:**

- opening existing file will automatically delete
- can only write strings

## Useful Libs

- random - RNG
  - `random.sample(a_list, num_of_samples)` take `a_list`  samples `num_of_samples` times
- requests - calls APIs :)
- BeautifulSoup - web scraper, parses html. Needs requests
- Scrapy - can both get and scrape web pages
- json
  - writing to json file: `json.dump(json_obj, open_file)`
  - reading from json file: `json.load(open_file)`

## Other Notes

### Closures

**Basics: Nested Function**

- inner function can access variables of enclosing scope
  - these variables are called "non-local" and are read-only
  - to modify these variables, we must explicitly declare them using "nonlocal" keyword

```python
def outerFunction(text):
    text = text
    
    def innerFunction():
        print(text)
    
    innerFunction()

outerFunction("Hello World")
>>> "Hello World"
```

**Closures**

- creating a meta-function (that can generate another function)

  ```python
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

  ```python
  def logger(func):
      def log_func(*args):
          logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
          print(func(*args))
      
      return log_func
  
  add_logger = logger(lambda x, y : x + y)
  add_logger(3, 4)	# gives 7
  ```

### Scoping

**Lexicon/Static Scoping:** variables can only be used within initiation block (e.g. private vars)

**Dynamic Scoping:** variables that can be used anywhere



### if \__name__ == "\_\_main__": 

- to deal with importing issues
- without `if __name__ == "__main__":`, the file will run on `import` 