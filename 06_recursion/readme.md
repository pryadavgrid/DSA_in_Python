# 📘 Recursion in Python

## 🔁 What is Recursion?

Recursion is a technique where a function **calls itself** to solve a problem.

Instead of using loops, recursion breaks a problem into **smaller sub-problems**.

---

## 🔑 3 Important Parts of Recursion

### 1. Starting Point

* The initial input where recursion begins
* Example: `factorial(5)`

---

### 2. Recursive Logic

* The rule that reduces the problem
* Example:

```python
return n * factorial(n - 1)
```

---

### 3. Base Condition (Stopping Condition)

* The condition where recursion **stops**
* Prevents infinite loop

```python
if n <= 1:
    return 1
```

---

## 📊 Example 1: Factorial

### 🔢 Explanation:

Factorial of a number `n` is:

```
n! = n × (n-1) × (n-2) × ... × 1
```

### 💻 Code:

```python
def factorial_of_number(my_num):
    if my_num <= 1:
        return 1
    
    return my_num * factorial_of_number(my_num - 1)
```

### ⏱ Time Complexity:

* **O(n)**

---

## 📊 Example 2: Fibonacci Series

### 🔢 Series:

```
0, 1, 1, 2, 3, 5, 8...
```

### 💻 Code:

```python
def fibonacci_series(my_number):
    if my_number <= 0:
        return 0
    
    if my_number == 1:
        return 1

    return fibonacci_series(my_number - 1) + fibonacci_series(my_number - 2)
```

### ⏱ Time Complexity:

* **O(2^n)** ❌ (very slow)

---

## ⚠ Why Fibonacci is Slow?

Because it repeats calculations:

Example:

```
fibonacci(5)
→ fibonacci(4) + fibonacci(3)
→ fibonacci(3) is calculated multiple times
```

---

## 🌍 Real World Examples of Recursion

### 1. 📁 File System (Folders inside folders)

* A folder contains subfolders
* Each subfolder again contains folders
* Same structure → perfect for recursion

---

### 2. 🌐 Website Navigation (Tree Structure)

* Pages linked to other pages
* Like menu → submenu → sub-submenu

---

### 3. 🧮 Mathematical Problems

* Factorial
* Fibonacci
* Power calculation

---

### 4. 🧠 Backtracking Problems

* Sudoku Solver
* Maze solving
* N-Queens problem

---

## ⚠ Important Points to Remember

* Always define a **base condition**
* Reduce the problem size in each step
* Avoid infinite recursion
* Recursion uses **stack memory**
* Sometimes recursion is slower than loops

---

## 🆚 Recursion vs Loop

| Feature      | Recursion                 | Loop                     |
| ------------ | ------------------------- | ------------------------ |
| Readability  | Easy for complex problems | Easy for simple problems |
| Performance  | Slower (sometimes)        | Faster                   |
| Memory Usage | More (stack)              | Less                     |

---

## ✅ Conclusion

Recursion is a powerful concept when:

* Problem can be divided into smaller parts
* Structure is repetitive (tree, graph, etc.)

But always use it wisely due to **memory and performance cost**.

---
