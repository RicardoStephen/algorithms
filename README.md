Algorithms
==========
A library of data structures and algorithms.


Contents
--------

datastructs
+ String, Array, ArrayList
+ LinkedList, Deque
+ HashMap, HashSet


Usage
-----

```
>>> import datastructs
>>> x = datastructs.LinkedList()
>>> x.append(1)
>>> print(x)
```


Tests
-----

```
# Discover all tests
python3 -m unittest discover tests

# Run specific test module/case/method
python3 -m unittest tests.test_string # .TestString.test_len
```
