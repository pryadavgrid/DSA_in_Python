# 🔄 Sorting in DSA

Sorting means arranging data in a specific order.

👉 Example:
`[5, 2, 9, 1] → [1, 2, 5, 9]` (Ascending order)

Sorting is very important because:

* It makes searching faster
* It helps organize data
* It is used in many real-world applications

---

# 📚 Types of Sorting You Will Learn

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort

---

# 🫧 1. Bubble Sort

## 🧠 Idea

Compare **adjacent elements** and swap if they are in wrong order.

👉 Biggest element goes to the end in each pass.

## 🔄 Approach

* Start from index 0
* Compare with next element
* Swap if needed
* Repeat for all elements
* After each round, one element is fixed

## 📊 Diagram

```
Initial:  [5, 2, 4, 1]

Pass 1:
[5, 2] → swap → [2, 5, 4, 1]
[5, 4] → swap → [2, 4, 5, 1]
[5, 1] → swap → [2, 4, 1, 5]

Pass 2:
[2, 4] → ok
[4, 1] → swap → [2, 1, 4, 5]

Pass 3:
[2, 1] → swap → [1, 2, 4, 5]
```

✅ Final: `[1, 2, 4, 5]`

---

# 🎯 2. Selection Sort

## 🧠 Idea

Find the **smallest element** and place it at correct position.

## 🔄 Approach

* Find minimum element
* Swap with first position
* Then find next minimum
* Repeat

## 📊 Diagram

```
Initial: [5, 2, 4, 1]

Step 1:
Minimum = 1 → swap with 5
[1, 2, 4, 5]

Step 2:
Minimum = 2 → already correct

Step 3:
Minimum = 4 → already correct
```

✅ Final: `[1, 2, 4, 5]`

---

# ✍️ 3. Insertion Sort

## 🧠 Idea

Build sorted array **one element at a time**.

👉 Like sorting cards in hand.

## 🔄 Approach

* Take one element
* Compare with left side
* Insert at correct position

## 📊 Diagram

```
Initial: [5, 2, 4, 1]

Step 1:
Take 2 → insert before 5
[2, 5, 4, 1]

Step 2:
Take 4 → insert between 2 and 5
[2, 4, 5, 1]

Step 3:
Take 1 → insert at start
[1, 2, 4, 5]
```

✅ Final: `[1, 2, 4, 5]`

---

# 🔀 4. Merge Sort

## 🧠 Idea

Divide → Sort → Merge

👉 Uses **Divide and Conquer**

## 🔄 Approach

1. Divide array into halves
2. Keep dividing until single element
3. Merge them in sorted order

## 📊 Diagram

```
Initial: [5, 2, 4, 1]

Divide:
[5, 2]   [4, 1]
[5] [2]  [4] [1]

Merge:
[5] + [2] → [2, 5]
[4] + [1] → [1, 4]

Final Merge:
[2, 5] + [1, 4] → [1, 2, 4, 5]
```

✅ Final: `[1, 2, 4, 5]`

---

# ⚡ 5. Quick Sort

## 🧠 Idea

Pick a **pivot** and arrange:

* Smaller elements → left
* Bigger elements → right

## 🔄 Approach

1. Choose pivot (example: last element)
2. Place pivot at correct position
3. Repeat for left and right parts

## 📊 Diagram

```
Initial: [5, 2, 4, 1]

Pivot = 1

Step:
[ ] 1 [5, 2, 4]

Now sort right part:
Pivot = 4

[2] 4 [5]

Final:
[1, 2, 4, 5]
```

✅ Final: `[1, 2, 4, 5]`

---

# 🧾 Quick Summary

| Sorting Type   | Idea                    | Speed     |
| -------------- | ----------------------- | --------- |
| Bubble Sort    | Swap adjacent           | Slow      |
| Selection Sort | Pick minimum            | Slow      |
| Insertion Sort | Insert in correct place | Medium    |
| Merge Sort     | Divide & Merge          | Fast      |
| Quick Sort     | Pivot based sorting     | Very Fast |

---

# 🧠 Final Tip

* **Bubble** → push biggest to end
* **Selection** → pick smallest
* **Insertion** → insert like cards
* **Merge** → divide & merge
* **Quick** → pivot & split
