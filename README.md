Algorithms
==========
A minimal library of data structures and algorithms.


Contents
---------

```
algorithms
    datastructs
        String    : len, getitem
        Array     : len, getitem, setitem
        ArrayList : len, getitem, setitem
                    append, extend, pop
        
        LinkedList : appendleft, popleft, iter
        Deque      : appendleft, popleft
                     append, extend, pop
                     iter, reversed
        
        HashMap    : getitem, setitem
        HashSet    : add, remove, contains
    graphs
        BinaryTreeNode : init, str
                         inorder, preorder, postorder
        Heapq          : heapify, heappush, heappop
        GraphDict      : breadthfirst, depthfirst
                         bidirectional
```


Usage
-----

```
>>> import algorithms
>>> x = algorithms.datastructs.Deque()
>>> x.appendleft(1)
>>> x
deque([1])
```


Tests
-----

```
# Discover all tests
python3 -m unittest discover test

# Run specific test module/case/method
python3 -m unittest test.test_string # .TestString.test_len
```
