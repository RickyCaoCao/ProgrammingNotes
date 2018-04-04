#Javascript

## Variable Definition

- can use variable to evaluate a function
- var a = ...

### Using Variable Inside String
- works for ES6
- use backticks (rather than quotes)
- use ${var}
- Ex:

```javascript
var foo = 'World!';
console.log(`Hello ${foo}`);
```

### var vs. let vs. const
Link: https://madhatted.com/2016/1/25/let-it-be

#### Scoping
- `var` is scoped to a function
- `let` is scoped to a block (if/else, while, etc.)

Problem with `var`:

``` javascript
for (var i = 0; i < 10; i++){ ... }
console.log(i) //outputs 10
```

#### Variable Re-declaration
- `let` does not allow variable to be re-declared
	- Does NOT work:
	
	``` javascript
		let a = 'hi';
		let a = 'bye';	
	```
	- can be re-assigned:

	``` javascript
		let a = 'hi';
		a = 'bye';
	```

- `const` objects cannot be reassigned but their properties can

## Useful Functions
**Array.prototype.map()**: Modifies each element of an array and makes new array

```javascript
var new_array = arr.map( (currentItem [, index [, origArray]]) {
	//do something
}
```

## Callback Functions
- js is single-threaded so callback functions will run after other code has finished
- The function in `foo` below is a callback

```javascript
foo(param_a, param_b, function (){ ... })
```
### Callback Hell / Pyramid of Doom
- not sure if variables are defined
- nested upon nested functions

### Ways to Avoid Callback Hell
- [Using Polling](https://stackoverflow.com/questions/9121902/call-an-asynchronous-javascript-function-synchronously)
- [General Avoidance](http://stackabuse.com/avoiding-callback-hell-in-node-js/)
- [Using Promises?](https://glebbahmutov.com/blog/passing-multiple-arguments-in-promises/)
- [f*** promises](http://stevehanov.ca/blog/index.php?id=127)

To ensure that callback function resolves before running something else, don't do

```javascript
function foo (int_a, int_b){
	return <some_api_call_with_return>;
}

let number = foo(1, 2);
```
because number might not resolve. Instead, do

```javascript
function foo(int_a, int_b, callback){
	callback(<some_api_call_with_return>);
}
let number;

foo(1, 2, function(returned_num){
	number = returned_num;
}

```

## Node.JS Libraries
- .dotenv - for local environment variables
- qs - for querystring
- JSON
