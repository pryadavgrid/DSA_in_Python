# 📦 Heap Data Structure (Easy + Visual Revision)

---

## 🧠 What is Heap?

👉 Heap = **Complete Binary Tree + Rule**

### 🔑 Two Things to Remember:

1. **Shape Rule** → Complete Binary Tree
2. **Order Rule** → Min or Max Heap

---

## 🌳 Structure (VERY IMPORTANT)

👉 Complete Binary Tree means:

* All levels filled
* Last level filled **from left to right**

```
        10
       /  \
     20    30
    /  \
  40   50
```

✅ Correct Heap Shape
❌ No gaps allowed between nodes

---

## 🔄 Types of Heap

### 🔽 Min Heap (Smallest on Top)

👉 Parent is always **smaller**

```
        10
       /  \
     20    30
    /  \
  40   50
```

👉 Root = **Smallest Element**

---

### 🔼 Max Heap (Largest on Top)

👉 Parent is always **greater**

```
        50
       /  \
     30    40
    /  \
  10   20
```

👉 Root = **Largest Element**

---

## 📊 Array Representation (MUST REMEMBER ⭐)

Heap is stored like this:

```
Tree:              Array:
   10               [10, 20, 30, 40, 50]
  /  \
20    30
/
40
```

### 🔑 Formula:

* Parent → (i - 1) // 2
* Left → 2*i + 1
* Right → 2*i + 2

👉 This is **very important for exams/interviews**

---

## ⚙️ Operations (CORE PART)

---

## ➕ Insert (Add Element)

### Example: Insert 15

### Step 1: Add at end

```
        10
       /  \
     20    30
    /
  40

After insert:

        10
       /  \
     20    30
    /  \
  40   15
```

---

### Step 2: Fix (Heapify UP ⬆️)

Compare with parent:

```
        10
       /  \
     15    30
    /  \
  40   20
```

👉 Move **up until rule is satisfied**

---

## ❌ Delete (Remove Root)

👉 Always delete **root element**

---

### Step 1: Replace root with last element

```
Before:
        10
       /  \
     20    30
    /  \
  40   50

After replace:
        50
       /  \
     20    30
    /
  40
```

---

### Step 2: Fix (Heapify DOWN ⬇️)

```
        20
       /  \
     40    30
    /
  50
```

👉 Move **down until rule is correct**

---

## 🔧 Heapify (IMPORTANT ⭐)

### ⬆️ Heapify UP

* Used in **Insert**
* Move element **UP**

---

### ⬇️ Heapify DOWN

* Used in **Delete**
* Move element **DOWN**

---

## 🔍 Search

👉 You must check all elements

```
[10, 20, 30, 40, 50]
```

👉 No shortcut ❌
👉 Time = **O(n)**

---

## ⚡ Time Complexity (Quick)

| Operation | Time     |
| --------- | -------- |
| Insert    | O(log n) |
| Delete    | O(log n) |
| Search    | O(n)     |
| Get Root  | O(1)     |

---

## 🌍 Real-Life Examples

👉 Easy to remember:

* 🎯 Priority Queue (VIP first)
* 🧠 CPU Scheduling
* 🗺️ Shortest Path (Dijkstra)
* 🔄 Heap Sort

---

## ⚡ Memory Tricks (SUPER IMPORTANT 🚀)

👉 Heap = **Complete Tree + Rule**
👉 Root = **Answer (min/max)**
👉 Insert = **Go UP ⬆️**
👉 Delete = **Go DOWN ⬇️**
👉 Array formulas = ⭐ MUST

---