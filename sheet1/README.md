Exercise sheet 1
================

This is our very first python exercise sheet :)

Python as a calculator
----------------------

In this exercise we learn about:

    - creating new Python programs
    - running programs
    - variables
    - mathematical operators (addition, subtraction, multiplication, division)
    - the print statement

### Important comments

#### Integer Division versus Float Division

The "/" division operator 

```python
>>> 10 / 3
3
```

One solution for this is to explicitly write at least one number as a float by using the point notation: **3** (Integer) -> **3.0** (Float)

```python
>>> 10.0 / 3
3.3333333333333335

>>> 10 / 3.0
3.3333333333333335

>>> 10.0 / 3.0
3.3333333333333335
```

Another solution is to use a special import statement at the beginning of the file. This overwrites the default behavior of the "/" operator to *Float division*. Integer division is still available with the "//" operator.

```python
>>> from __future__ import division

>>> 10 / 3
3.3333333333333335

>>> 10 // 3
3
``` 

