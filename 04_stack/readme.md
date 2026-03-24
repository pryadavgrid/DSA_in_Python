# Stack Implementation in Python

## 📌 Overview

This project is a simple implementation of a **Stack Data Structure** using Python.

A stack follows the **LIFO (Last In First Out)** principle.

* The last element added is the first one to be removed.

Example:

```
Push: 10 → 20 → 30
Pop: 30 → 20 → 10
```

---

## 📂 Code Structure

The project contains one class:

### 1. Stack Class

This class is used to create and manage stack operations.

---

## ⚙️ Functions Explained

### 1. `__init__(self)`

* This is a constructor.
* It initializes an empty list to store stack elements.

```
self.my_stack = []
```

---

### 2. `lenght_of_stack(self)`

* Returns the number of elements in the stack.

```
return len(self.my_stack)
```

---

### 3. `push_element(self, val)`

* Adds a new element to the top of the stack.
* Here, index `0` is considered as the top.

```
self.my_stack.insert(0, val)
```

---

### 4. `peek(self)`

* Returns the top element without removing it.
* If stack is empty, it raises an exception.

```
return self.my_stack[0]
```

---

### 5. `pop_element(self)`

* Removes and returns the top element.
* If stack is empty, it raises an exception.

```
return self.my_stack.pop(0)
```

---

## ▶️ How the Code Works

### Step 1: Create Stack

```
stack = Stack()
```

### Step 2: Push Elements

```
stack.push_element(10)
stack.push_element(20)
stack.push_element(30)
```

Stack becomes:

```
[30, 20, 10]
```

---

### Step 3: Pop Elements

```
print(stack.pop_element())  # 30
print(stack.pop_element())  # 20
print(stack.pop_element())  # 10
```

---

### Step 4: Peek

```
print(stack.peek())
```

❗ This will raise an exception because stack is empty.

---

## 🧠 Key Concepts

* Stack follows **LIFO**
* Top element is at index `0`
* Uses Python list internally
* Operations:

  * Push → Insert element
  * Pop → Remove element
  * Peek → View top element

---

## 🚀 Improvement Suggestions

1. Use `append()` instead of `insert(0, val)` for better performance
2. Use `pop()` instead of `pop(0)`

### Better Version:

```
self.my_stack.append(val)
self.my_stack.pop()
```

👉 This makes stack operations faster (O(1))

---

## ✅ Conclusion

This is a basic and good implementation of a stack in Python. With small improvements, it can be more efficient and production-ready.

---

If you want, I can also:

* Convert this into a project file structure
* Add unit tests
* Improve code with best practices
