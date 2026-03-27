# 🌳 Binary Tree - Complete Guide (README.md)

## 📌 1. What is a Binary Tree?

A **Binary Tree** is a data structure where:

* Each node has **at most 2 children**
* These children are called:

  * **Left Child**
  * **Right Child**

### ✅ Simple Definition

A binary tree is a tree where each node can have **0, 1, or 2 children**.

---

## 🌿 Structure of Binary Tree

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

### 🔑 Key Points

* First node is called **Root**
* Nodes with no children are called **Leaf Nodes**
* Each node stores:

  * Data
  * Left reference
  * Right reference

---

## 📚 2. Types of Binary Trees

---

### 2.1 Binary Tree (General)

No restriction:

* A node can have 0, 1, or 2 children

---

### 2.2 Binary Search Tree (BST)

### 📌 Condition:

* Left child < Root
* Right child > Root

```
        10
       /  \
      5    20
     / \     \
    2   8     30
```

### 🔑 Logic:

* Used for **fast searching**
* Searching time: O(log n) (average)

---

### 2.3 Strict Binary Tree (Full Binary Tree)

### 📌 Condition:

* Every node has **0 or 2 children**

```
        A
       / \
      B   C
     / \
    D   E
```

### ❌ Not allowed:

Node with only 1 child

---

### 2.4 Complete Binary Tree

### 📌 Condition:

* All levels filled except last
* Last level filled **from left to right**

```
        A
       / \
      B   C
     / \  /
    D  E F
```

---

### 2.5 Extended Binary Tree (2-Tree)

### 📌 Condition:

* Replace NULL with special nodes

```
        A
       / \
      B   C
     / \   \
    D   E   F
   / \ / \ / \
  N  N N  N N N
```

(N = Null node)

---

### 2.6 Skewed Binary Tree

### 📌 Condition:

* All nodes go in one direction

#### Left Skewed:

```
    A
   /
  B
 /
C
```

#### Right Skewed:

```
A
 \
  B
   \
    C
```

### ❌ Problem:

* Works like linked list
* Time complexity becomes O(n)

---

## 📦 3. Representation of Binary Tree

---

## 3.1 Array Representation

### 📌 Storage:

Store elements in array like:

```
Index:  0   1   2   3   4   5   6
Value:  A   B   C   D   E   F   G
```

### 📌 Formula:

| Relation    | Formula      |
| ----------- | ------------ |
| Left Child  | 2*i + 1      |
| Right Child | 2*i + 2      |
| Parent      | (i - 1) // 2 |

---

### 🔑 Example:

If index = 1

* Left = 2*1+1 = 3
* Right = 2*1+2 = 4

---

### ❌ Drawbacks:

* Wastes memory if tree is not complete
* Not suitable for skewed trees

---

## 3.2 Linked List Representation

### 📌 Structure:

Each node contains:

* Data
* Left pointer
* Right pointer

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

---

### ✅ Why we use Linked List?

* Dynamic size (no memory waste)
* Easy insertion and deletion
* Works for all types of trees

---

## 🔄 4. Tree Traversal

Traversal means **visiting all nodes**

---

### 4.1 Inorder (Left → Root → Right)

```
D → B → E → A → C
```

---

### 4.2 Preorder (Root → Left → Right)

```
A → B → D → E → C
```

---

### 4.3 Postorder (Left → Right → Root)

```
D → E → B → C → A
```

---

### 4.4 Level Order (BFS)

```
A → B → C → D → E → F
```

---

## 🎯 Real-World Use Cases

* File system structure
* Database indexing (BST)
* Expression trees (compiler)
* AI decision trees
* Routing algorithms

---

## 🚀 Summary

* Binary tree is a **hierarchical structure**
* Each node has **max 2 children**
* Many types based on structure and rules
* Represented using:

  * Array (fast but limited)
  * Linked List (flexible and widely used)
* Traversal helps to **process all nodes**

---
