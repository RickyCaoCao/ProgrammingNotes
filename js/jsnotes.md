#Javascript

## Variable Definition

- can use variable to evaluate a function
- var a = ...


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