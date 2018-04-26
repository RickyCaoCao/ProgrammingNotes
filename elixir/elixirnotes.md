# Elixir Notes

- parentheses can be removed for functions
- data structures are immutable

**The Little Elixir & OTP Guidebook**
Actor == Genserver
Genserver.call is sync, Genserver.cast is async
`handle_cast`, `handle_call`
Genserver.start_link = associating genservers with supervisors and etc.
Supervisor strategies
  - manages when to restart actors
:observer.start
<https://github.com/TylerPachal/introduction_to_actors>

## Data Types
- integer (both arabic 1 and binary/octal/hex 0x1F)
- float 1.0
- boolean true/false
- atom :atom (aka symbol)
- string ""
  - String Interpolation: `"hello #{:world}"`
  - String concatenation: `iex> "foo" <> "bar"`
  - double quote "" is string, single quote '' is charlist
- list []
  - use `++` and `--` to concatenate and subtract operators
  - Head: `hd`, Tail: `tl`
  - Lists are Linked Lists (better for iteration)
- tuple {}
  - Tuples are arrays (better for direct access)
- Aliases
  - uppercase, also considered atoms (eg. `Hello`)

Checks: `is_boolean()`, `is_float()`, `is_integer()`, etc.

Use `i` to retrieve info <br>
Example: `iex> i 'hello'`

There is a `<` and `>` order between data types

Speed Comparison: <https://medium.com/learn-elixir/speed-up-data-access-in-elixir-842617030514>

## Functions
- print = `IO.puts(<string>)`
- use `or`, `and`, `not` if expecting booleans, otherwise use `||`, `&&`, `!`
  - The former operators only execute right side if left side is not enough

### Anonymous Functions
Inline functions

- function can be passed as argument (like js)
- must use dot after name to invoke function
- global variables will not be changed in function

Example:

```elixir
iex> add = fn a, b -> a + b end
iex> add.(1, 2)
3
```

```elixir
iex> x = 3
iex> (fn -> x + 3 end).()
6
```

### Multiple Functions

```elixir
some_var = foo(a,b)
|> bar
```
means pass in returned value from `foo` to `bar` and then assign returned value from `bar` to `some_var`


## Modules
- String

### Alias vs Require vs Import
**Alias:**
- allows for name shortening (e.g. Shared.Function -> Function)

**Require vs Import**
- use import because more flexibility and automatically requires