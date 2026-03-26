# 📘 Data Structures: Queue, Deque, Circular Queue

This project contains implementation of:

* Queue
* Deque (Double Ended Queue)
* Circular Queue

All are implemented using Python.

---

# 🔹 1. What is Queue?

## 📌 Definition

A **Queue** is a linear data structure that follows:

👉 **FIFO (First In First Out)**
The element inserted first will be removed first.

---

## 📊 Diagram

```
Insert (Rear) → 10 → 20 → 30 → 40 → Remove (Front)

Front                          Rear
  ↓                              ↓
 [10] → [20] → [30] → [40]
```

---

## 🔑 Key Points

* Insertion happens at **rear**
* Deletion happens at **front**
* Works like a **line of people**
* Operations:

  * `enqueue` (insert)
  * `dequeue` (delete)
  * `peek` (see first element)

---

## 🌍 Real World Example

* Queue in a ticket counter 🎟️
* Printer queue 🖨️
* Customer support calls 📞

---

# 🔹 2. What is Deque (Double Ended Queue)?

## 📌 Definition

A **Deque** is a special type of queue where insertion and deletion can happen from **both ends**.

---

## 📊 Diagram

```
Insert/Delete from both sides

Front                         Rear
  ↓                             ↓
 [10] ↔ [20] ↔ [30] ↔ [40]
```

---

## 🔑 Key Points

* Insert at:

  * Front ✅
  * Rear ✅
* Delete from:

  * Front ✅
  * Rear ✅
* More flexible than Queue

---

## 🌍 Real World Example

* Undo/Redo operations in software ↩️
* Browser history navigation 🌐
* Sliding window problems in DSA

---

# 🔹 3. What is Circular Queue?

## 📌 Definition

A **Circular Queue** is a queue where the last position connects back to the first position.

👉 It forms a **circle**

---

## 📊 Diagram

```
Normal Queue Problem:
[10][20][30][40][50]
After delete → space wasted ❌

Circular Queue Solution:

        [10]
     ↗       ↘
   [50]     [20]
     ↘       ↗
        [40] → [30]
```

Or simple view:

```
Index:   0   1   2   3   4
        [10][20][30][40][50]

After some operations:
        [60][70][30][40][50]
          ↑
        reused space
```

---

## 🔑 Key Points

* Last position connects to first 🔁
* Uses **modulo (%)** for rotation
* Avoids memory wastage
* Two pointers:

  * `front`
  * `rear`

---

## ⚙️ Important Conditions

* **Queue Full**

```
(rear + 1) % size == front
```

* **Queue Empty**

```
front == -1
```

---

# 🌍 Real World Examples of Circular Queue

### 1. CPU Scheduling (Round Robin)

* Processes are executed one by one in a loop
* After last process → goes back to first

---

### 2. Music Playlist 🎵

* Songs play in loop
* After last song → first song starts again

---

### 3. Traffic Signal System 🚦

* Signals rotate:

  * Red → Green → Yellow → Red

---

### 4. Multiplayer Game Turns 🎮

* Players take turns in circular order

---

### 5. Buffer Memory (Keyboard / Network)

* Fixed size memory reused again and again

---

# 🚀 Conclusion

* **Queue** → simple FIFO
* **Deque** → flexible (both ends)
* **Circular Queue** → efficient memory usage

---
