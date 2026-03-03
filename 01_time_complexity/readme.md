Here is your corrected and well-structured **README.md** file in simple English for better understanding.

---

# 📘 Time Complexity & Asymptotic Analysis (Simple Guide)

## 📌 What is `n`?

* `n` = Size of input
* Example: If an array has 10 elements, then `n = 10`

---

# 📊 Order of Growth (Comparison)

When input size increases, running time also increases.

```
1 < log log n < log n < n < n log n < n² < n³ < 2ⁿ
```

👉 From left to right, time complexity becomes slower.

---

# 📐 Mathematical Functions (Basic Understanding)

These math functions help us understand time complexity.

### 1️⃣ Constant Function

* Example: `y = 5`
* Output does NOT depend on input `x`
* Value is always same
* Time Complexity → **O(1)**

---

### 2️⃣ Linear Function

* Example: `y = 2x + 5`
* Power of `x` is 1
* Time Complexity → **O(n)**

---

### 3️⃣ Quadratic Function

* Example: `y = 2x² + 3x - 5`
* Power of `x` is 2
* Time Complexity → **O(n²)**

---

### 4️⃣ Cubic Function

* Example: `y = 3x³ + 2x + 5`
* Power of `x` is 3
* Time Complexity → **O(n³)**

---

### 5️⃣ Logarithmic Function

* Example: `y = log(x) + 2`
* Time Complexity → **O(log n)**

---

### 6️⃣ Exponential Function

* Example: `y = 3ˣ + 3`
* Time Complexity → **O(2ⁿ)** (very slow)

---

# ⭐ Dominating Term (Very Important)

In time complexity, we only write the biggest growing term.

Example:

```
2 + 4n + n²
```

We remove small values and constants.

Final Answer → **O(n²)**

We ignore:

* Constants (2, 4)
* Smaller terms (n)

---

# 📈 Types of Asymptotic Notations

| Case Type    | Notation  |
| ------------ | --------- |
| Best Case    | Ω (Omega) |
| Average Case | Θ (Theta) |
| Worst Case   | O (Big O) |

Most commonly used → **Big O Notation**

---

# 🔵 1. Constant Time — O(1)

Code does NOT depend on input size.

### Example:

```python
x = 5
print(x)

if x == 5:
    print("Hello")
else:
    print("Welcome")
```

✅ No loop
✅ No recursion
✅ Runs same time always

Time Complexity → **O(1)**

---

# 🟢 2. Linear Time — O(n)

When code runs in a single loop depending on `n`.

### Example 1:

```python
n = 5
print(n)

for i in range(n):
    print(i)
```

Calculation:

```
1 + 1 + n + n
= 2 + 2n
```

Remove constants → **O(n)**

---

### Example 2 (Two Independent Loops)

```python
n = 5

for i in range(n):
    print(i)

for i in range(n):
    print(i)
```

Calculation:

```
n + n
= 2n
```

Final → **O(n)**

👉 Independent loops add, not multiply.

---

# 🟡 3. Quadratic Time — O(n²)

When one loop is inside another loop.

### Example:

```python
n = 5

for i in range(n):
    for j in range(n):
        print(i, j)
```

Calculation:

```
n × n = n²
```

Time Complexity → **O(n²)**

---

# 🟠 4. Cubic Time — O(n³)

When three nested loops are used.

### Example:

```python
n = 5

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
```

Calculation:

```
n × n × n = n³
```

Time Complexity → **O(n³)**

---

# 🔵 5. Logarithmic Time — O(log n)

When value increases or decreases by dividing or multiplying.

Usually seen in:

* Binary Search
* Dividing problem into half

### Example 1 (Divide by 2)

```python
n = 16

while n >= 1:
    print(n)
    n = n // 2
```

Each step:

```
16 → 8 → 4 → 2 → 1
```

Time Complexity → **O(log n)**

---

### Example 2 (Multiply by 2)

```python
n = 1

while n < 16:
    print(n)
    n = n * 2
```

Each step:

```
1 → 2 → 4 → 8 → 16
```

Time Complexity → **O(log n)**

---

# 🚨 Important Rules

✔ Ignore constants
✔ Ignore smaller terms
✔ Focus on highest power
✔ Nested loops multiply
✔ Independent loops add

---

# 🧠 Quick Summary

| Type        | Complexity |
| ----------- | ---------- |
| Constant    | O(1)       |
| Logarithmic | O(log n)   |
| Linear      | O(n)       |
| Quadratic   | O(n²)      |
| Cubic       | O(n³)      |
| Exponential | O(2ⁿ)      |

---

# 🎯 Final Thought

As input size (`n`) increases:

* O(1) → Fastest
* O(log n) → Very Fast
* O(n) → Good
* O(n²) → Slow
* O(2ⁿ) → Very Slow