# Ember Notes

## Links
[Components](http://www.programwitherik.com/ember-js-components-examples/)

## MVC Stuff
- controller is associated with 

## DS.Store - Model
- Essentially cache

### Functions
- [link of methods](https://emberjs.com/api/ember-data/2.15.3/classes/DS.Store/methods/)
- `store.query(itemName, queryParams)`: sends a GET request to the backend, URI handled in `adapter` file
- `store.filter(itemName, query, filter func)` gets itemNames currently in store and uses the filter function. Returns array
	- the `query` part just queries from backend whenever another record is added
	- the filter is cumulative!

## Handlebars
- .html is replaced with .hbs

- use `{{#each list do |item|}}` for enumeration
  - [link for limiting number of elements in ember component](http://www.falsepositives.com/index.php/2016/07/20/limiting-the-number-of-elements-displayed-in-a-ember-component/)


## Controllers/Components

**Difference:** Controllers are connected to routes (aka URI) while components are easily reused

- Allows for generic copy-able template
- Create component in .hbs
    - Example: {{about-profile twitter="http://www.twitter.com/erikch" name="John Smith" 
title="Engineer I" image="https://placekitten.com/g/200/300"}}
    - Define variable initialization values
    - Use handlebars
    - Allows calculation of computed properties (variables that are calculated when they are called)
    - **Block Form**: Allows usage of {{yield}}
      - preceded with # on .hbs
    - **Action Helper**: determines function on actions such as hover, click, etc. 
- classNameBindings - determines classes of component based on variable values

### Simple/Computed Properties
- `foo: computed(param, ..., function(){return 'bar'}`
- calculated once when called and cached
	- will only change if one of the passed parameters change
	- can also use observers
- `alias('thing')` - for simple properties to access other properties
- for computed properties, use `this.get('foo')`

### Actions
- actions are functions that are called when an interaction occurs
- defined on .hbs
- can pass in actions to child elements:

```ember
//parent .hbs
{{ child-component foo=(action 'sayHi') }}

//parent .js
actions: {
	sayHi() {
		console.log(Hi!);
	}
}

//child .hbs
{{ button onClick=(action 'sayHi') }}

//child .js
actions: {
	sayHi() {
		this.sendAction('sayHi', params...);
	}
}
```

### Controller + Route Relationship
- routes define URL (in master route.js file)
- define `model()`, which is data used by page
- page will wait for `model` before loading
- `controller.js` and `template.hbs` can access model
- controller can call router actions through `this.send('anAction', params...)`
- use `this.refresh()` or `this.modelFor(...path...).reload()` to refresh
- [Pagination using model()] (https://emberigniter.com/pagination-in-ember-with-json-api-backend/)