---
title: Easy to comprehend - Comprehensions
status: drafty
# number: 12
---

### list

Using comprehensions make a list containing numbers from 1 to 10.

Read [this]({   { site.baseurl }}/misc/lorem) file word by word, using comprehensions build a new list that contains the length of every word.

Write a function that, given two lists, builds the cartesian product of the lists with tuples.[^nested]

```python
>>> function([1,2,3], [6,7,8])
[(1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8), (3, 6), (3, 7), (3, 8)]
```

Try it with the two lists you've created earlier.

[^nested]:
    Comprehensions can be nested!!!

### dict

Use dict comprehension to map every word of the text to it's length.

### generator

Try the above by calling the `dict()` function on a (new) generator comprehension of tuples (the generator should generate tuples).