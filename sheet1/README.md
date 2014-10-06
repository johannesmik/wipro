Exercise sheet 1
================

This is our very first python exercise sheet :)

Here, I try to give you a guidance through the exercises, especially highlighting some common pitfalls. However, I recommend you to first try all the exercises by yourself, before reading this guide. 

Python as a calculator
----------------------

In this exercise we learn about:

- creating new Python programs
- running programs
- variables
- mathematical operators (addition, subtraction, multiplication, division)
- the print statement

### Important comments

#### Variable names

You can be very creative inventing new variable names. However, there is a very famous saying "code is read more than it is written". Always try to pick descriptive variable names, such that others can easily understand your code.

In our example, the variable name "F" is better than something like "a" or "blub". Even more better might be something like "fahrenheit", or "fahrenheit_temperature", because it indicates the use of the variable better.

#### Integer Division versus Float Division

Maybe you noticed that the "/" division operator does not work always as you would expect. Let's look what happens when we divide 10 by 4:

```python
>>> 10 / 4
2
```

What is that??? Our python interpreter says that the result of "10/4" is 2, and not 2.5! Crazy, why is that? Well, Python treats "10" and "4" as integers (dt. Ganze Zahlen) and not as floats (dt. Fließkommazahlen). Therefore, the statement "10/4" is treated as a "integer division" and we get the result "2". But our expected behavior is a "float division" and get the result"2.5".

One solution for this is to explicitly write at least one number as a float by using an additional point: **3** (Integer) -> **3.0** (Float), or by using the float() function **float(3)**.

```python
>>> 10.0 / 4
2.5

>>> 10 / 4.0
2.5

>>> 10.0 / 4.0
2.5

>>> float(10) / 4
2.5
```

Another solution is to use a special import statement at the beginning of the file: "from __future__ import division". This overwrites the default behavior of the "/" operator to *Float division*. Integer division is still available with the "//" operator. By the way, this is the way that Python3 handles division, which might explain the "from __future__" part.

```python
>>> from __future__ import division

>>> 10 / 4
2.5

>>> 10 // 4
2
``` 

The math library
----------------

You'll learn about:

- math.pi
- math.sqrt()
- the operator ** for the power.

### Contents of the math module

In this tutorial we use a very small subset of the math module, namely the Pi constant and the squareroot function. But the math module has so much more to offer! At this point you can have a look at the [documentation of math library](https://docs.python.org/2/library/math.html?highlight=math#module-math).

My very own selection of math highlights in this module is:

```python
>>> import math
>>> math.ceil(3.4)
4.0

>>> math.e
2.718281828459045

>>> math.exp(1)
2.718281828459045

>>> math.log(16)
2.772588722239781

>>> math.log(16,2)
4.0

>>> math.sin(1)
0.8414709848078965

>>> math.degrees(math.pi/2.0)
90.0
The operator "**" is the power operator. For example:

```python
>>> 3 ** 2
9

>>> 2 ** 8
 256
```

Aggregate state of water
------------------------

In this exercise you can practice the if-then-else control flow. You should know this by heart :)

For our exercise the control flow looks like this:

Check if the temperature is over 100 degrees. If yes the state is "Air". If not, check if the temperature is over 0 degrees. If yes, the state is "Liquid". If not, the state is "Solid".

Sometimes it may be helpful to draw the control flow. We did this in the exercise on the whiteboard.

Remember that Python knows the "elif *condition*:" statement. Its an else with an additional condition.

Bizz Buzz Woof
--------------

In this exercise you'll learn:

- the for statement to iterate over a sequence of numbers
- the range function to generate a sequence of numbers
- the modulo operator "%"


Monte Carlo approximation of Pi
--------------------------------

You'll learn how to:

- create random numbers
- while loops

### Augmented assignments

Python offers so-called "[augmented assignments](https://docs.python.org/2/reference/simple_stmts.html#augmented-assignment-statements)". 

That is the expression `x = x + 1` can be written as `x += 1`. 

Another example: `y = y - 5` is the same as `y -= 5`.
