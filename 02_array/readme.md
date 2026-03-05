# 📘 Array in Python

## 📌 Introduction

An **Array** is a data structure used to store multiple values in a single variable.

All values in an array are stored in **continuous memory locations**.

Arrays are useful when we want to store **many values of the same type**.

Example:

```
10, 20, 30, 40, 50
```

Instead of creating many variables, we store them in one array.

---

# 🔹 What is an Array?

An **Array** is a collection of elements stored at **contiguous memory locations**.

Key points:

* Stores **multiple values**
* Elements are stored **in order**
* Elements are accessed using **index**
* Usually stores **same data type**

Example concept:

```
Index : 0   1   2   3
Value : 10  20  30  40
```

To access element:

```
array[0] → 10
array[2] → 30
```

---

# 🔹 Types of Arrays in Python

Python mainly provides two ways to work with arrays:

1. **array.array (Built-in module)**
2. **NumPy Array (numpy library)**

---

# 1️⃣ array.array in Python

Python provides an **array module** to create arrays.

It is useful when we want **memory-efficient arrays**.

Unlike lists, `array.array` stores **only one data type**.

---

## Importing array module

```
from array import array
```

---

## Creating an Array

Syntax:

```python
array(typecode, elements)
```

Example:

```python
from array import array

numbers = array('i', [10, 20, 30, 40])

print(numbers)
```

Output

```
array('i', [10, 20, 30, 40])
```

---

## Type Codes

Type code defines **what type of data the array stores**.

Common type codes:

| Type Code | Data Type                                               |
| --------- | ------------------------------------------------------- |
| 'i'       | integer                                                 |
| 'f'       | float                                                   |
| 'd'       | double                                                  |
| 'b'       | signed char                                             |
| 'u'       | unicode character (deprecated in newer Python versions) |

Example:

```python
array('f', [1.2, 2.4, 3.6])
```

---

## Accessing Elements

```python
from array import array

numbers = array('i', [10, 20, 30, 40])

print(numbers[0])
print(numbers[2])
```

Output

```
10
30
```

---

## Common Array Operations

### Add element

```python
numbers.append(50)
```

### Insert element

```python
numbers.insert(1, 15)
```

### Remove element

```python
numbers.remove(30)
```

### Loop through array

```python
for num in numbers:
    print(num)
```

---

## Advantages of array.array

* Uses **less memory than list**
* Faster when working with **large numeric data**
* Enforces **same data type**

---

## Limitations

* Stores **only one type of data**
* Less flexible than Python lists
* Not used in advanced data science work

For advanced numerical computing, Python developers use **NumPy arrays**.

---

# 2️⃣ NumPy Array

NumPy stands for **Numerical Python**.

It is a powerful library used for:

* Data Science
* Machine Learning
* Scientific Computing
* Large numerical operations

NumPy arrays are **much faster and more powerful** than normal Python arrays.

---

## Installing NumPy

```
pip install numpy
```

---

## Importing NumPy

```python
import numpy as np
```

---

## Creating a NumPy Array

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)
```

Output

```
[10 20 30 40]
```

---

## Multi-Dimensional Arrays

NumPy can easily create **2D and 3D arrays**.

Example 2D array:

```python
import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr)
```

Output

```
[[1 2 3]
 [4 5 6]]
```

---

## NumPy Array Properties

Example:

```python
print(arr.ndim)   # number of dimensions
print(arr.shape)  # rows and columns
print(arr.size)   # total elements
print(arr.dtype)  # data type
```

---

## Advantages of NumPy Array

* Very **fast calculations**
* Supports **multi-dimensional arrays**
* Used in **data science and machine learning**
* Efficient **memory usage**
* Provides many **mathematical functions**

---

## Example Mathematical Operation

```python
import numpy as np

arr = np.array([1,2,3,4])

print(arr * 2)
```

Output

```
[2 4 6 8]
```

NumPy performs operations **element-wise**.

---

# 🔎 Difference Between List, array.array and NumPy Array

| Feature           | List     | array.array | NumPy Array    |
| ----------------- | -------- | ----------- | -------------- |
| Data Type         | Multiple | Single      | Single         |
| Speed             | Medium   | Faster      | Very Fast      |
| Memory Usage      | High     | Low         | Very Efficient |
| Multi-Dimensional | No       | No          | Yes            |
| Data Science Use  | No       | No          | Yes            |

---

# 🎯 Conclusion

Arrays are used to store **multiple values efficiently**.

Python provides two main array options:

**array.array**

* Simple
* Memory efficient
* Stores single data type

**NumPy Array**

* Very powerful
* Fast calculations
* Used in Data Science and Machine Learning

For **DSA learning**, `array.array` is enough.
For **Data Science**, NumPy arrays are preferred.

