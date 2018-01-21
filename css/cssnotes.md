# CSS Notes

## Combinators
- Space = descendant
- `>` = immediate child
- `+` = adjacent sibling
- `~` = general sibling

## Selectors
For selecting elements to style: <https://www.w3schools.com/cssref/css_selectors.asp>

## Niche
- Clicking on a button is both :focus and :active state
  - Define :active after :focus in order to get a different state 

  
## BEM - Block, Element, Modifier
https://css-tricks.com/bem-101/
Naming convention for HTML/CSS
- use `__` for child elements
- use `--` for modifications to style

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