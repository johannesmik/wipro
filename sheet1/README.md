Exercise sheet 1
================

This is our very first python exercise sheet :)

Here, I try to give you a guidance through the exercises, especially highlighting some common pitfalls. However, I recommend you to first try all the exercises by yourself, before reading this guide.

Repetition
----------

In the first exercise sheet you practice to:
- create new Python programs
- run programs
- assign values to variables with **=**
- use mathematical operators: ** + - \* / \*\* %**
- **print** text to your terminal output
- use the math library: **math.pi, math.sqrt()**
- use control flow: **if, else, elif**
- generate number sequences: **range()**
- repeat code blocks: **for, while**
- create random numbers: **random.random()**

Now I'm going to repeat those.

### Assign values to variables with **=**

You can assign values to a variable using the **=** operator.

The name of the variable comes to the left side, and the value to be assigned on the right side.

For example, this assigns the integer value `5` to the variable called `age`:

```python
age = 25
```

This assigns the string value `Hello` to a variable called `message`.

```python
message = "Hello"
```

Note that strings have to be enclosed with `"` or `'`.

The next one assigns the float value `3.1415` to a variable called `pi`.

```python
pi = 3.1415
```

On the right side you can also write more complex statements, like computations. Note that those computations might involve other variables:

```python
area = pi * 2 ** 2
```

Python also offers so-called "[augmented assignments](https://docs.python.org/2/reference/simple_stmts.html#augmented-assignment-statements)".

That is the expression `x = x + 1` can be written as `x += 1`. Another example: `y = y - 5` is the same as `y -= 5`.

```python
x += 5
```
This increases the variable called `x` by 5.

### Mathematical operators: ** + - \* / \*\* %**

In Python you have the following operators available:

- Addition **+**
- Subtraction **-**
- Unary minus **-**
- Multiplication **\***
- Power **\*\***
- Modulo/Remainder **%**
- Division **/**

The use of them should not be too hard:

```python
>>> 5 + 5
10
>>> 5 - 3
2
>>> - 3
-3
>>> 5 * 4
20
>>> 2 ** 4
16
>>> 10 % 3
1
```

But notice, that the division operator behaves differently! If both values are **integers** it will do an **Integer Division**. If at least one value is a **float** it will do a **Float Division**:

```python
>>> 10 / 3
3
```
The `10` and `3` are both integers, therefore **Integer Division**.

```python
>>> 10.0 / 3
3.3333333333333335
```

The `10.0` is a float, `3` is an integer. So at least one value is a float, therefore **Float Division**.


### the **print** statement

You can output text to your console with the `print` statement.

The most famous example is the "Hello World!" program:

```python
print "Hello World"
```

You can easily combine the output using a comma:

```python
print "1 plus 1 is ",  1 + 1
```

This program will print `1 plus 1 is 2` to the console.

After each print statement a new line is started, for example:

```python
print "Hello, World!"
print "Today's nice weather, isn't it?"
```

Will print to the console:

```
Hello, World!
Today's nice weather, isn't it?
```

You can suppress the print statement from starting a new line by writing a comma to the very end:

```python
print "Hello, World!",
print "Today's nice weather, isn't it?"
```

This will print everything to a single line:

```
Hello, World! Today's nice weather, isn't it?
```

### Using the **math** module

For a complete overview of all available functions see: [Math Documentation](https://docs.python.org/2/library/math.html)

First you have to import the math module

```python
import math
```

Then you can use constants and functions of it:

```python
print math.pi
print math.sqrt(2)
```

My favorite selection of math functions:

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
```

### Control flow **if, else, elif**

Examples:

```python
age = 17
if age >= 18:
    print "You are older than 18."
else:
    print "You are younger than 18."
```

An indentation of 4 spaces (that's the common rule) is used to define blocks of statements.

Consider the next two examples:

```python
if 1 > 3:
    print "hello",
    print ", world."
```

The output is ` ` (empty).

```python
if 1 > 3:
   print "hello",
print ", world."
```

The output is `, world`. Because the latter print statement is not part of the if code block.

There's also the **elif** statement. Basically, it enables you to combine an *else* with a condition. Example:

```python
age = 18
if age > 18:
  print "You are older than 18."
elif age == 18:
  print "You are 18."
else:
  print "Your are younger than 18."
```

### Number sequences with **range()**

Using the [range](https://docs.python.org/2/library/functions.html?highlight=range#range) function you can create sequences of numbers:

The function takes 3 parameters: Start (default=0), Stop, Step (default=1).

```python
>>> range(10)     # Stop: 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(3, 8)   # Start: 3, Stop: 8
[3, 4, 5, 6, 7]
>>> range(2, 10, 2) # Start: 2, Stop: 10, Step: 2
[2, 4, 6, 8]
```

### Repeat code blocks **for, while**

Example for loop:

```python
for i in range(1, 5):
  print i, i**2
```

Which outputs:
```
1 1
2 4
3 9
4 16
```

The same as a while loop:

```python
i = 1
while(i < 5):
  print i, i**2
  i += 1
```

This also outputs:
```
1 1
2 4
3 9
4 16
```

Most for loops can be rewritten as while loops. However, most of the time the for loop will be more readable.

### Random numbers with **random.random()**

You can use the `random()` function from the `random` ([documentation](https://docs.python.org/2/library/random.html)) module to create random floats between 0.0 and 1.0:

```python
>>> import random
>>> random.random()
0.30483000659768067
>>> random.random()
0.7702909925259085
>>> random.random()
0.7702909925259085
```

You can use the `randint(start, stop)` function to create random integers between a defined interval:

```python
>>> import random
>>> random.randint(1, 3)
3
>>> random.randint(1, 3)
1
>>> random.randint(1, 3)
2
```


Drill exercises
---------------

You can try those very simple exercise at home.

### Operators

Complete the following program by replacing the `#TODO` comment with the actual code.

```python

import math

n = 5
print "n is ", n
print "n plus one is ", n + 1
print "n minus one is ", #TODO
print "three times n is ", #TODO
print "twice n is ", #TODO
print "n squared is ", #TODO
print "n raised to the power of 4", #TODO
print "half of n is ", #TODO
print "the remainder of n/2 is ", #TODO
print "n times pi is ", #TODO
print "square root of n is ", #TODO
```

### For loops 1

Write a program that writes all numbers from 1 to 15 to the screen.

### For loops 2

Write a program that writes all even numbers from 2 to 20 to the screen.
