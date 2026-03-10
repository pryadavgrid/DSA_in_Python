# Linked List (Data Structure)

## What is a Linked List?

A **Linked List** is a linear data structure where elements are stored in **nodes**.
Each node stores some **data** and a **pointer (address)** to the next node.

Unlike arrays, elements in a linked list are **not stored in continuous memory**.
Nodes can be stored **anywhere in memory** and connected using pointers.

---

# Node Structure

Each node has **two parts**.

```
+--------+--------+
| Data   | Next   |
+--------+--------+
```

**Data** → stores the value
**Next** → stores the address of the next node

Example node:

```
+--------+--------+
|  10    |   •    |
+--------+--------+
```

---

# Example of a Linked List

```
Head → [10 | • ] → [20 | • ] → [30 | NULL]
```

Explanation:

* **Head** stores the address of the first node
* Each node points to the **next node**
* The last node points to **NULL**

---

# Why We Use Linked List

Linked Lists are used when we need **dynamic memory and flexible data storage**.

## 1. Dynamic Size

Arrays have **fixed size**, but linked lists can **grow or shrink easily**.

Example:

Array

```
[10, 20, 30, _ , _]
```

Linked List

```
10 → 20 → 30 → 40 → 50
```

We can add nodes anytime.

---

## 2. Easy Insertion and Deletion

In arrays, when we insert or delete an element, many elements must **shift**.

Example in array:

```
[10, 20, 30]
Insert 15

[10, 15, 20, 30]  ← shifting required
```

In linked list:

```
10 → 20 → 30

Insert 15

10 → 15 → 20 → 30
```

We only change **pointers**, not move data.

---

## 3. Better Memory Usage

Linked Lists allocate memory **only when needed**.

Arrays allocate memory **in advance**.

---

## 4. Useful in Many Data Structures

Linked Lists are used to implement:

* **Stack**
* **Queue**
* **Graph**
* **Hash Tables**
* **Memory Management**

---

# Types of Linked Lists

There are four main types.

1. Singly Linked List
2. Doubly Linked List
3. Circular Linked List
4. Circular Doubly Linked List

---

# 1. Singly Linked List

A **Singly Linked List** is the simplest type.

Each node has:

* Data
* Next pointer

Nodes move in **one direction only (forward)**.

### Structure

```
Head → [10 | • ] → [20 | • ] → [30 | NULL]
```

Explanation:

* Node **10** points to **20**
* Node **20** points to **30**
* Node **30** points to **NULL**

---

## Operations in Singly Linked List

### 1. Traversal

Traversal means **visiting every node**.

```
Head → 10 → 20 → 30 → NULL
```

Steps:

1. Start from **Head**
2. Move to next node
3. Continue until **NULL**

---

### 2. Insert at Beginning

```
Before

Head → [10] → [20] → [30]

After inserting 5

Head → [5] → [10] → [20] → [30]
```

New node becomes the **new head**.

---

### 3. Insert at End

```
Before

10 → 20 → 30 → NULL

After inserting 40

10 → 20 → 30 → 40 → NULL
```

---

### 4. Insert at Middle

```
Before

10 → 20 → 30 → NULL

Insert 25

10 → 20 → 25 → 30 → NULL
```

---

### 5. Delete First Node

```
Before

10 → 20 → 30

After deletion

20 → 30
```

---

### 6. Delete Last Node

```
Before

10 → 20 → 30

After deletion

10 → 20
```

---

### 7. Delete Specific Node

```
Before

10 → 20 → 30 → 40

Delete 30

10 → 20 → 40
```

---

### 8. Searching

Searching means **finding a value** in the list.

Example:

```
10 → 20 → 30 → 40
```

Search **30**

We check each node until the value is found.

---

# 2. Doubly Linked List

In a **Doubly Linked List**, each node has **three parts**.

```
+--------+--------+--------+
| Prev   | Data   | Next   |
+--------+--------+--------+
```

Example structure:

```
NULL ← [NULL | 10 | • ] ⇄ [ • | 20 | • ] ⇄ [ • | 30 | NULL] → NULL
```

Explanation:

* **Prev** → address of previous node
* **Next** → address of next node

---

## Advantages

* Can move **forward**
* Can move **backward**

---

## Disadvantages

* Uses **more memory**
* Slightly **more complex**

---

# 3. Circular Linked List

In a **Circular Linked List**, the last node **does not point to NULL**.

Instead, it points back to the **first node**.

```
Head → [10 | • ] → [20 | • ] → [30 | • ]
  ↑                                      |
  |______________________________________|
```

This creates a **circle**.

---

## Advantages

* Traversal can continue **forever**
* Useful in **round robin scheduling**

---

# 4. Circular Doubly Linked List

This is a combination of:

* Doubly Linked List
* Circular Linked List

Each node has:

```
+--------+--------+--------+
| Prev   | Data   | Next   |
+--------+--------+--------+
```

Structure:

```
      ⇄ [10] ⇄ [20] ⇄ [30] ⇄
      ↑                     ↓
      ← ← ← ← ← ← ← ← ← ← ←
```

The last node connects back to the first node.

---

# Comparison of Linked List Types

| Type                        | Direction          | Last Node      |
| --------------------------- | ------------------ | -------------- |
| Singly Linked List          | Forward            | NULL           |
| Doubly Linked List          | Forward + Backward | NULL           |
| Circular Linked List        | Forward            | Points to Head |
| Circular Doubly Linked List | Forward + Backward | Circular       |

---

# Important Points

* Linked Lists store data in **nodes**
* Each node has a **pointer**
* Memory is **not continuous**
* Insertion and deletion are **easy**
* Searching takes **more time than arrays**

---

# Summary

A **Linked List** is a flexible data structure used to store data dynamically.

Key features:

* Nodes connected using pointers
* Easy insertion and deletion
* Dynamic memory usage

Linked Lists are an important concept in **Data Structures and Algorithms** and are used to build many other data structures.
