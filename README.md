# W4S3M1: In Class Activity


## 🕒 Activity Overview (15–20 min)

**Objective:**

1. Observe and reason about mutable vs. immutable objects via `id()`
2. Practice iterating over lists, using `for` loops, `enumerate`, and common list methods


## Part 1: Mutability vs. Immutability (≈7 min)

1. **Starter snippet (in `exercise.py`):**

   ```python
   # Part 1: Mutable vs Immutable
   a = 100
   b = a
   print("Before:", a, b, id(a), id(b)) 
   #a and b both have the same id currently
   a += 1
   print("After a += 1:", a, b, id(a), id(b))
   #because of iteration, a and be now have different ids.
   x = [1, 2, 3]
   y = x
   print("Before:", x, y, id(x), id(y))
   #x and y have the same id
   x.append(4)
   print("After x.append(4):", x, y, id(x), id(y))
   #x and y still maintain the same id due to lists being mutable objects
   #even though 4 was appended
   ```

2. **Tasks:**

   * **Predict**: What will the `id` values tell us for `a` vs. `b`, and for `x` vs. `y`?
   a & b will share the same id number even while iterated. X and Y will be the same id number until 4 gets appended to x.
   * **Run** the code and **verify** your predictions.
   * **Answer** in comments:

     * Why did `id(a)` change but `id(x)` did not?
       id(a) changed because iterables are immutable and must get a new object and id when attempting to change it. id(x) maintained          the same id because the list was appended making the object mutable.
     * What does this say about integers vs. lists in Python?
       This says that integers, like strings, are immutable objects and lists are mutable.

3. **Deliverable:**

   * Add a short comment under each block explaining your observations.

---

## Part 2: Lists, `for`‑loops, `enumerate`, and Methods (≈10 min)

1. **Extend `exercise.py` with:**

   ```python
   # Part 2: Lists & Loops
   names = ["alice", "bob", "charlie", "dana"]

   # Task A: Upper‑case each name and store in new list
   names = ["alice", "bob", "charlie", "dana"]
   upper_names = []
   for n in names: 
    upper_names.append(n.capitalize())

   print("Uppercase names:", upper_names)

   #Expected output: Uppercasse names: Alice, Bob, Charlie, Dana

   # Task B: Use enumerate to print index + 1 alongside name
   # Expected output:
   # 1. Alice
   # 2. Bob
   # ...
   for idx, names in enumerate(upper_names, start=1): 
    print(f"{idx}. {names}")

   # Task C: Demonstrate at least two list methods (e.g., insert, pop, remove, sort)
   #   1. Insert a new name at position 2
   #   2. Remove "charlie"
   names = ["Alice", "Bob", "Charlie", "Dana"]
   if "Bob" in names:
    names.remove("Bob")
   print(names)
   #   3. Sort the list
   names = ["Alice", "Bob", "Charlie", "Dana"]
   for n in names:
    names.sort(key=len)
   print(names)
   # Print the list after each operation.
   ```

2. **Tasks:**

   * **Fill in** Task A to build `upper_names`.
   * **Implement** Task B using `enumerate`.
   * **Choose** and apply two list methods in Task C; print after each.
   * **Discuss**: What’s the difference between modifying `names` vs. creating a new list?

3. **Deliverable:**

   * Completed code in `exercise.py` with printed output demonstrating each step.

---

## Wrap‑Up & Discussion (≈3 min)

* **Compare**: What patterns did you notice about mutability?
Mutability tends to update stored information without the need to create brand new data. Mutability also has a more efficient recall on memory stores and maintains the same id address.

* **Reflect**: When might you prefer immutability?
When you want to prevent data from erroneously being changed, to allow for the interpreter to cache, use memory and improve performance, and to ensure a function doesn't mistakenly change inputs.

When is a list’s mutability useful?
A lists mutability is useful when updating collections of data, maintaining the tracking of data, and efficient memory use via updating the data.

* **Share** one new thing you learned with the class.
One new thing I learned in this class is that there are a variety of methods that allow for more efficient coding and faster code processing.



Discuss your observations with your partner and be ready to share!
