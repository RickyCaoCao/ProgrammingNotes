# CSS Notes

## Selectors
For selecting elements to style: <https://www.w3schools.com/cssref/css_selectors.asp>

## Niche
- Clicking on a button is both :focus and :active state
  - Define :active after :focus in order to get a different state 

# SASS Notes

## Summary
Easier way to write css. Will compile into css.

* .css is replaced with .scss

### Tricks
**& Selector**

Goal: Easy nesting
Usage: When compiled, replaces & with parent
Example: 

``` SCSS
a {
  font-weight: bold;
  text-decoration: none;
  &:hover { text-decoration: underline; }
  body.firefox & { font-weight: normal; }
}
```

is compiled to:

```
a {
  font-weight: bold;
  text-decoration: none; }
  a:hover {
    text-decoration: underline; }
  body.firefox a {
    font-weight: normal; }
}
```


## Links
Reference: http://sass-lang.com/documentation/file.SASS_REFERENCE.html