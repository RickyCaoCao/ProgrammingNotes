# Ruby on Rails Notes

# MVC (Model-View-Controller)

**Model aka. ActiveRecord**: Database interface. Handles relationship between objects and database. For validation, transactions, etc.

**View aka. ActionView**: Determines how objects are displayed

**Controller aka. ActionController**: Takes the data presented by the model and fits it to the view. Manages user interaction.

## Model/ActiveRecord
**3 Types of Association between Models**:

1. One-to-One
2. One-to-Many
3. Many-to-Many

**Association Methods**:

1. has_one: parent of child (for one-to-one)
2. belongs_to: child of parent (for one-to-one and many-to-one)
3. has_many: parent to children (for one-to-many)
4. has_and_belongs_to_many: parent to parent (for many-to-many)

**Validation** - Rails provides validation methods for input fields

**More Methods**

1. **scope**: associates a symbol to method. essentially a query that narrows down the database
  - scope :red -> {where(color: 'red')}

## Controllers
- inherits from `ApplicationController`

###Filters
- Methods that are ran before, after, and around controller action
- Filters are inherited so be careful
- **before** filter
  - may halt request cycle
  - ex. check if user is logged in
  
  ```
  before_filter :require_login
  ```
  
- **skip_filter**: skip a filter for certain actions
  
  ```ruby
  skip_filter :require_login, only: [:new, :create]
  ```

- **around/after filters**: can be used for confirmation from user (careful because action is in mid process or already happened)
  
## Views
- contains HTML and handles what certain actions defined by the controller do
- **Layouts**: templates of view for controllers

## Objects
### Attributes
- **attr_accessor** = read + write
- **attr_reader** = read only
- **attr_writer** = write only

### Alias_Methods
- use alias_methods rather than alias
- another name for already defined method
- allows for extension of methods and etc.
  - see https://wikimatze.de/method-alias-in-ruby/

## Symbols
- [Relevant Link](http://www.rubyfleebie.com/an-introduction-to-symbols/)
- **Strings are about content. Symbols are about meaning**
- an object that is essentially a String but allows two variables to point to this one object rather than point to two separate springs
- we do not assign to symbols

### Usage
- No need to instantiate, use it like it already exists
- Use it as a hash for an object
  - animals[:dog] = “charlie”

## Modules
### Links
[Benefits of Modules](http://phrogz.net/programmingruby/tut_modules.html)


### Namespaces
- prevents conflicts from namespacing (ie. two methods with the same name)

### Mixins
- classes can use module's instance methods as it's own
- saves from multiple inheritance
- e.g. just define `a <=> b` in `Comparable` module to use it's comparison functions

## Methods
- redirect_to: automatically forwards the page without user interaction


## Lambda Function
- nameless function
- allows a function to return another function (think js where a variable can equal a function)
- https://stackoverflow.com/questions/16501/what-is-a-lambda-function

## Scaffolding
- quickly create a Model, View,Controller for easy demos

## Style
- Pascal Case for models, controllers,
- Also make it singular

### Unless
- `return a unless b` better than `return a if !b`
- checking one condition (not using else)
- checking multiple conditions in unless